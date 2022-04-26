'''
a=10; b=20
temp=a
a=b
b=temp
print(f"a={a} b={b} ")
'''
a=10; b=20; c=30
a,b,c = b,c,a
print(f"a={a} b={b} c={c}")
a=10; b=20; c=30
a,b,c = c,a,b
print(f"a={a} b={b} c={c}")