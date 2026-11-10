# [모범 답안] Open API + Web 연동 실습: 세계 지진 대시보드
# 실행) streamlit run app.py

import streamlit as st

from quake_api import REGIONS, get_earthquakes

st.set_page_config(page_title="세계 지진 대시보드", page_icon="🌏", layout="wide")
st.title("🌏 세계 지진 대시보드")
st.caption("데이터 출처: USGS Earthquake Hazards Program (https://earthquake.usgs.gov) · 최근 30일")


# [도전 D] 같은 조건으로 다시 조회하면 API를 부르지 않고 10분간 캐시된 결과 사용
@st.cache_data(ttl=600, show_spinner=False)
def load_quakes(min_mag, region):
    return get_earthquakes(min_mag, region)


# [도전 A] 규모에 따라 지도에 찍을 점의 색상 정하기
def mag_color(mag):
    if mag >= 6:
        return "#e03131"    # 빨강
    if mag >= 5:
        return "#f08c00"    # 주황
    return "#fab005"        # 노랑


# ===========================================================
#  문제 2. 사이드바: 조회 조건 입력 (= API 요청 파라미터)
# ===========================================================

with st.sidebar:
    st.header("🔎 조회 조건")
    region = st.selectbox("지역", list(REGIONS.keys()))
    min_mag = st.slider("최소 규모", min_value=2.5, max_value=8.0, value=4.5, step=0.5)
    clicked = st.button("지진 조회하기", type="primary", width="stretch")


# ===========================================================
#  문제 3. 데이터 로딩 (버튼 클릭 → API 호출 → session_state 저장)
# ===========================================================

if clicked:
    try:
        with st.spinner("지진 정보를 불러오는 중..."):
            st.session_state.quakes = load_quakes(min_mag, region)
            st.session_state.condition = f"{region} / 규모 {min_mag} 이상"
    except Exception as e:
        st.error("지진 정보를 가져오지 못했습니다.")
        print(f"에러 메시지: {e}")

if "quakes" not in st.session_state:
    st.info("왼쪽 사이드바에서 조건을 고르고 [지진 조회하기] 버튼을 눌러 주세요.")
    st.stop()

quakes = st.session_state.quakes
st.caption(f"조회 조건: {st.session_state.condition}")

if not quakes:
    st.info("조건에 맞는 지진이 없습니다.")
    st.stop()


# ===========================================================
#  문제 4. 결과 필터 (API를 다시 부르지 않고 파이썬으로 거르기)
# ===========================================================

col_days, col_keyword = st.columns(2)
days = col_days.slider("📅 최근 며칠", min_value=1, max_value=30, value=7)
keyword = col_keyword.text_input("📍 위치 검색 (영문, 예: Japan, Indonesia)")

filtered = []
for q in quakes:
    if q["경과(시간)"] >= days * 24:
        continue
    if keyword.lower() not in q["위치"].lower():
        continue
    filtered.append(q)

if not filtered:
    st.info("필터 조건에 맞는 지진이 없습니다.")
    st.stop()


# ===========================================================
#  문제 5. 요약 지표
# ===========================================================

mags = [q["규모"] for q in filtered]
depths = [q["깊이(km)"] for q in filtered]

col1, col2, col3 = st.columns(3)
col1.metric("지진 횟수", f"{len(filtered)}건")
col2.metric("최대 규모", f"M {max(mags):.1f}")
col3.metric("평균 깊이", f"{sum(depths) / len(depths):.1f} km")


# ===========================================================
#  문제 6. 지도
#  - 기본: st.map(filtered, latitude="위도", longitude="경도")
#  - [도전 A] 규모가 클수록 크고 붉은 점
# ===========================================================

st.subheader("🗺️ 발생 위치")

map_data = []
for q in filtered:
    map_data.append({
        "위도": q["위도"],
        "경도": q["경도"],
        "크기": q["규모"] ** 2 * 4000,     # 점 반지름(m): M4.5 → 약 81km, M7 → 약 196km
        "색상": mag_color(q["규모"]),
    })
st.map(map_data, latitude="위도", longitude="경도", size="크기", color="색상")
st.caption("🟡 M5 미만 · 🟠 M5 이상 · 🔴 M6 이상")


# ===========================================================
#  문제 7. 경과 일수별 차트 + 지진 목록 표
# ===========================================================

left, right = st.columns(2)

with left:
    st.subheader("📊 며칠 전에 발생했나")

    # {며칠 전: 횟수} 세기 (예: 경과 30.5시간 → 1일 전)
    counts = {}
    for q in filtered:
        day = int(q["경과(시간)"] // 24)
        counts[day] = counts.get(day, 0) + 1

    chart_data = []
    for day in range(days):
        chart_data.append({"며칠 전": day, "횟수": counts.get(day, 0)})
    st.bar_chart(chart_data, x="며칠 전", y="횟수")

with right:
    # [도전 C] 규모 TOP 5
    st.subheader("🏆 규모 TOP 5")
    top5 = sorted(filtered, key=lambda q: q["규모"], reverse=True)[:5]
    st.dataframe(top5, hide_index=True, column_order=["규모", "위치", "경과(시간)"])

st.subheader("📋 지진 목록")
st.dataframe(
    filtered,
    hide_index=True,
    # [도전 B] 경과 시간을 "OO시간 전"으로, 링크 열을 클릭 가능한 링크로 표시
    column_config={
        "경과(시간)": st.column_config.NumberColumn("발생", format="%.1f시간 전"),
        "링크": st.column_config.LinkColumn("상세 정보", display_text="USGS에서 보기"),
    },
)
