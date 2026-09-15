# 딕셔너리 기초

# ===========================================================
#  딕셔너리 (dict): 키와 값 쌍으로 저장하는 변경 가능한 자료형
#  딕셔너리의 특징
#  1. ( mutable, 변경 가능 ) - 리스트와 동일, 튜플과 반대
#  2. ( iterable, 반복 가능 )
#  3. ( not sequential, 인덱싱과 슬라이싱 불가 ) - 리스트, 튜플과 반대
#  4. ( 키는 중복 불가, 값은 중복 가능 )
# ===========================================================

# 딕셔너리 생성
a = {}
b = dict()
print(type(a), type(b))

d = {"id": 1401, "name": "고희성", "age": 17}
print(d)

# 키로 값 가져오기
print(d["name"])
# print(d["phone"]) # 없는 키 입력하면 에러 난다.

# 에러가 안나게 하려면?
if "phone" in d: # membership 연산자를 사용해서 있는지 확인한다.
    print(d["phone"])

print(d.get("phone")) # 키값이 없으면 None 출력
print(d.get("phone", "전화 없음")) # 없을 때 출력할 Default값을 지정해줄 수도 있음.
print("\n\n")

# ===========================================================
# 1. 딕셔너리는 mutable하다. (변경 가능)
# ===========================================================

d["age"] += 1
print(d)
d["phone"] = "010-1234-5678"
print(d)

del d["phone"]
print(d)
d.pop("age") # list와 마찬가지로 제거하면서 값을 반환함 | 없으면 에러남
print(d)
# d.pop() # list와 달리 순서가 없기 때문에 마지막에 들어온 값을 지우는 이러한 코드는 쓸 수 없다.
print("\n\n")

# ===========================================================
# 2. 딕셔너리는 iterable하다. (반복 가능)
# ===========================================================

# 딕셔너리 순회
for key in d: # 이렇게 하면 키만 나온다.
    print(key)

for key in d:
    print(key, d[key]) # 값은 d[key]로 꺼내면 됨.

for i, data in enumerate(d): # 주의! 여기서 i는 인덱스가 아니다. 단순히 순회하면서 꺼내오는 순서일 뿐이며, 이것이 인덱스라는 뜻은 아니다.
    print(i, data)

# 키가 아닌 값만 뽑아오기
for value in d.values():
    print(value)

# 키와 값을 동시에 뽑아오기
for key, value in d.items():
    print(value)

# 참고(몰라도 됨) : (딕셔너리).values() 또는 (딕셔너리).items()는 view 객체를 반환한다. 새로운 객체가 아니라 원본 객체를 참조하기만 한다.
a = d.items()
print(a)
d["key"] = 100
print(a) # a는 원본이 바뀌면 그걸 그대로 보여주는 view 객체이므로 이렇게 바뀔 수 있다.

print("\n\n")

# ===========================================================
# 3. 딕셔너리는 sequence 객체가 아니다. (인덱싱, 슬라이싱 불가)
# ===========================================================

d[0] = "python"
# sequence 객체이기 때문에 0번 인덱스 위치에 python이 들어가지 않는다. 
# 그 대신에'0'이라는 키값을 갖는 "python"값이 추가된다.
print(d)
print("\n\n")

# ===========================================================
# 4. 딕셔너리는 키는 중복 불가, 값은 중복 가능하다.
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

d["kor"] = 100
print(d)

d["sci"] = 80
print(d)
print("\n\n")

# 키로 가능한 것 : immutable 타입 (숫자형, 불리언, 문자열, 튜플) -> hashable type
# 키로 안되는 것 : mutable 타입 (리스트, 딕셔너리, 집합) -> unhashable type
# 키는 해시 가능(hashable) + 프로그램 실행 동안 hash값이 변하지 않아야 함

d[3.14] = 100
d[(1, 2)] = 100
d[True] = 100

# d[[1, 2]] = 100 # 안됨!
# d[{"key": 1, "key2": 2}]
print(d)

# 딕셔너리가 저장되는 방식
# 1. 딕셔너리 데이터를 저장하기 위한 해시 테이블을 생성함
# 2. hash(key) 함수를 통해 hash값을 얻음
# 3. hash값을 테이블 크기로 압축하여 버킷 인덱스를 계산하고 해시 테이블에 저장함
# 4. key값으로 조회할 때에도 hash(key)로 hash값을 얻어낸 후(동일 hash값) 해당 인덱스로 가서 조회함

# 만약 key에 mutable 타입을 허용했다면?
# 1. hash(key) 함수로 hash값을 얻어 해시 테이블에 저장함
# 2. key 내용이 변경됨
# 3. 다시 hash(바뀐key)를 하면 새로운 hash값이 나옴
# 4. 새 hash값을 이용하여 버킷 인덱스를 계산하고 해시테이블에 조회를 하면 원래 데이터를 찾을 수 없음

# 따라서, key는 해시 가능(hashable) + 프로그램 실행시 hash값이 변경되지 않아야 함
print(hash(123))
print(hash("hi"))
print(hash((1, 2)))
print(hash((1, 2))) # 동일한 값에 대한 해시값은 같음

print("\n\n")

# ===========================================================
#  파이썬 내장 함수
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

print(len(d))
# print(sum(d)) # 이건 안 된다.
print(sum(d.values())) # 이건 된다. value에 숫자만 있으므로 지금은 되지만, 문자같이 sum 불가한 객체가 들어가면 불가능하다.
print(min(d)) # 가장 작은 **key값**을 반환한다.
print(min(d.values())) # value중에서 가장 작은 값을 반환한다.
print(max(d), min(d.values()))

# sort 함수
print(sorted(d)) # key값을 오름차순 정렬한 리스트를 반환한다.
print(sorted(d.values())) # value값을 오름차순으로 정렬한 리스트를 반환한다.
print(sorted(d.items())) # key값을 오름차순 정렬하여 value값까지 함께 보여주는 리스트를 반환한다.

# sort 심화
print(dict(sorted(d.items()))) # key값 기준으로 정렬한 딕셔너리를 오름차순으로 정렬한 리스트를 다시 딕셔너리로 만들어준다.
print(dict(sorted(d.items(), reverse="True"))) # key값 기준으로 정렬한 딕셔너리를 **내림차순**으로 정렬한 리스트를 다시 딕셔너리로 만들어준다.

# value 기준 sort하여 딕셔너리 반환
def key_func(x): # key:value쌍 (튜플)을 x로 입력받음
    return x[1] # value를 반환
print(dict(sorted(d.items(), key=key_func))) # key_func함수 기준으로 오름차순 정렬한 리스트를 다시 딕셔너리로 만들어준다.
print(dict(sorted(d.items(), key=key_func, reverse=True))) # key_func함수 기준으로 **내림차순** 정렬한 리스트를 다시 딕셔너리로 만들어준다.

# 정렬 기준 설정하기
# lambda: 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda 매개변수1, 매개변수2, ... : 표현식
print(dict(sorted(d.items(), key=lambda x: x[1])))

print("\n\n")

# 딕셔너리 합치기
d2 = {"sci": 95, "prog": 100}
# print(d + d2) # 딕셔너리는 합칠 수 없다. 아마 이유는 키값이 겹치면 뭘 기준으로 업데이트해야할지 모르기 때문이지 않을까?

# 딕셔너리 반복하기
# print(d2 * 2) # 키값이 중복되기 때문에 곱할 수 없다.

# 멤버십 연산자
print("kor" in d)
print("art" in d)
print(80 in d.values())
print(100 in d.values())