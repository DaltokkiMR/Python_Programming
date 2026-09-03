# 반복문 : while문, for문



# while문
# 1 ~ 10까지 반복 출력하기
i = 0
while i < 10:
    i += 1
    print(i)
else:
    print("End")                             # while문의 조건식이 False가 되면서 while문을 빠져나오면 else 구문이 실행된다.
print("\n\n")

i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5: break                         # i = 5이면 while문 빠져나오기
else:
    print("End")                             # while문의 조건식이 False여서 빠져나온 것이 아니라 break때문에 빠져나왔기 때문에 실행 안 됨.
print("\n\n")

# 리스트에 target값 찾기
nums = [1, 3, 5, 7, 9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print(f"목표값 {target}이(가)) {i}번 인덱스에 존재합니다.")
        break
    i += 1
else:
    print(f"목표값 {target}이(가) 없습니다.")
print("\n\n")

# 1 ~ 10까지의 합
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(tot)

i = 1
tot = 0
while i <= 10:
    if i%2 == 0: continue
    i += 1
print(tot)