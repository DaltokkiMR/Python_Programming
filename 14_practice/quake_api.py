# Open API 모듈
# - USGS 지진 정보 API 호출 담당
# - [문제 1] get_earthquakes() 함수를 완성하세요. (problem.md, api.md 참고)

import requests

# ===========================================================
#  1. 준비하기
#  - USGS 지진 API는 인증키가 필요 없음
#  - REGIONS: 지역 이름 → 위도/경도 범위 파라미터 (api.md 1-2 참고)
# ===========================================================

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

REGIONS = {
    "전 세계": {},
    "한국·일본 주변": {"minlatitude": 30, "maxlatitude": 46, "minlongitude": 122, "maxlongitude": 146},
    "동남아시아": {"minlatitude": -11, "maxlatitude": 21, "minlongitude": 92, "maxlongitude": 141},
    "남미 서부": {"minlatitude": -56, "maxlatitude": 5, "minlongitude": -82, "maxlongitude": -66},
    "알래스카": {"minlatitude": 51, "maxlatitude": 72, "minlongitude": -180, "maxlongitude": -129},
}


# ===========================================================
#  2. Open API 호출
#  - min_mag : 최소 규모
#  - region  : REGIONS의 키 (지역 이름)
#  - 반환값  : 최근 30일 지진 정보 dict 리스트 (최신순)
# ===========================================================

def get_earthquakes(min_mag=4.5, region="전 세계"):
    try:
        # TODO 1-1. 요청 파라미터 만들기 (api.md "1-2. 요청 파라미터")
        #  - minmagnitude, eventtype, orderby 를 추가하세요.
        #  - starttime, endtime은 넣지 않습니다. (생략하면 최근 30일)
        #  - REGIONS[region]의 위도/경도 범위도 params에 추가하세요.
        params = {
            "format": "geojson",
        }

        # TODO 1-2. requests.get()으로 요청 보내기 (timeout=10)


        # TODO 1-3. 상태 코드가 200이 아니면 예외 발생
        #  - 오류 응답은 JSON이 아니라 텍스트! → response.text 를 메시지에 포함


        # TODO 1-4. 응답 JSON의 features를 하나씩 dict로 바꿔서 quakes에 추가
        #  - dict 키: 경과(시간), 규모, 위치, 깊이(km), 위도, 경도, 링크
        #  - coordinates 순서 주의! [경도, 위도, 깊이]
        #  - 경과(시간): (metadata의 generated - properties의 time) 밀리초 → 시간
        quakes = []


        return quakes

    except Exception as e:
        print(f"Open API 오류 발생: {e}")
        raise


# ===========================================================
#  3. 테스트 (python quake_api.py 로 실행)
# ===========================================================

if __name__ == "__main__":
    result = get_earthquakes(4.5, "전 세계")
    print(f"조회 건수: {len(result)}")
    for quake in result[:3]:
        print(quake)
