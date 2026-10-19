# 예외 처리 (Exception Handling)

# ===========================================================
#  1. 예외 처리란?
#  - ( 예외 ): 프로그램 실행 중에 발생하는 오류 (오류: 코드에서의 잘못도 오류, 시스템적인 잘못, 예를 들어 메모리 부족이나 리소스 부족 등으로 인한 문제도 오류임. 예외는 오류의 부분집합임.)
#  - ( 예외 처리 ): 오류가 발생해도 프로그램이 비정상 종료되지 않도록 미리 대비하여 처리하는 것
#
#  [오류의 종류]
#  - 문법 오류(SyntaxError): 코드 작성 규칙을 어겨서 실행 전에 발생
#  - 예외(Exception): 문법은 맞지만 실행 중에 발생 (예: 0으로 나누기)
#
#  [자주 만나는 예외]
#  - ZeroDivisionError: 0으로 나눌 때
#  - IndexError: 리스트의 범위를 벗어난 인덱스에 접근할 때
#  - ValueError: 값의 형식이 맞지 않을 때 (예: int("abc"))
#  - KeyError: 딕셔너리에 없는 키로 접근할 때
#  - TypeError: 자료형이 맞지 않는 연산을 할 때 (예: 1 + "a")
# ===========================================================

# 아래 코드 예상 결과는?
# print(10 / 0)                         # ( ZeroDivisionError )
# print([1, 2, 3][10])                  # ( IndexError )
# print(int("abc"))                     # ( VlaueError )
# d = {"a": 1}
# print(d["b"])                         # ( KeyError )
# print(1 + "2")                        # ( TypeError )

# -> 프로그램이 종료되지 않게 하려면 예상되는 오류는 처리하기


# ===========================================================
#  2. try-except 기본 문법
#  - 형식) try:
#              예외가 발생할 수 있는 코드
#          except:
#              예외가 발생했을 때 실행할 코드
#  - ( try ) 블록에서 예외가 발생하면 나머지 코드는 건너뛰고
#    ( except ) 블록으로 이동한다.
#  - 예외가 발생하지 않으면 except 블록은 실행되지 않는다.
# ===========================================================

# try:
#     num = int(input("숫자 => "))        # 예외 발생 가능한 코드
#     print(num)
# except:
#     print("숫자를 입력하지 않았습니다. 숫자를 입력하세요.")

# print("프로그램 계속 진행")
# 오류가 발생하면 무조건 except 통으로 받는다.

# try:
#     num = int(input("숫자 => "))        # 예외 발생 가능한 코드
#     print(10 / num)
# except:
#     print("숫자를 입력하지 않았습니다. 숫자를 입력하세요.")

# print("프로그램 계속 진행")
# 그런데, 이렇게 코드를 만들면 '0'을 '숫자를 입력하지 않은 것'으로 파악하게 된다.


# ===========================================================
#  3. 예외 종류별로 처리하기
#  - 형식) try:
#              ...
#          except 예외종류1:
#              ...
#          except 예외종류2:
#              ...
#          else:
#              예외가 없을 때만 실행
#          finally:
#              예외 발생 여부와 관계없이 항상 실행
#
#  - 구체적으로 예외를 지정하는 것을 권장
#  - 에러 메시지 확인하기: except 예외종류 as 변수명
# ===========================================================

try:
    num = int(input("숫자 => "))        # 예외 발생 가능한 코드
    result = 10 / num
except ValueError as e:
    print("숫자를 입력하세요.")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print(e)
else:
    print("결과:", result)
finally:
    print("예외가 생기든 아니든 이건 실행됩니다.")

print("\n\n")


# ===========================================================
#  4. 예외 직접 발생시키기
#  - 형식) raise 예외종류("에러 메시지")
#  - 프로그램에서 개발자가 직접 예외를 발생시킬 수 있다.
#  - raise로 발생시킨 예외도 try-except로 처리할 수 있다.
# ===========================================================

# 이건 함수에서 예외를 발생시키고 호출한 곳에서 예외처리를 하도록 되어 있다.
# 함수에서 예외처리까지 하려면 함수 안에 try-except 구문으로 예외처리해줘도 된다.
def check_age(age):
    if age < 0:
        raise ValueError("나이는 음수일 수 없습니다.")
    print("나이 출력:", age)

try:
    check_age(-10)
except ValueError as e:
    print(e)

print("\n")

def check_age(age):
    try:
        if age < 0:
            raise ValueError("나이는 음수일 수 없습니다.")
        print("나이 출력:", age)
    except ValueError as e:
        print("함수 내부 출력 오류 문구:", e)
        raise # 이건 함수 내에서 예외처리를 한 다음 호출한 곳까지 오류를 넘겨주는 코드. raise만 써도 except 구분의 ValueError와 오류 문구까지 전달된다.

try:
    check_age(-10)
except ValueError as e:
    print(e)

print("\n\n")

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 사칙연산 계산기 만들기
#  - 피연산자가 숫자가 아닌 경우: "숫자를 입력하세요." 예외 발생
#  - 0으로 나눌 경우: "0으로 나눌 수 없습니다." 예외 발생
#  - 그 외 연산자의 경우: "지원하지 않는 연산자입니다." 예외 발생

def calc(a, op, b):
    try:
        a, b = int(a), int(b)
    except ValueError:
        raise ValueError("숫자를 입력하세요.")
              
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return a/b
    else:
        raise ValueError(f"존재하지 않는 연산자 '{op}' (+, -, *, /만 사용 가능)")



# 2️⃣ 계산기 함수 호출 시 예외 처리하기
# [실행 결과]
#  - 15
#  - 에러: 0으로 나눌 수 없습니다.
#  - 에러: 지원하지 않는 연산자(%)입니다.
#  - 에러: 숫자를 입력하세요.

for data in [("10", "+", "5"), ("10", "/", "0"), ("10", "%", "3"), ("ten", "+", "3")]:
    try:
        print(calc(*data))
    except ValueError as e:
        print("오류:", e)
    except ZeroDivisionError as e:
        print("오류:", e)

# 이건 오류가 하나라도 발생하면 바로 중지하고 뒤 작업도 정지. for data in ... 구문을 하나의 프로세스로 보는 것.
try:
    for data in [("10", "+", "5"), ("10", "/", "0"), ("10", "%", "3"), ("ten", "+", "3")]:
        print(calc(*data))
except (ValueError, ZeroDivisionError) as e:
    print("오류:", e)