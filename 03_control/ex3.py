# for문

# for i in (iterable 객체 (문자열, 튜플 등))
for i in range(5):
    print(i)

a = range(5)
print(a.start, a.stop, a.step) # start는 기본값 0, step은 기본값 1
print("\n\n")

# 1 ~ 5 까지 출력
for i in range(1, 6):
    print(i)

# 0 ~ 10 중 짝수 출력
for i in range(0, 11, 2):
    print(i)

# 5 ~ 1까지 거꾸로 출력
for i in range(5, 0, -1):
    print(i)



# 1 ~ 10까지 합 출력
tot = 0
for i in range (1, 11):
    tot += i
else: # for문에서도 정상 종료되면 else 쓸 수 있다.
    print(tot)

print(sum(range(1, 11))) 
# 주의! 내장 함수명을 위에서 다른 것으로 선언하면 오류 납니다!
# 예를 들어, 파이썬 내장 함수명인 sum, len과 같은 이름을 변수로 선언해 버리면, 내장 함수를 선언한 변수가 덮어씌우면서 기존 내장 함수가 사라집니다.



# 한글이나 한자, 이모지와 같은 유니코드를 str 타입으로 넣을 수 있다.
s = "안녕하세요, hello, 你好, こんにちは, 😀"
for c in s:
    print(c, end=" ")
print()
print(len(s)) # 유니코드 기준 글자 개수임



# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {(i*j):2d}", end="    ")
    print()
else:
    print("END")