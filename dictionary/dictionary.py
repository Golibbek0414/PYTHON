'''
                   #sortlash
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print("Lug'at qiymati bo'yicha o'sish tartibida : ",sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print("Lug'at kamayish tartibida valuef bo'yicha : ",sorted_d)

   # dictionaryga ma'lumot qo'shish
d = {1:10, 2:20}
print(d)
d.update({3:30})
print(d)

   # bir nechta dactionarni birlashtirish
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
     dic4.update(d)
print(dic4)

 # kvadrati bilan topish
n=int(input("son kiriting: "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)

  # dictionarlarni qo'shish
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d) 
  # 1dic 2 dic qiymatlari bilan birlashtirish
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for i in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(i))
    '''
from collections import Counter
list1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
yigindi= Counter()
for d in list1:
    yigindi[d['item']] += d['amount']
print(yigindi)     