a = input("a = ")
b = ''; belgilar = ''; x = 0; y = 0; h = ''
if not '(' in a:
    for i in range(len(a)):
        if a[i].isspace() and a[i-1].isdigit():
            b += belgilar
        if a[i] == '+' or a[i] == '*' or a[i] == '/' or a[i] == '-':
            belgilar = a[i]
        elif a[i].isdigit():
            b += a[i]
else:
    for i in range(len(a)):
        if a[i] == '(':
            x = i+1
        elif a[i] == ')':
            y = i
    for i in range(y+1,len(a)):
        if a[i].isdigit():
            b += a[i]
    for i in range(x-1):
        if not a[i].isspace():
            b += a[i]
    while x < y:
        if a[x].isspace() and a[x-1].isdigit():
            h += belgilar
            belgilar = ''
        if a[x] == '+' or a[x] == '*' or a[x] == '/' or a[x] == '-':
            belgilar = a[x]
        elif a[x].isdigit():
            h += a[x]
        x += 1
h = eval(h)
b += str(h)
print(eval(b))