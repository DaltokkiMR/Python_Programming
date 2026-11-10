# [모범 답안] Open API 모듈
# - USGS 지진 정보 API 호출 담당

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
        # starttime, endtime을 생략하면 최근 30일을 조회
        params = {
            "format": "geojson",
            "minmagnitude": min_mag,
            "eventtype": "earthquake",      # 채석장 발파 등 제외
            "orderby": "time",              # 최신순
        }
        params.update(REGIONS[region])      # 지역의 위도/경도 범위 추가

        response = requests.get(URL, params=params, timeout=10)

        # 오류 응답은 JSON이 아닌 텍스트이므로 json() 전에 상태 코드부터 확인
        if response.status_code != 200:
            raise Exception(f"상태 코드 {response.status_code}: {response.text}")

        data = response.json()

        # 응답이 만들어진 시각(= 지금, 밀리초)
        now_ms = data["metadata"]["generated"]

        quakes = []
        for feature in data["features"]:
            props = feature["properties"]
            lon, lat, depth = feature["geometry"]["coordinates"]    # 순서 주의! [경도, 위도, 깊이]

            # 몇 시간 전에 발생했는지: (지금 - 발생 시각) 밀리초 → 시간 (1시간 = 3,600,000ms)
            hours_ago = (now_ms - props["time"]) / 3600000

            quakes.append({
                "경과(시간)": round(hours_ago, 1),
                "규모": props["mag"],
                "위치": props["place"],
                "깊이(km)": depth,
                "위도": lat,
                "경도": lon,
                "링크": props["url"],
            })

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
