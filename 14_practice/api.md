# USGS 지진 정보 Open API 명세

> 미국 지질조사국(USGS)이 전 세계 지진 정보를 실시간으로 제공하는 Open API
> (2026-11-10 직접 호출해서 키값 확인함, API 버전 2.8.4)

| 항목 | 내용 |
|---|---|
| 제공기관 | 미국 지질조사국 USGS (U.S. Geological Survey) |
| 공식 문서 | https://earthquake.usgs.gov/fdsnws/event/1/ |
| 인증키 | **필요 없음** (회원가입, 키 발급 없이 바로 사용) |
| 요청 방식 | `GET` |
| 응답 형식 | GeoJSON (JSON 형식의 지리 정보 표준) |
| 조회 제한 | 1회 최대 **20,000건** |

---

## 1. 요청 (Request)

### 1-1. 요청 URL

| 용도 | URL |
|---|---|
| 지진 목록 조회 | `https://earthquake.usgs.gov/fdsnws/event/1/query` |
| 건수만 조회 | `https://earthquake.usgs.gov/fdsnws/event/1/count` |

### 1-2. 요청 파라미터

| 키 | 필수 | 타입 | 설명 | 예시 |
|---|:---:|---|---|---|
| `format` | ✅ | string | 응답 형식. JSON으로 받으려면 `geojson` | `geojson` |
| `starttime` | | string | 조회 시작 일시 (ISO-8601). 기본값: 30일 전 | `2026-11-03` |
| `endtime` | | string | 조회 종료 일시 (ISO-8601). 기본값: 현재 | `2026-11-10` |
| `minmagnitude` | | float | 최소 규모 (이 값 **이상**) | `4.5` |
| `maxmagnitude` | | float | 최대 규모 (이 값 이하) | `7.0` |
| `eventtype` | | string | 이벤트 종류. 지진만 보려면 `earthquake` (채석장 발파 `quarry blast`, 폭발 `explosion` 등 제외) | `earthquake` |
| `orderby` | | string | 정렬 기준<br>`time`: 최신순 (기본값)<br>`time-asc`: 오래된 순<br>`magnitude`: 규모 큰 순<br>`magnitude-asc`: 규모 작은 순 | `magnitude` |
| `limit` | | int | 최대 조회 건수 (1 ~ 20000) | `100` |
| `minlatitude`, `maxlatitude` | | float | 사각형 영역 검색: 위도 범위 (-90 ~ 90) | `33`, `39` |
| `minlongitude`, `maxlongitude` | | float | 사각형 영역 검색: 경도 범위 (-180 ~ 180) | `124`, `132` |
| `latitude`, `longitude`, `maxradiuskm` | | float | 원형 영역 검색: 중심 좌표와 반경(km) | `36`, `128`, `500` |

### 1-3. ⏰ 시간 파라미터 주의사항

- 시간대(타임존)를 쓰지 않으면 **UTC(세계 표준시)** 로 해석한다. 한국시간(KST)은 UTC보다 **9시간 빠르다** (UTC+9).
- 날짜만 쓰면 그날 `00:00:00`으로 해석한다. 그래서 `endtime=2026-11-10`으로 요청하면 11월 10일 지진은 **포함되지 않는다**.
- 한국 날짜 기준으로 조회하려면 뒤에 `+09:00`을 붙인다.
  ```
  starttime=2026-11-08T00:00:00+09:00     ← 11월 8일 0시 (한국시간)
  endtime=2026-11-08T23:59:59+09:00       ← 11월 8일 23시 59분 59초 (한국시간)
  ```
  `requests`의 `params`로 넘기면 `+`, `:` 같은 특수문자는 자동으로 URL 인코딩된다 (`+` → `%2B`).

### 1-4. 요청 예시

```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-11-03&endtime=2026-11-10&minmagnitude=4.5
```

> 💡 이 주소를 브라우저 주소창에 붙여 넣으면 응답 JSON을 바로 확인할 수 있다. 크롬에서는 "꾸밈 출력(pretty print)"에 체크하면 보기 편하다.

---

## 2. 응답 (Response)

### 2-1. 전체 구조

```
응답 (dict)
├── type          : "FeatureCollection"
├── metadata      : 요청 정보 (dict)
├── features      : 지진 목록 (list)                    ★
│   └── [i]       : 지진 1건 (dict)
│       ├── type        : "Feature"
│       ├── id          : 지진 고유 ID
│       ├── properties  : 지진 정보 (dict)             ★ mag, place, time, url ...
│       └── geometry    : 발생 위치 (dict)             ★
│           ├── type        : "Point"
│           └── coordinates : [경도, 위도, 깊이]       ★ 순서 주의!
└── bbox          : 조회된 지진 전체를 감싸는 영역 [최소경도, 최소위도, 최소깊이, 최대경도, 최대위도, 최대깊이]
```

꺼내는 방법 예시:

```python
data = response.json()
data["features"]                                   # 지진 목록 (list)
data["features"][0]["properties"]["mag"]           # 첫 번째 지진의 규모
data["features"][0]["geometry"]["coordinates"][1]  # 첫 번째 지진의 위도
```

### 2-2. `metadata`

| 키 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `generated` | int | 응답 생성 시각 (밀리초) | `1794281255000` |
| `url` | string | 요청한 URL | `"https://earthquake.usgs.gov/fdsnws/event/1/query?..."` |
| `title` | string | 제목 | `"USGS Earthquakes"` |
| `status` | int | 상태 코드 | `200` |
| `api` | string | API 버전 | `"2.8.4"` |
| `count` | int | 조회된 지진 수 ※ `limit`을 쓰면 이 키가 **없고** 대신 `limit`, `offset` 키가 온다 | `29` |

### 2-3. `features[i]`

| 키 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `type` | string | 항상 `"Feature"` | `"Feature"` |
| `id` | string | 지진 고유 ID | `"us7000tx38"` |
| `properties` | dict | 지진 정보 (아래 2-4) | |
| `geometry` | dict | 발생 위치 (아래 2-5) | |

### 2-4. `features[i]["properties"]`

굵게 표시한 키가 이번 문제에서 쓰는 키이다.

| 키 | 타입 | 설명 | 예시 |
|---|---|---|---|
| **`mag`** | float | 규모 | `5.3` |
| **`place`** | string | 발생 위치 설명 (영문) | `"80 km ENE of Lagunas, Peru"` |
| **`time`** | int | 발생 시각. 1970-01-01 00:00:00 UTC부터 지난 **밀리초(ms)** | `1794219833528` |
| `updated` | int | 정보가 마지막으로 수정된 시각 (밀리초) | `1794220569040` |
| `tz` | null | 사용하지 않음 (항상 `null`) | `null` |
| **`url`** | string | USGS 상세 정보 웹페이지 주소 | `"https://earthquake.usgs.gov/earthquakes/eventpage/us7000tx38"` |
| `detail` | string | 이 지진 1건의 상세 정보 API 주소 (GeoJSON) | `"https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000tx38&format=geojson"` |
| `felt` | int / null | "흔들림을 느꼈다"는 신고 수 | `null` |
| `cdi` | float / null | 신고 기반 최대 진도 | `null` |
| `mmi` | float / null | 계측 기반 최대 진도 | `null` |
| `alert` | string / null | 피해 예상 경보 등급 (PAGER): `green` < `yellow` < `orange` < `red` | `null` |
| `status` | string | 검토 상태: `automatic`(자동 분석) / `reviewed`(전문가 검토 완료) | `"reviewed"` |
| `tsunami` | int | 해양 지역의 큰 지진이면 `1`, 아니면 `0` ※ 실제 쓰나미 발생 여부는 아님 | `0` |
| `sig` | int | 중요도 점수 (규모, 신고 수, 피해 예상으로 계산, 보통 0 ~ 1000) | `432` |
| `net` | string | 정보를 제공한 관측망 ID | `"us"` |
| `code` | string | 관측망 내부 ID | `"7000tx38"` |
| `ids` | string | 관련 ID 목록 (쉼표로 구분) | `",us7000tx38,"` |
| `sources` | string | 정보 출처 목록 (쉼표로 구분) | `",us,"` |
| `types` | string | 제공되는 정보 종류 (쉼표로 구분) | `",origin,phase-data,"` |
| `nst` | int / null | 위치 계산에 사용된 관측소 수 | `66` |
| `dmin` | float / null | 가장 가까운 관측소까지의 거리 (도 단위) | `4.572` |
| `rms` | float | 계산 오차 (초) | `0.91` |
| `gap` | float / null | 관측소 사이의 최대 방위각 간격 (도) | `90` |
| `magType` | string | 규모 계산 방식 (`mb`, `ml`, `mww` 등) | `"mb"` |
| `type` | string | 이벤트 종류 (`earthquake`, `quarry blast`, `explosion` 등) | `"earthquake"` |
| `title` | string | 제목. `"M 규모 - 위치"` 형식 | `"M 5.3 - 80 km ENE of Lagunas, Peru"` |

### 2-5. `features[i]["geometry"]`

| 키 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `type` | string | 항상 `"Point"` | `"Point"` |
| **`coordinates`** | list | **[경도(longitude), 위도(latitude), 깊이(km)]** | `[-75.0002, -4.9495, 11.49]` |

> ⚠️ **순서 주의!** 위도가 아니라 **경도가 먼저** 온다. (GeoJSON 표준이 [x, y] = [경도, 위도] 순서)
> 깊이는 땅속으로 들어간 거리(km)이며, 해발 고도 때문에 드물게 음수가 나올 수 있다.

### 2-6. 실제 응답 예시

`minmagnitude=5`로 호출한 실제 결과 (features는 1건만 표시)

```json
{
  "type": "FeatureCollection",
  "metadata": {
    "generated": 1794281255000,
    "url": "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-11-01&endtime=2026-11-10&minmagnitude=5",
    "title": "USGS Earthquakes",
    "status": 200,
    "api": "2.8.4",
    "count": 29
  },
  "features": [
    {
      "type": "Feature",
      "properties": {
        "mag": 5.3,
        "place": "80 km ENE of Lagunas, Peru",
        "time": 1794219833528,
        "updated": 1794220569040,
        "tz": null,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000tx38",
        "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000tx38&format=geojson",
        "felt": null,
        "cdi": null,
        "mmi": null,
        "alert": null,
        "status": "reviewed",
        "tsunami": 0,
        "sig": 432,
        "net": "us",
        "code": "7000tx38",
        "ids": ",us7000tx38,",
        "sources": ",us,",
        "types": ",origin,phase-data,",
        "nst": 66,
        "dmin": 4.572,
        "rms": 0.91,
        "gap": 90,
        "magType": "mb",
        "type": "earthquake",
        "title": "M 5.3 - 80 km ENE of Lagunas, Peru"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-75.0002, -4.9495, 11.49]
      },
      "id": "us7000tx38"
    }
  ],
  "bbox": [-178.7145, -58.7979, 10, 179.2119, 39.3619, 535.494]
}
```

### 2-7. `time` (밀리초) → "몇 시간 전" 계산

`metadata`의 `generated`(응답이 만들어진 시각 = 지금)와 `properties`의 `time`(발생 시각)은 둘 다 **같은 기준의 밀리초**이므로, 빼기만 하면 경과 시간이 나온다.

```python
now_ms = data["metadata"]["generated"]          # 1794281255000 (지금)
time_ms = feature["properties"]["time"]         # 1794219833528 (발생 시각)

elapsed_ms = now_ms - time_ms                   # 61421472 밀리초
hours_ago = elapsed_ms / 3600000                # 1시간 = 60분 × 60초 × 1000 = 3,600,000ms
# → 17.06... → 약 17.1시간 전

days_ago = int(hours_ago // 24)                 # → 0 (오늘 = 0일 전)
```

---

## 3. 오류 응답

| 상황 | HTTP 상태 코드 | 응답 내용 |
|---|:---:|---|
| 정상 | `200` | GeoJSON |
| 조건에 맞는 지진이 없음 | `200` | `"features": []`, `"count": 0` |
| 시작일이 종료일보다 늦음 | `200` | 오류가 아니라 **0건**으로 응답 |
| 잘못된 값 (날짜 형식, 숫자 아님 등) | `400` | **텍스트** (JSON 아님) |
| 결과가 20,000건 초과 | `400` | **텍스트** (JSON 아님) |

오류 응답 예시 (`starttime=2026-13-01`):

```
Error 400: Bad Request

Bad starttime value "2026-13-01". Valid values are ISO-8601 timestamps.

Usage details are available from https://earthquake.usgs.gov/fdsnws/event/1
...
```

오류 응답 예시 (기간을 너무 길게 잡은 경우):

```
Error 400: Bad Request

261573 matching events exceeds search limit of 20000. Modify the search to match fewer events.
...
```

> ⚠️ 오류일 때는 응답이 JSON이 아니므로 `response.json()`을 호출하면 `JSONDecodeError`가 난다.
> **`response.status_code`를 먼저 확인**하고, 200이 아니면 `response.text`로 오류 내용을 확인한다.

---

## 4. 참고: 규모(Magnitude)

| 규모 | 영향 |
|---|---|
| 2.5 미만 | 대부분 느끼지 못함 |
| 2.5 ~ 4.0 | 실내에서 느낄 수 있음 |
| 4.0 ~ 5.0 | 물건이 흔들리고 떨어짐, 가벼운 피해 |
| 5.0 ~ 6.0 | 약한 건물에 피해 |
| 6.0 ~ 7.0 | 넓은 지역에 큰 피해 가능 |
| 7.0 이상 | 대지진 |

규모가 1 커지면 지진 에너지는 약 **32배** 커진다.
