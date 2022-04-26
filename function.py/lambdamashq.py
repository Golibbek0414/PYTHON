'''
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))
'''
def a(n):
 return lambda x : x * n
result = a(2)
print("Ikkilangan son 15 =", result(15))
result = a(3)
print("Uchlangan son 15 =", result(15))
result = a(4)
print("To'rtlangan 15 =", result(15))
result = a(5)
print("Beshlangan 15 =", result(15))
