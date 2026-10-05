# 사용자 정의 모듈
print("start:", __name__) # mymath.py에서 바로 실행하면 start: __main__으로 나온다.

PI = 3.14

def add(a, b):
    return a+b

if __name__ == "__main__": # 직접 실행할 때에만 실행되지만, 밖에서 호출하면 실행이 안 된다.
    print(PI)
    print(add(10, 20))