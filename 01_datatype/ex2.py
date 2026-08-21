# 파이썬 자료형
# 1. 기본 자료형: 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합



# 숫자형 - 정수형 (int)
a = 10
print(a, type(a))

# int 데이터의 표현 범위
x = 10 ** 100 # x에 googol을 입력
print(x) # 그대로 출력

# 오버플로우 테스트
a = 2 ** 31 - 1 # C언어에서의 int type의 최대값
a = a + 1
print(a) # C언어에서의 int type은 오버플로우가 안 생긴다!

# 2진수, 8진수, 16진수
a = 31
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65)) # A의 아스키코드, 아스키코드 65에 해당하는 문자



# 숫자형 - 실수형(float)
b = 3.1415
print(b, type(b))

# float의 표현 범위
# 부동소수점 방식으로 저장
# 예를 들어 64Bit이면 (부호부 1Bit) + (지수부 11Bit) + (기수부 52Bit)
import sys
print(sys.float_info.min, sys.float_info.max) # 양수 범위의 최소/최대
print(-sys.float_info.min, -sys.float_info.max) # 음수 범위의 최대/최소

a = 1.7e308
b = 1.8e308 # python의 float 자료형의 최대값은 약 1.79e308이다.
c = 2e308 # 지수 표현은 float 타입으로 간주
print(a, b, c)

# 부동소수점 표현의 부정확성
print(0.1 + 0.2 == 0.3) # 부동 소수점 연산의 측징상 0.1이 정확히 0.1이 아니므로 false가 나온다.
print(f"{0.1:.20f}") # 완전히 0.1이 아닌 것을 확인할 수 있다.
print(0.1) # 이렇게 쓰면 가장 간결한 실수값으로 표시하므로 0.1이 나온다.



# 형변환
print(float(10)) # float형으로 바꾼다.
print(int(3.14)) # 소수점 버림
print(int(3.84)) # 소수점 버림