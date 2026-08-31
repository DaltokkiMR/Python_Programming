# 비트 연산자
a = 5                                    # 5 = 0000 0101
b = 3                                    # 3 = 0000 0011
print(a & b)                             # 1 = 0000 0001
print(a | b)                             # 7 = 0000 0111
print(a ^ b)                             # 6 = 0000 0110
print(a << b)                            # 0000 0101 -> 0000 1010 -> 0001 0100 -> 0010 1000 = 40
print(40 >> b)                           # 5
print(~a)                                # -6 = 1111 1010



# 삼항 연산자
# int max = a > b ? a : b;
a, b = 2, 3
max = a if a > b else b
print(max)

oddeven = "짝수" if a%2 == 0 else "홀수"
print(oddeven)

score = 85
# 90점 이상이면 "A", 80점 이상이면 "B", 70점 이상이면 "C", 60점 이상이면 "D", 60점 미만이면 "F"
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(grade)