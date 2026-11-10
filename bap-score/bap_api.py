# Open API 모듈
# - 나이스 급식 API 호출 담당

import os
import pprint
import requests
from dotenv import load_dotenv

# ===========================================================
#  1. 준비하기
#  - .env 파일에서 NEIS_API_KEY 불러오기
#  - 상수 데이터 설정
# ===========================================================

load_dotenv()
NEIS_API_KEY = os.getenv("NEIS_API_KEY")  # Neis API key
SC_CODE = os.getenv("SC_CODE")            # 시도교육청구분코드
SCHUL_CODE = os.getenv('SCHUL_CODE')      # 행정표준코드

# ===========================================================
#  2. Open API 호출
# ===========================================================

def get_bap(mlsv_ymd, sc_code=SC_CODE, schul_code=SCHUL_CODE):
    """
    급식 제공일, 시도교육청구분코드(기본값 디미고), 행정표준코드(기본값 디미고)를 입력받습니다.
    Neis API로 급식 정보를 불러오고, (일자, 구분, 메뉴, 칼로리) 형태의 튜플을 원소로 갖는 리스트를 반환합니다.
    """
    try:
        # ---------- Neis API로 요청 날리기 ----------
        url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
        params = {
            "KEY": NEIS_API_KEY,
            "Type": "json",
            "pIndex": "1",
            "pSize": "100",
            "ATPT_OFCDC_SC_CODE": sc_code,
            "SD_SCHUL_CODE": schul_code,
            "MLSV_YMD": mlsv_ymd,
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        # ---------- 응답코드 확인 (급식이 없는 날은 INFO-200) ----------
        if "RESULT" in data:
            result = data["RESULT"]
            if result["CODE"] == "INFO-200":
                return []                   # 급식이 없으므로 빈 리스트 반환
            raise Exception((result["CODE"], result["MESSAGE"]))

        # ---------- 파싱하여 rows에 급식 정보 저장 ----------
        rows = []
        for row in data["mealServiceDietInfo"][1]["row"]:

            # dish = row["DDISH_NM"].replace("<br/>", "\n")
            dishes = []
            dish_origin = row["DDISH_NM"].split("<br/>")
            for menu in dish_origin:
                m = menu
                m = m.replace(")", "")
                m = m.replace("(", "")
                dishes.append(m)
            dish_str = "\n".join(dishes)

            rows.append(
                (row["MLSV_YMD"],           # 일자
                 row["MMEAL_SC_NM"],        # 구분
                 dish_str,                  # 메뉴
                 row["CAL_INFO"])           # 칼로리
            )

        # ---------- rows 반환 ----------
        return rows

    except Exception as e:
        print(f"Open API 오류 발생: {e}")
        raise