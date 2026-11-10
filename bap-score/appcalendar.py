# app.py 내부 캘린더 관련 함수를 모은 모듈입니다.

def score_to_color(score):
    """
    점수(float, 0~100)를 입력받습니다.
    캘린더에서 표시할 해당 점수에 대한 색상을 HEX값으로 반환합니다.
    점수가 없으면(None이면) 회색을 반환합니ㅏㄷ.
    """

    if score == None:
        return "#BFBFBF"
    elif type(score) != int:
        raise ValueError("정수값을 입력하세요")
    elif not (0 <= score and score <= 100):
        raise ValueError("0 이상 100 이하의 값을 입력하세요.")
    
    color = str(hex(round(220 - 1.6*score)))[2:4].upper()
    return f"#FF{color*2}"



def make_event(mlsv_ymd, meal_nm, mainmenu, pref, extendedProps):
    """
    급식 정보와 선호도 정보를 입력받고, 캘린더 이벤트 형식으로 반환합니다.
    """
    title = f"[{meal_nm}] {mainmenu} 등"
    if pref is not None:
        title = title + f" ({pref}점)"
    
    event = {
        "title": f"[{meal_nm}] {mainmenu} 등",
        "start": f"{mlsv_ymd[0:4]}-{mlsv_ymd[4:6]}-{mlsv_ymd[6:]}",
        "color": score_to_color(pref),
        "textColor": "#222222",
        "extendedProps": extendedProps,
    }
    return event



def get_mainmenu(dish):
    """
    DB에 저장된 형식 그대로 dish를 입력받고, 가장 이름이 긴 메뉴를 대표 메뉴로 가정하여 반환합니다.
    """
    menu_list = [dish.split(" ")[0] for dish in dish.split("\n")]   # 메뉴명만 분리하여 menu_list에 저장
    menu_len = [len(menu.split("*")[0]) for menu in menu_list]      # * 뒤에는 양념 이름만 붙는다는 것을 이용, 양념 이름을 제외한 '진짜 메뉴 이름 길이'를 반환
    return menu_list[menu_len.index(max(menu_len))]                 # 이름이 가장 긴 메뉴가 대표 메뉴인 경우가 많다는 성질을 이용, 이름이 가장 긴 메뉴를 반환 (길이가 같다면 앞에 있는 것을 반환)