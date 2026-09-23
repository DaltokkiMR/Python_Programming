# 함수 1

# ===========================================================
# 1. 기본 함수
# ===========================================================

# C언어의 덧셈 함수
'''
int add(int a, int b)
{
    return a + b
}
'''

def add(a, b):
    """a+b의 결과를 반환한다"""
    return a+b # __add__()

# print(int.__add__(10, 20))
# print(str.__add__("Hello", "World"))

print(add(3, 4)) # 7
print(add("Hello", "Python")) # "HelloPython"
print(add([1, 2], [3, 4])) # [1, 2, 3, 4]
print(add((1, 2), (3, 4))) # (1, 2, 3, 4)

print(add.__doc__)

# ===========================================================
# 2. 튜플을 리턴하는 함수
# ===========================================================

def add_sub(a, b):
    return a+b, a-b # tuple은 소괄호 생략 가능, 하나의 튜플을 리턴하는 것.

print(add_sub(5, 3))
print(*add_sub(5, 3))

x, y = add_sub(5, 3)
print(x, y)

# ===========================================================
# 3. 디폴트 매개변수 (Default Parameter)
# ===========================================================
# 매개변수에 기본값을 지정하면, 호출 시 해당 인자를 생략할 수 있다.
# 디폴트 매개변수는 항상 일반 매개변수 뒤에 위치해야 한다.

def sub(a = 0, b = 0): # b에 디폴트 매개변수 0 설정
    return a-b

print(sub(5, 10))
print(sub(5)) # 5-0 = 5
print(sub()) # 0-0 = 0

'''
def sub2(a = 0, b): # 오류: 디폴트 매개변수는 일반 매개변수 뒤에 위치해야 한다.
    return a-b
'''
    
# ===========================================================
# 4. 키워드 인자 (Keyword Argument)
# ===========================================================
# 인자를 순서가 아니라 "매개변수명=값" 형태로 전달할 수 있다.
# 순서를 바꿔서 호출해도 이름만 맞으면 정확히 전달된다.

print(sub(5, 10)) # 순서대로 매핑
print(sub(b=10, a=5)) # 키워드 인자로 전달

def introduce(name, hometown, mbti = "ISTJ"):
    return f"저는 {name}이고, {hometown}에 살고, MBTI는 {mbti}입니다."

print(introduce("뽀로로", "일산", "ENFP"))
print(introduce(hometown="일산", mbti="ENFP", name="뽀로로"))
print(introduce(hometown="일산", name="뽀로로"))

# ===========================================================
# 5. 가변 인자 (Variable-length Argument, *args)
# ===========================================================
# 몇 개의 인자가 들어올지 모를 때 *args를 사용한다. (관례적으로 사용)
# args라는 이름으로 입력값들을 모아 튜플로 만든다.

'''
def add_all(args):
    print(args)
    return sum(args)

print(add_all(1, 2, 3)) # 이렇게 하면 인자 1개를 받는 함수에 인자를 3개 넣으므로 오류 발생
'''

def add_all(*args): # '*'을 넣어줘야 가변 인자로 받을 수 있다.
    print(args) # 튜플로 만들어줌.
    return sum(args)

print(add_all(1, 2, 3, 4, 5))

a = [1, 2, 3]
print(add_all(*a))

# ================================================================
# 6. 키워드 가변 인자 (Keyword Variable-length Argument, **kwargs)
# ================================================================
# 이름=값 형태로 몇 개가 들어올지 모를 때 **kwargs를 사용한다.
# kwargs라는 이름으로 입력값들을 모아 딕셔너리로 만든다.

def introduce2(**kwargs): # 딕셔너리를 묶어야 키워드 가변 인자로 쓸 수 있다.
    print(kwargs)
    print(f"제 이름은 {kwargs["name"]}이고, {kwargs["age"]}살이고, {kwargs["kind"]}입니다.")

introduce2(name="크롱", age=4, kind="공룡") # keyword 쓸 때는 키값에 쌍따옴표 안 붙인다. "name" 안됨!
d = {"name": "크롱", "age": 4, "kind": "공룡"}
introduce2(**d) # 딕셔너리를 완전히 언패킹해야 한다.

# ===========================================================
# 7. *args와 **kwargs를 함께 사용하는 예시
# ===========================================================

# 디미가 현재 가진 돈 구하기
# - 지난 달 남은 돈 : 500원
# - 길 가다가 주운 돈 : 100원, 200원 => 가변인자 (튜플)
# - 아빠한테 받은 돈 : 10000원
# - 엄마한테 받은 돈 : 5000원 => 키워드 가변인자 (딕셔너리)

def pocket_money(remains, *args, **kwargs):
    return remains + sum(args) + sum(kwargs.values())

print(pocket_money(500, 100, 200, mom=5000, dad=10000))
print(pocket_money(500, 100, 200, 400, mom=5000, dad=10000, uncle=3000))