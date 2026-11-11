from datetime import datetime # 시간 변환용

import streamlit as st
from streamlit_calendar import calendar

import pandas as pd

# 커스텀 모듈
import appcalendar as ac
from bap_api import get_bap
from bap_db import init_bap_db, load_all_baps, save_bap
from pref_db import init_pref_db, load_all_prefs, save_pref

# 구현과제
from api import get_rest_api_data



# ============================== 시작 ==============================

st.set_page_config(page_title="급식 SCORE", layout="wide")

# 테이블이 없을 경우 새로 만든다.
init_bap_db()
init_pref_db()

# ============================== 급식 불러오기 사이드바 ==============================

st.sidebar.header("급식 불러오기")
month = st.sidebar.text_input("불러올 달 입력", value=datetime.now().strftime("%Y%m")) # 기본값을 현재 시간으로 정함

if st.sidebar.button("불러오기"):
    try:
        rows = get_bap(month)
        save_bap(rows)
        st.sidebar.success(f"{month}의 {len(rows)}건의 급식을 저장했습니다.")
    except Exception as e:
        st.sidebar.error(f"불러오기 실패: {e}")

# ============================== 캘린더 정의 ==============================

# 1. 급식 불러오기
baps = load_all_baps()
prefs = load_all_prefs()

# 2. pref_dict 만들기 (급식 제공 시점을 key, 점수를 value로 갖는 딕셔너리)
pref_dict = {(mlsv_ymd, meal_nm):pref for mlsv_ymd, meal_nm, pref, _ in prefs}
update_dict = {(mlsv_ymd, meal_nm):updated_at for mlsv_ymd, meal_nm, _, updated_at in prefs}

# 3. 캘린더에 표시할 이벤트 설정
calendar_events = list()
for mlsv_ymd, meal_nm, dish_nm, cal_info in baps:
    pref = pref_dict.get((mlsv_ymd, meal_nm))
    updated_at = update_dict.get((mlsv_ymd, meal_nm))
    extendedProps = {
        "mlsv_ymd": mlsv_ymd,
        "meal_nm": meal_nm,
        "dish_nm": dish_nm,
        "cal_info": cal_info,
        "pref": pref,
        "updated_at": updated_at
    }

    event = ac.make_event(mlsv_ymd, meal_nm, ac.get_mainmenu(dish_nm), pref, extendedProps)
    calendar_events.append(event)



# 추가. 캘린더 옵션 설정
calendar_options = {
    "headerToolbar": {
        "left": "today",
        "center": "title",
        "right": "prev,next"
    },
    "initialView": "dayGridMonth",
    "selectable": True,
    "editable": False # True면 이벤트를 옮길 수 있어서 막음
}



# ============================== 화면 렌더링 ==============================

st.title("🍚 밥 SCORE")
st.markdown("**급식을 직접 평가**하고 **캘린더로 보는** 급식 앱!")

# 1. 캘린더 렌더링 (key를 지정하여 상태 초기화 방지)
state = calendar(
    events=calendar_events,
    options=calendar_options,
    callbacks=["eventClick"],
    key="bap_calendar"
)


# 추가 구현과제. streamlit dataframe으로 보여주기
processed_data = [[data['id'], data['title'], data['author']['name'], data['tags'][0], data['stats']['likes']] for data in get_rest_api_data()]
id = [book[0] for book in processed_data]
title = [book[1] for book in processed_data]
author = [book[2] for book in processed_data]
tag = [book[3] for book in processed_data]
likes = [book[4] for book in processed_data]

df = pd.DataFrame({
    "ID": id,
    "TITLE": title,
    "AUTHOR": author,
    "TAG": tag,
    "LIKES": likes,
})

st.dataframe(df, hide_index=True)

# 2. 사용자가 클릭한 급식을 감지하고, 해당 급식의 상세정보를 보여주고 점수 매기기
if state.get("callback") == "eventClick": # 가장 최근 콜백이 이벤트 클릭(캘린더에서 이벤트 선택)인지 확인
    info = state["eventClick"]["event"]["extendedProps"] # 캘린더 이벤트 속 extendedProps를 가져와서 info에 넣기
    meal_key = (info["mlsv_ymd"], info["meal_nm"])
    current_pref = pref_dict.get(meal_key)
    current_updated_at = update_dict.get(meal_key)

    st.subheader(f"{info['mlsv_ymd'][0:4]}/{info['mlsv_ymd'][4:6]}/{info['mlsv_ymd'][6:]} {info['meal_nm']}")
    st.caption(f"{info['cal_info']} | 평가일: {'평가 안 함' if current_pref is None else current_updated_at}")
    st.text(info["dish_nm"])

    if current_pref is None:
        default = 50
    else:
        default = current_pref

    # key를 급식마다 다르게 해야 다른 급식을 눌렀을 때 슬라이더 값이 섞이지 않음
    score = st.slider("만족도", 0, 100, default, key=f"slider_{info['mlsv_ymd']}_{info['meal_nm']}")

    if st.button("저장"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_pref([(*meal_key, score, now)])
        st.rerun()      # 캘린더는 이미 위에서 그려졌으므로, 새 점수 색을 보여주려면 다시 실행