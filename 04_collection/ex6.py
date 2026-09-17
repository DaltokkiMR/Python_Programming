# 딕셔너리 심화

# ===========================================================
#  딕셔너리에서 제공하는 메소드
# ===========================================================

d = {"name": "뽀로로", "age": 5}

d2 = {"age": 23, "city": "일산"}

d.update(d2) # 원본 수정
print(d)
print(d.pop("city")) # value값을 return하고 삭제 (원본 수정)

d.clear() # 완전히 삭제
print(d)
print("\n\n")

# ===========================================================
#  그 외
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80, "prog": 100}

# 딕셔너리 언패킹
print(*d) # 이렇게 하면 키만 언패킹된다.
print(*d.values()) # 이렇게 하면 값만 언패킹된다.

a, *b, c = d
print(a, b, c)

print({**d}) # 이렇게 하면 키와 값 모두 언패킹된 다음 그것을 딕셔너리로 만들게 된다.
# print(**d) # 이건 안됨!

d2 = {"eng": 90, "sci": 95}
print({**d, **d2}) # d.update(d2)와 동일하게 동작하지만, update는 원본을 바꾸는 반면 언패킹으로 새 딕셔너리를 만들면 원본은 건드리지 않고 새로운 딕셔너리를 만들게 된다.

# 위 딕셔너리를 key 리스트와 value 리스트로 만들기
print(list(d))
print(list(d.values()))

# 리스트를 다시 딕셔너리로 만들기
# zip 함수로 튜플을 먼저 만들고, dict()에서 튜플의 [0]값을 key로, [1]값을 value로 넣음
subjects = list(d)
scores = list(d.values())
dt = dict(zip(subjects, scores)) # zip iterable 객체를 활용해서 딕셔너리를 채워줌.
print(dt)

# ===========================================================
#  딕셔너리 Comprehension
# ===========================================================

# 1 ~ 10의 제곱수 딕셔너리 만들기
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25 .. }
result = {x: x**2 for x in range(1, 11)}
print(result)

# 1 ~ 10 중 홀수 제곱수로 된 딕셔너리 만들기
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
result = {x: x**2 for x in range(1, 11) if x%2 == 1}

# 위 result 딕셔너리의 키를 값으로, 값을 키로 바꾸기
# {1: 1, 9: 3, 25: 5, 49: 7, 81: 9}
# result2 = dict(zip(result.values(), result))
# result2 = {k: v for k, v in zip(result.values(), result)}
result2 = {k: v for v, k in result.items()}
print(result2)

# 점수 90 이상만 필터링하기
scores = {"kor": 90, "eng": 85, "mat": 95, "sci": 89}
result = {k: v for k, v in scores.items() if v >= 90}
print(result)
print("\n\n")


# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 바구니에 있는 과일의 단어 개수 세기
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 1) Dictionary Comprehension
result = {x: words.count(x) for x in words}
print(result)

# 2) for문
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1  # 이게 어떻게 작동되는가: count 딕셔너리에 w키에 해당하는 값이 있으면 해당 값을, 없으면 0을 리턴한다. (get 메소드는 키가 없으면 None을 리턴한다.)
                                    # 이 식을 한 번 수행하면 w키에 해당하는 값이 없으면 1로 만들고, 있으면 1을 더하므로 숫자를 세는 것과 같은 효과를 얻는다.
print(count)

# 3) Counter: 요소 개수를 자동으로 세어주는 딕셔너리 서브클래스
from collections import Counter
# print(Counter(words)) # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(dict(Counter(words)))

                                    # ✅ {'apple': 3, 'banana': 2, 'cherry': 1}


# 2️⃣ 60점 이상인 경우 합격 설정하기
scores = {"국어": 85, "영어": 50, "수학": 95, "과학": 40, "사회": 72}
result = {k: "합격" for k, v in scores.items() if v >= 60}
print(result)

                                    # ✅ {'국어': '합격', '수학': '합격', '사회': '합격'}


# 3️⃣ 과목 리스트와 점수 리스트로 딕셔너리 만들기
subjects = ["국어", "영어", "수학"]
grades = [90, 80, 100]
result = dict(zip(subjects, grades))
print(result)

                                    # ✅ {'국어': 90, '영어': 80, '수학': 100}


# 4️⃣ 기존 재고에 입고 내역을 합치기 (이미 있는 상품은 합산, 새 상품은 추가)
stock = {"연필": 10, "지우개": 5, "노트": 3}        # 기존 재고
incoming = {"지우개": 4, "노트": 7, "볼펜": 12}     # 입고 내역

# 1) Dictionary Comprehension
stock.update({item: stock.get(item, 0) + qty for item, qty in incoming.items()})
# stock.update()로 원본을 수정하는 방식
# incoming 딕셔너리의 item
print(stock)

# 2) for문
for item, qty in incoming.items():
    stock[item] = stock.get(item, 0) + qty
print(stock)

                                    # ✅ {'연필': 10, '지우개': 9, '노트': 10, '볼펜': 12}