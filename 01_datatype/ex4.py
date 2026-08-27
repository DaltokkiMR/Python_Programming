# 문자열(str)
# " ", ' '



a = "python"
print(a, type(a))
a = 'python'
print(a, type(a))

# 반드시 쌍따옴표/홑따옴표 써야 하는 때
text = "I'll be back" # 홑따옴표 쓰면 끊긴다.
text = 'I\'ll be back'



# 여러줄 문자열
py = """
Life is short
You need python
"""
print(py)
# 이건 원칙적으로 주석은 아님.

# docstring (함수 맨 앞에 Multi-line string 작성)
def func():
    """
    func() 함수에 대한 설명 작성
    """ # 반드시 첫 번째 줄에 작성해야 함!
    pass
print(func.__doc__)



# 문자열 연결
print("Hello, " + "Python")

# 문자열 반복
print("Hello"*10)
print("-"*50)

# 문자열 연산시 주의사항
# print("Hello" + 3) # TypeError 발생. 같은 type끼리만 더할 수 있음.
print("Hello" + str(3))
print("10" + "2")
print(int("10") + int("2"))



# 문자열 포맷팅(f-string)
name = "Pororo"
age = 23
print(f"{name}는 {age}살입니다.")
print(f"내년 나이는 {age+1}살입니다.")
print(f"{name.upper()}처럼 함수를 쓸 수도 있죠.")
print(f"f-string에서 중괄호 자체를 출력하려면 {{ 또는 }} 사용하면 됩니다.")

pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}") # 1000 단위 ',' 찍기
print(f"{num:15d}") # 15칸 확보 후 우측정렬
print(f"{num:<15d}") # 15칸 확보 후 좌측정렬

print(f"{num:15,d}") # 15칸 확보 후 우측정렬, 1000 단위 ',' 찍기
print(f"{num:015,d}") # 15칸 확보 후 우측정렬, 남은 공간에 0으로 채우기