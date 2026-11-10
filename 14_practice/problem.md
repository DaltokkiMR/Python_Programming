# [실습] 🌏 세계 지진 대시보드 만들기

USGS 지진 Open API로 최근 30일 동안의 전 세계 지진 데이터를 불러와서, Streamlit 웹 대시보드로 보여주는 앱을 만든다.

- API 명세(요청 파라미터, 응답 키): **[api.md](api.md)**
- 참고 코드: `11_openapi/ex1.py` (requests), `12_web/ex1.py` (streamlit), `13_openapi_project/` (모듈 나누기)

## ⚠️ 사용 가능한 라이브러리

| 파일 | import 가능 |
|---|---|
| `quake_api.py` | `requests` |
| `app.py` | `streamlit`, `quake_api` |

> `pandas`, `numpy`, `matplotlib`, `datetime` 등 **그 외 라이브러리는 사용 금지**.
> 데이터는 **리스트와 딕셔너리**로만 다루고, 시간 계산도 **숫자 계산**으로 한다.
> (`st.map()`, `st.bar_chart()`, `st.dataframe()`은 dict의 리스트를 그대로 넣어도 동작한다.)

## 학습 목표

1. 요청 파라미터를 dict로 만들어 `requests.get()`으로 Open API를 호출할 수 있다.
2. 중첩된 JSON(dict → list → dict → list)에서 원하는 키값을 꺼낼 수 있다.
3. 밀리초 단위 시각을 숫자 계산으로 "몇 시간 전"으로 바꿀 수 있다.
4. 반복문, 리스트, 딕셔너리로 데이터를 거르고 집계할 수 있다.
5. Streamlit 위젯, `st.session_state`, 지도, 차트, 표로 화면을 구성할 수 있다.

## 파일 구성

```
14_practice/
├── api.md          ← API 명세서
├── problem.md      ← 문제 (이 파일)
├── quake_api.py    ← 문제 1을 여기에 작성
├── app.py          ← 문제 2 ~ 7을 여기에 작성
└── solution/       ← 모범 답안 (다 풀고 나서 열어보기!)
    ├── quake_api.py
    └── app.py
```

## 실행 방법

```bash
cd 14_practice
python quake_api.py       # 문제 1 확인 (터미널 출력)
streamlit run app.py      # 문제 2 ~ 7 확인 (브라우저 http://localhost:8501)
```

> 이 API는 인증키가 필요 없어서 `.env` 파일을 만들 필요가 없다.

## 완성 화면 예시

```
[사이드바]                 [메인 화면]
🔎 조회 조건               🌏 세계 지진 대시보드
                           조회 조건: 전 세계 / 규모 4.5 이상
지역
[ 전 세계        ▼ ]       📅 최근 며칠               📍 위치 검색 (영문, 예: Japan, Indonesia)
                           1 ──●────────── 30         [                              ]
최소 규모                     7
2.5 ──────●──── 8.0
         4.5                 지진 횟수        최대 규모        평균 깊이
                              85건            M 6.4           100.9 km
[  지진 조회하기  ]
                           🗺️ 발생 위치
                           ( 세계 지도 위에 지진 발생 위치가 점으로 표시됨 )

                           📊 며칠 전에 발생했나
                           ( 0일 전 ~ 6일 전 막대 그래프 )

                           📋 지진 목록
                           경과(시간) | 규모 | 위치 | 깊이(km) | 위도 | 경도 | 링크
```

---

## 문제 1. API 호출 함수 만들기 — `quake_api.py`

`get_earthquakes(min_mag, region)` 함수를 완성하라. (`URL`, `REGIONS`는 미리 주어져 있다.)

**① 요청 파라미터** (api.md `1-2` 참고)

| 키 | 값 |
|---|---|
| `format` | `"geojson"` |
| `minmagnitude` | 매개변수 `min_mag` |
| `eventtype` | `"earthquake"` |
| `orderby` | `"time"` (최신순) |
| `minlatitude`, `maxlatitude`, `minlongitude`, `maxlongitude` | `REGIONS[region]`에 들어 있는 값 (`"전 세계"`는 빈 dict라 추가되는 것 없음) |

> `starttime`, `endtime`은 넣지 않는다. 생략하면 API가 **최근 30일**을 조회한다.

**② 상태 코드 확인**: `status_code`가 200이 아니면 예외를 발생시킨다. 오류 내용(`response.text`)을 메시지에 포함한다.

**③ 응답 변환**: `features`의 지진 하나하나를 아래 dict로 바꿔서, **dict의 리스트**를 반환한다.

| dict 키 | 값을 가져올 곳 (api.md `2-2`, `2-4`, `2-5`) | 가공 |
|---|---|---|
| `"경과(시간)"` | `metadata` → `generated`, `properties` → `time` | (generated - time) 밀리초 → **시간**, 소수 첫째 자리까지 |
| `"규모"` | `properties` → `mag` | 그대로 |
| `"위치"` | `properties` → `place` | 그대로 |
| `"깊이(km)"` | `geometry` → `coordinates` | 3번째 값 |
| `"위도"` | `geometry` → `coordinates` | **2번째** 값 |
| `"경도"` | `geometry` → `coordinates` | **1번째** 값 |
| `"링크"` | `properties` → `url` | 그대로 |

**④ 예외 처리**: 오류가 나면 `print()`로 출력한 뒤 `raise`로 다시 던진다. (`13_openapi_project/meal_api.py`와 같은 방식)

**실행 결과 예시** (`python quake_api.py`, 실행하는 시각에 따라 결과는 다름)

```
조회 건수: 668
{'경과(시간)': 1.4, '규모': 4.8, '위치': 'northern Mid-Atlantic Ridge', '깊이(km)': 10, '위도': 34.8774, '경도': -35.075, '링크': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000tx9n'}
{'경과(시간)': 1.5, '규모': 4.7, '위치': '90 km SSE of Tateyama, Japan', '깊이(km)': 10, '위도': 34.1962, '경도': 140.1377, '링크': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000tx9i'}
{'경과(시간)': 2.8, '규모': 4.9, '위치': '78 km ESE of Hitachi, Japan', '깊이(km)': 35, '위도': 36.3338, '경도': 141.4659, '링크': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000tx96'}
```

<details>
<summary>💡 힌트</summary>

- dict에 다른 dict의 키/값을 한꺼번에 추가하기 → `params.update(REGIONS[region])`
- 리스트를 변수 3개에 한 번에 나눠 담기 → `lon, lat, depth = feature["geometry"]["coordinates"]`
- 1시간 = 60분 × 60초 × 1000 = **3,600,000 밀리초** → `(now_ms - props["time"]) / 3600000`
- 소수 첫째 자리까지 반올림 → `round(값, 1)`

</details>

---

## 문제 2. 사이드바: 조회 조건 입력 — `app.py`

`with st.sidebar:` 블록 안에 아래 위젯을 만들고, 반환값을 변수에 저장하라. 이 값들은 **API 요청 파라미터**로 쓰인다.

| 위젯 | 라벨 | 조건 |
|---|---|---|
| `st.selectbox` | 지역 | 선택지: `REGIONS`의 키 목록 |
| `st.slider` | 최소 규모 | 2.5 ~ 8.0, 간격 0.5, 기본값 4.5 |
| `st.button` | 지진 조회하기 | `type="primary"` |

<details>
<summary>💡 힌트</summary>

- dict의 키 목록 → `list(REGIONS.keys())`
- `st.slider("최소 규모", min_value=2.5, max_value=8.0, value=4.5, step=0.5)`

</details>

---

## 문제 3. 데이터 로딩

**[지진 조회하기] 버튼을 눌렀을 때**

1. `st.spinner("지진 정보를 불러오는 중...")` 안에서 `get_earthquakes()`를 호출하고, 결과를 **`st.session_state.quakes`** 에 저장
   - 조회 조건 문자열(예: `"전 세계 / 규모 4.5 이상"`)도 `st.session_state.condition`에 저장
2. 예외가 나면 → `st.error("지진 정보를 가져오지 못했습니다.")`, 터미널에는 `print()`로 에러 메시지 출력

**버튼과 상관없이 (매번 실행)**

3. `st.session_state`에 `quakes`가 없으면 → `st.info("왼쪽 사이드바에서 조건을 고르고 [지진 조회하기] 버튼을 눌러 주세요.")` 후 `st.stop()`
4. `st.caption()`으로 조회 조건(`st.session_state.condition`)을 보여준다.
5. 조회 결과가 빈 리스트면 → `st.info("조건에 맞는 지진이 없습니다.")` 후 `st.stop()`

> ❓ **왜 `session_state`에 저장할까?**
> `st.button()`은 **누른 그 순간 한 번만** `True`이다. 문제 4의 슬라이더나 검색창을 조작하면 스크립트가 처음부터 다시 실행되는데, 이때 버튼은 `False`가 되어 조회 결과가 사라진다.
> 결과를 `st.session_state`에 저장해 두면 다시 실행돼도 값이 유지된다. (`12_web/ex1.py` 6번 참고)
>
> 💡 `st.stop()`: 이 줄에서 스크립트 실행을 멈춘다. 아래쪽 코드는 실행되지 않는다.

---

## 문제 4. 결과 필터 (API를 다시 부르지 않고 파이썬으로 거르기)

1. `st.columns(2)`로 2칸을 만들고 위젯을 하나씩 배치한다.

   | 위젯 | 라벨 | 조건 |
   |---|---|---|
   | `st.slider` | 📅 최근 며칠 | 1 ~ 30, 기본값 7 |
   | `st.text_input` | 📍 위치 검색 (영문, 예: Japan, Indonesia) | |

2. `st.session_state.quakes`에서 아래 두 조건을 **모두** 만족하는 지진만 `filtered` 리스트에 담는다.
   - `경과(시간)`이 `며칠 × 24`시간 **미만**
   - `위치`에 검색어가 **포함** (대소문자 무시: `japan`으로 검색해도 `Japan`이 나와야 함)
3. `filtered`가 비어 있으면 → `st.info("필터 조건에 맞는 지진이 없습니다.")` 후 `st.stop()`

<details>
<summary>💡 힌트</summary>

- 대소문자 무시 → 둘 다 소문자로 바꿔서 비교: `keyword.lower() in q["위치"].lower()`
- 검색어가 빈 문자열 `""`이면 `"" in "아무 문자열"`은 항상 `True` → 검색어를 안 쓰면 전부 통과한다.
- 조건에 안 맞으면 `continue`로 건너뛰고, 맞으면 `filtered.append(q)`

</details>

---

## 문제 5. 요약 지표

`st.columns(3)`으로 3칸을 만들고 `metric`으로 보여준다.

| 라벨 | 값 | 표시 예시 |
|---|---|---|
| 지진 횟수 | `filtered`의 개수 | `85건` |
| 최대 규모 | 규모의 최댓값 | `M 6.4` |
| 평균 깊이 | 깊이의 평균 (소수 첫째 자리) | `100.9 km` |

<details>
<summary>💡 힌트</summary>

- 규모만 모은 리스트 → `mags = [q["규모"] for q in filtered]`
- 내장 함수 `len()`, `max()`, `sum()` 사용, 평균 = `sum(리스트) / len(리스트)`
- `col1, col2, col3 = st.columns(3)` → `col1.metric("지진 횟수", f"{len(filtered)}건")`, 소수 첫째 자리: `f"{값:.1f}"`

</details>

---

## 문제 6. 지도

`st.subheader("🗺️ 발생 위치")` 아래에 `st.map()`으로 지진 발생 위치를 표시하라.

<details>
<summary>💡 힌트</summary>

- `st.map()`에는 dict의 리스트를 그대로 넣을 수 있다.
- `st.map()`은 기본적으로 `lat`, `latitude`, `lon`, `longitude` 같은 **영문** 이름의 키를 찾는다. 한글 키면 직접 알려줘야 한다.
  → `st.map(filtered, latitude="위도", longitude="경도")`

</details>

---

## 문제 7. 경과 일수별 차트 + 지진 목록 표

1. `st.subheader("📊 며칠 전에 발생했나")` 아래에 **며칠 전**에 발생한 지진이 몇 건인지 막대 그래프로 그린다.
   - 며칠 전 = `경과(시간) // 24` (예: 30.5시간 → 1일 전)
   - `{며칠 전: 횟수}` dict로 센 다음, 0일 전부터 `(최근 며칠 - 1)`일 전까지 **빠짐없이** 차트 데이터를 만든다. (지진이 없던 날은 0건)
2. `st.subheader("📋 지진 목록")` 아래에 `filtered` 전체를 표로 보여준다. (인덱스 숨기기)

<details>
<summary>💡 힌트</summary>

- 개수 세기 → `counts[day] = counts.get(day, 0) + 1`
- 차트 데이터 → `[{"며칠 전": 0, "횟수": 12}, {"며칠 전": 1, "횟수": 9}, ...]` 형태의 리스트
- `st.bar_chart(chart_data, x="며칠 전", y="횟수")`
- `st.dataframe(filtered, hide_index=True)`

</details>

---

## 🔥 도전 문제

| 번호 | 내용 | 사용할 기능 |
|:---:|---|---|
| A | 지도의 점을 규모가 클수록 **크게**, 규모별로 **다른 색**으로 (M5 미만 노랑 / M5 이상 주황 / M6 이상 빨강) | `st.map(..., size="키", color="키")` |
| B | 지진 목록 표에서 `경과(시간)`을 `"3.5시간 전"`처럼, `링크`를 클릭 가능한 링크로 표시 | `st.column_config.NumberColumn(format=...)`, `st.column_config.LinkColumn` |
| C | 차트 옆에 **규모 TOP 5** 표 배치 | `st.columns(2)`, `sorted(리스트, key=lambda q: q["규모"], reverse=True)` |
| D | 같은 조건으로 다시 조회하면 API를 또 부르지 않고 저장된 결과 사용 (10분) | `@st.cache_data(ttl=600)` |
| E | (자유) `REGIONS`에 지역 추가하기 / `orderby=magnitude`, `limit=5` 파라미터로 TOP 5만 따로 요청하기 등 | api.md `1-2` |

> 모범 답안(`solution/app.py`)에는 도전 A ~ D가 포함되어 있다. E는 자유 과제라 답안이 없다.

---

## ✅ 스스로 확인하기

- [ ] `quake_api.py`는 `requests`만, `app.py`는 `streamlit`과 `quake_api`만 import 한다.
- [ ] `python quake_api.py`를 실행하면 조회 건수와 지진 3건이 출력된다.
- [ ] 위도·경도가 바뀌지 않았다. (일본 지진이면 위도 30 ~ 45, 경도 130 ~ 145 근처)
- [ ] `경과(시간)`이 링크로 들어간 USGS 페이지의 발생 시각과 맞다.
- [ ] 지역을 "한국·일본 주변"으로 바꿔 조회하면 지도에 그 지역 지진만 나온다.
- [ ] 슬라이더나 검색창을 조작해도 조회 결과가 사라지지 않는다.
- [ ] 없는 지명(예: `zzz`)을 검색하면 안내 문구가 뜬다.
- [ ] 최소 규모를 8.0으로 하고 조회하면 (대부분) "조건에 맞는 지진이 없습니다."가 뜬다.
