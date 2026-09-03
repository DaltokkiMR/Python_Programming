# 연산자

# 산술 연산자
from curses import A_ALTCHARSET
from operator import truediv


a = 10
b = 3

print(a + b)
print(a - b)
print(a / b)                             # 2.0으로 나온다. 기본적으로 실수 연산임.
print(a % b)                             # a를 b로 나눈 나머지
print(a // b)                            # a를 b로 나눈 몫
print(a ** b)                            # a의 b제곱
print("\n\n")



# 복합 대입 연산자
a += 4
print(a)
a -= 2
print(a)
print("\n\n")



# 증감 연산자 없음
# a++ 없음!
a += 1 # 이걸 쓰자.



# 비교 연산자
print(3 == 3.0)                          # type은 비교하지 않고, 값만 비교함.
print(3 != 4)
print("apple" < "apble")                 # 사전순 배열로 비교함
print(1 < 2 < 3)                         # 연쇄 비교 : 1 < 2 and 2 < 3
print("\n\n")


# 논리 연산자 (and, or, not)
a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b and a)                      # (not b) and a로 본다.

# short-circuit 테스트
a = 10
b = 0
if a > 0 or a / b:
    print("Short-Circuit 발동!")