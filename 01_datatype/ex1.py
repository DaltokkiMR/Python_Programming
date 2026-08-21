# 변수



# 한줄로 변수 넣기
a = 2
b = 3
print(a, b)

# a = 2, b = 4 -> 이건 안 된다!
# a = (2, b) = 4로 여긴다. 2, b를 튜플로 생각하므로, SyntaxError다.
a = 2; b = 3
a, b = 2, 3 # 이 방법을 권장한다. a, b 튜플에 2, 3 튜플을 집어넣는 구조다. (튜플 언패킹)
print(a, b)



# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a # 짧은 swap



# 변수명 규칙(C와 동일)
# 알파벳, 숫자, 특수문자 중에서는 언더스코어(_)만 가능 + 유니코드 문자도 가능하지만 비권장
# 숫자로 시작 불가
# 예약어 금지

# name! = 1 하면 오류 난다.
# 1abc = 1 하면 오류 난다.
# class = 20 하면 오류 난다. (예약어)
_age = 20
a123b = "hi"
사람 = "JHW" # 한굴 변수명 사용 가능하지만 비권장

student_name = "뽀로로" # snake case
studentName = "뽀로로" # camel case

MAX_SCORE = 100 # python은 기본적으로는 상수가 없다. 다만 대문자로 표현하면 관습적으로 상수를 의미하므로, 대문자로 쓰자. (값은 바꿀 수 있음)