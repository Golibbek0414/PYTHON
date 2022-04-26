'''
# function yig'indisi
def sum(numbers):
    s = 0
    for i in numbers:
        s+=i
    return s
print(sum((8, 2, 3, 0, 7)))

# funtion ko'paytmasi
def kopaytma(numbers):  
    s = 1
    for i in numbers:
        s *= i  
    return s  
print(kopaytma((8, 2, 3, -1, 7)))

# funtionni teskarisiga chiqarish
def stringteskari(str1):

    str2 = ''
    index = len(str1)
    while index > 0:
        str2 += str1[ index - 1 ]
        index = index - 1
    return str2
print(stringteskari('123456789'))

 # tartiblash birnechtalarni bitta qilib beradi
def list(l):
  t = []
  for i in l:
    if i not in t:
      t.append(i)
  return t

print(list([1,2,3,3,3,3,4,5])) 

# toqlari
def num(l):
    enum = []
    for n in l:
        if n % 2 != 0:
            enum.append(n)
    return enum
print(num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
'''
# ko'paytmasi
def Values():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
Values()
