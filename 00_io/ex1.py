# 1. 입출력



a = input("입력: ")
print(a)
print(a, end="") # a 뒤에 줄바꿈 없음. ""사이에 있는 문자가 a 출력 뒤에 붙음.
print(type(a))
print(a, type(a))
print(a, type(a), sep=", ") # a와 type(a) 사이에 무슨 문자를 끼워넣을지 정함. 기본은 " "



# type 변환
a = int(a)
print(a, type(a))

a = int(input("입력, 정수로 변환: "))
print(a, type(a))
b = float(input("입력, 실수로 변환: "))
print(a, type(b))



# 정수 2개를 한 번에 입력받기
a = int(input())
b = int(input())
print(a, b)

a = input().split() # 입력값을 whitespace 기준으로 나눔
print(a, type(a)) # list 형태로 입력받음

# map
a = map(int, input().split()) # a에 map 객체 저장
print(a, type(a))

a, b = map(int, input().split()) # map 객체를 바로 a, b에 저장
print(a, b)

# 리스트 변환
lst = list(map(int, input().split()))