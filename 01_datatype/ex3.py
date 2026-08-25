# 불리언(bool)



a = True
b = False
print(a, type(a))

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)
print("apple" < "banana")
print("apple" < "apble")



#bool
#True
print(bool(4))
print(bool("abc"))
print(bool([10]) )

#False
print(bool(0))
print(bool(""))
print(bool([]))



# None 자료형
variable = None # 아직 무슨 type인지 정해지지 않았을 때 None을 씀.
print(bool(None)) # 이것도 false