# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

print(t.count(1))                   # 1이 몇개 있는지?

print(t.index(2))                   # 2의 첫번째 인덱스는?


# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
l = list(t)

# list -> tuple 변환
t = list(l)

# 튜플을 이용해서 swap하기
a, b = 10, 20
a, b = b, a

# 튜플 언패킹
t = (1, 2, 3, 4)
print(*t)

a, *b, c = t
print(a, b, c)

t2 = (5, 6)
print((*t, *t2))

# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
print(tuple(zip(subjects, scores)))
print("\n\n")


# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================

# Generator 표현식
gen = (x for x in range(1,11)) # List Comprehension처럼 이렇게 쓰면 Generator를 반환하는 Generator 표현식이 나온다!
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen: # 이미 앞에서 next를 했기 때문에, 4부터 출력된다.
    print(i, end=" ")
print()

# Generator는 순회가 끝나면 소진되며 끝남. 완전히 새로운 객체를 만들어야 다시 쓸 수 있다. deep/shallow copy해도 소진된 상태도 유지되기 때문에 똑같은 결과가 나온다.
for i in gen:
    print(i, end=" ")
# List Comprehension vs Generator 표현식
a = [x for x in range(1, 11)]
b = (x for x in range(1, 11))
print(a, b)
print(sum(a), sum(a))
print(sum(b), sum(b)) # b는 Generator 표현식이므로, 한 번 순회하며 sum하면 그 이후에는 소진되어 0이 난다.

# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
result = tuple((x**2 for x in range(1, 11)))
result = tuple(x**2 for x in range(1, 11)) # 튜플의 인자가 1개일 경우, () generator 소괄호를 생략할 수 있다.
print(result)

# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦



# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기
p1 = (1, 2, 3)
p2 = (10, 20, 30)
xyz = tuple(p1[i]+p2[i] for i in range(3))
xyz = tuple(a+b for a, b in zip(p1, p2))
print(xyz)
print("\n\n")


# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일","월","화","수","목","금","토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
print(f"{sum(hours[1:6])}시간")                                               # ✅ 15시간


# 2️⃣ 가장 많이 공부한 시간 출력하기
print(f"{max(hours)}시간")                                                    # ✅ 6시간


# 3️⃣ 가장 많이 공부한 요일 출력하기
print(f"{days[hours.index(max(hours))]}요일")                                 # ✅ 토요일
_, day = max(zip(hours, days))
print(f"{day}요일")

# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)

sort_list = sorted(scores)
print(f"max 점수: {sort_list[-1]}, min 점수: {sort_list[0]}")                   # ✅ max 점수: 92점, min 점수: 76점
print(f"max 점수: {max(scores)}, min 점수: {min(scores)}")                      # ✅ max 점수: 92점, min 점수: 76점


# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", 1000, 5),
    ("바나나", 2000, 3),
    ("체리", 5000, 2),
)

# 총 재고 금액 출력

total = sum(price * num for _, price, num in stocks)                          # ✅ 총액: 21,000원
print(total)
# Generator 표현식으로 표현함.

stocks = (
    ("사과", "바나나", "체리"),
    (1000, 2000, 5000),
    (5, 3, 2),
)

# 총 재고 금액 출력 v2

total = sum(price * num for _, price, num in zip(*stocks))
print(total)