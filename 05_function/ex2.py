# 함수 2

# ===========================================================
# 1. 지역변수와 전역변수
# ===========================================================
# 함수 안에서 만든 변수는 지역변수로, 함수 밖에서는 사용할 수 없다.
# 함수 밖에서 선언된 변수는 전역변수이며, 함수 안에서는 기본적으로
# "읽기"만 가능하고, 값을 바꾸려면 global 키워드가 필요하다.

a = 1 # 전역변수

def func():
    print(f"함수 안: {a}")

func()
print(f"함수 밖: {a}")



def func2():
    a = 10 # 지역변수
    print(f"함수 안: {a}")

func2()
print(f"함수 밖: {a}")



def func3():
    global a
    a = 10 # 전역변수
    print(f"함수 안: {a}")

func3()
print(f"함수 밖: {a}")

print("\n\n")

# ===========================================================
#  2. 함수 인자 전달 방식
# ===========================================================
# <C언어에서의 표현>
# 1) call-by-value: 값 자체가 복사되어 전달, 원본과 별도의 메모리 공간을 할당, 함수 내부에서 수정 시 원본 불변
# 2) call-by-reference: 변수의 주소가 전달, 원본과 같은 메모리 공간을 가리킴, 함수 내부에서 수정 시 원본 변경
# 3) call-by-assignment: 파이썬은 객체를 가리키는 참조 전달, 원본과 같은 객체를 가리킴(재할당 전까지)
#                        immutable 객체인 경우 call-by-value처럼 동작 -> 함수 내부에서 수정 시 원본 불변
#                        mutable 객체인 경우 call-by-reference처럼 동작 -> 함수 내부에서 수정 시 원본 변경
#                        mutable 객체라도 재할당을 하면 원본과 연결이 끊기고 새로운 객체 할당

# 객체 참조값을 전달하고, 지역변수를 만듦
def swap(a, b):
    print(id(a), id(b)) # 전역변수 a, b와 동일한 객체
    a,b = b,a
    print(id(a), id(b)) # 이제는 지역변수 a, b를 새로 만들면서 id값이 바뀜.
    print(a, b)

a, b = 1, 2
print(id(a), id(b))
swap(a, b) # 2, 1 | a, b 객체의 참조값을 전달함.
print(a, b) # 1, 2

print("\n")



# 객체 참조값을 전달하고, 그것을 수정
def append_item(num): # num 매개변수가 객체 참조값(id) 복사
    print(id(num))
    num.append(2)

num = [1]
print(id(num))
append_item(num)
print(num)

print("\n")



# 객체 참조값을 전달하고, 참조값 자체를 사용하여 리스트를 직접 수정
def swap2(num):
    num[0], num[1] = num[1], num[0]

num = [1, 2]
swap2(num)
print(num)

print("\n")



# 객체 참조값을 전달하고, 새로운 지역변수 리스트를 만들어서 반환
def assign(num):
    num = [10]
    print(num)

num = [1, 2]
assign(num)
print(num)

print("\n\n")
# ===========================================================
# 3. 재귀함수
# ===========================================================

# 팩토리얼 계산하기 (1, 1, 2, 6, 24, ..)
# 점화식: f(n): 1 if n < 1 else n * f(n-1)
def factorial(n):
    return 1 if n<1 else n * factorial(n-1)

print(factorial(5))

# 피보나치 계산하기 (0, 1, 1, 2, 3, 5, 8, ..)
# 점화식: f(n): f if n <= 1 else f(n-2)+f(n-1)
def fibo(n):
    return n if n<=1 else fibo(n-2) + fibo(n-1)

print(fibo(5))

def fibo_list(n):
    lst = list()
    for i in range(n):
        if i <= 1: lst.append(i)
        else: lst.append(lst[i-2]+lst[i-1])
    return lst

print(fibo_list(8))
print([fibo(i) for i in range(10)])

print("\n\n")

# ===========================================================
# 4. 람다함수
# ===========================================================

# 람다함수 : 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda a, b, ...: 표현식
lambda a, b: a + b

add = lambda a, b: a + b # 이렇게 하면 def로 만든 함수마냥 add 쓸 수 있음
print(add(2, 3))


students = [
    {"name": "뽀로로", "score": 85},
    {"name": "크롱", "score": 92},
    {"name": "포비", "score": 78},
]
# print(sorted(students)) # 딕셔너리끼리 깡으로 비교할 수가 없음.
print(sorted(students, key=lambda s: s["name"])) # 정렬 기준을 name으로 한 것.
print(sorted(students, key=lambda s: s["score"])) # 정렬 기준을 score로 한 것.

print("\n\n")

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ n이 짝수면 True, 홀수면 False를 반환하는 함수 작성하기

is_even = lambda n: n%2==0

print(is_even(4))                           # ✅ True
print(is_even(7))                           # ✅ False


# 2️⃣ 가변 인자로 여러 숫자를 받아 (최소값, 최대값, 합계, 평균) 튜플 리턴하기

def num_info(*args):
    return min(args), max(args), sum(args), sum(args)/len(args)

print(num_info(4, 8, 1, 9, 3))              # ✅ (1, 9, 25, 5.0)


# 3️⃣ 이름과 키워드 가변 인자로 받은 정보로 아래와 같이 문자열을 만들어 리턴하기

def introduce(name, **kwargs):
    lst = [name] + [f"{k}: {v}" for k, v in kwargs.items()]
    return " / ".join(lst)


print(introduce("카리나", age=26, team="에스파", hometown="수원"))
# ✅ 카리나 / age: 26 / team: 에스파 / hometown: 수원

print(introduce("장원영", age=22, team="아이브", bloodtype="O형"))
# ✅ 장원영 / age: 22 / team: 아이브 / bloodtype: O형

print(introduce("성현", age=17, team="코르티스"))
# ✅ 성현 / age: 17 / team: 코르티스


# 4️⃣ 5부터 카운트다운하여 로켓 발사시키기 (재귀함수)
# time.sleep(1)                     # 1초 동안 stop

import time

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("로켓 발사")

countdown(5)                        # ✅ 5 -> 4 -> 3 -> 2 -> 1 -> 로켓 발사