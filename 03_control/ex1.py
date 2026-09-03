# 조건문 : if문, match문

# if문
age = 17
if age >= 18:
    print("성인")
else:
    print("미성년자")

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")



# match문 | C와 달리 자동 break. break를 안 써도 된다.
grade = "A"

match grade:
    case "A":
        print("우수")
    case "B":
        print("양호")
    case "C" | "D":              # grade = "C" or grade = "D"
        print("보통")
    case _:                      # C의 default와 같은 역할
        print("알 수 없음")