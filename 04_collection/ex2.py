# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

langs.append("go")                  # 끝에 추가
print(langs)

langs.insert(2, "c#")               # 인덱스 2에 "c#" 추가
print(langs)

langs[3] = "javascript"             # 인덱스 3을 "javascript"로 변경
print(langs)

langs.remove("c++")                 # "c++" 삭제 (첫번째 데이터만 삭제)
print(langs)

langs.pop(1)                        # 인덱스 1 삭제하고 값을 str 형식으로 반환함.
print(langs)

langs.pop()                         # 인덱스 생략 시 마지막 항목 삭제
print(langs)

print(langs.index("python"))        # "python" 인덱스 찾기

langs.reverse()                     # 리스트 순서를 거꾸로 뒤집기 | in place sort : 원본 자체를 바꾼다
print(langs)

langs.sort()                        # 오름차순 정렬 | in place sort : 원본 자체를 바꾼다
print(langs)

langs.sort(reverse=True)            # 내림차순 정렬 | in place sort : 원본 자체를 바꾼다
print(langs)

langs.clear()                       # 모든 item 삭제
print(langs)



print("\n\n")



# 리스트 복사
ori = [1, 2, 3]

result = ori.copy() # shallow copy
result.append(10)
print(ori, result) # 복사되었으므로 result를 바꿨지만 ori는 그대로임

# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]
result2 = ori.copy()
result2[0].append(10) # 원본이 같이 바뀜

print(ori, result2) # 중요! 결과값이 같다. shallow copy는 주소값을 반환하므로, result2[0]은 [1, 2]의 주소값을 의미한다. 여기에 10을 붙였으므로, [1, 2]의 주소값을 공유하는 ori와 append 모두 값이 바뀐 것이다.

# 깊은 복사를 하려면?
import copy

result3 = copy.deepcopy(ori)
result3[0].append(100) # 사본만 바뀜

print(ori, result3) # 중요! 결과값이 다르다. deep copy는 리스트 요소의 주소값까지 완전히 다른 새로운 리스트를 만들기 때문에, result3의 [1, 2]와 ori의 [1, 2]는 독립적인 주소값을 가지게 되어 서로 영향을 주지 않는다.
print("\n\n")

# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1][1][0])         # x 출력하기
print(nested_list[1][2])            # b 출력하기
print(nested_list[2])               # 2 출력하기

# 리스트 언패킹
nums = [1, 2, 3, 4]

print(*nums) # 데이터 자체를 꺼내는 것임. 리스트 형식으로 반환하지 않음.

a, b, c, d = nums # 리스트를 언패킹해서 변수에 넣음.
print(a, b, c, d)

a, *b, c = nums # 확장 언패킹, b는 항상 리스트
print(a, b, c)

nums2 = [5, 6]
print(nums + nums2)
print([*nums, *nums2]) # 이렇게 묶을 수도 있음.


# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어"]
scores = [80, 90, 95]
a, b, c = zip(subjects, scores)
print(a, b, c)

subjects = ["국어", "수학", "영어", "과학"]
scores = [80, 90, 95]
a, b, c = zip(subjects, scores)
print(a, b, c) # 개수가 안 맞으면 묶을 수 있는 것끼리만 묶는다.
# a, b, c = zip(subjects, scores, strict=True) # 짝이 안 맞으면 에러나도록 strict=True 옵션을 줄 수 있다.

for subject, score in zip(subjects, scores):
    print(f"{subject}: {score}점")

# [x] : x 자체를 원소로 넣은 리스트 생성
# list(x) : x가 iterable 객체일 경우, 차례대로 순회해서 리스트에 넣어 생성함.
print([zip(subjects, scores)])
print(list(zip(subjects, scores)))

print("\n\n")

# ===========================================================
#  List Comprehension
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
lst = []
for x in range(1,11):
    lst.append(x**2)
print(lst)

print([x**2 for x in range(1, 11)]) # List Comprehension


# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)
lst = [x**2 for x in range(1, 11) if x%2 == 0]
print(lst)

# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기
lst = ["짝" if x%2 == 0 else "홀" for x in range(1, 11)]
print(lst)

# 각 이름의 길이로 이루어진 리스트 만들기
names = ["pororo", "crong", "poby", "eddy"]
lst = [len(x) for x in names]
print(lst)

# 길이가 5 이상인 이름만 뽑기
names = ["pororo", "crong", "poby", "eddy"]
lst = [x for x in names if len(x) >= 5]
print(lst)

# 중첩 for문도 가능
# x = 1, 2, 3
# y = 0, 1, 2
# x*y 출력
lst = [x*y for x in range(1,4) for y in range(3)]
print(lst)
print("\n\n")


# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
scores = [85, 42, 73, 55, 90, 68, 35, 100]

result = [x for x in scores if x >= 60]
print(result)                       # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
result = ["합격" if x>=60 else "불합격" for x in scores]
print(result)                       # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
result = sum([n for n in range(1, 101) if n%3==0 or n%5==0])
print(result)                       # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
words = ["apple", "banana", "kiwi", "mango"]

result = [x for x in words if 'n' in x]
result = [x for x in words if x.find('n') >= 0] # index는 없으면 에러남
result = [x for x in words if x.count('n')]
print(result)                       # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
scores = [
    [92, 84, 71],       # 학생 1
    [100, 90, 80],      # 학생 2
    [80, 70, 60],       # 학생 3
]

result = [round(sum(sc)/len(sc), 2) for sc in zip(*scores)] # 언패킹해서 zip에 넣음
print(result)

result = [round(sum([scores[n][i] for n in range(3)])/3, 2) for i in range(3)]
print(result)                       # ✅ [90.0, 80.0, 70.0]

# round 함수에서 주의할 점 : 은행가 반올림
print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))