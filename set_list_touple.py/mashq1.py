'''
print("1-masala")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
     dic4.update(d)
print(dic4)
print("2-masala")
n=int(input("n="))
dic1 = dict()
for i in range(1,n+1):
    dic1[i]=i**2
print(dic1)

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
'''
'''
Phone=['+998 33 651 31 24',
'+998 33 677 41 04',
'+998 33 566 62 04',
'+998 33 742 82 45',
'+998 62 299 67 26',
'+998 33 554 13 04',
'+998 55 909 84 80',
'+998 90 474 95 41',
'+998 90 061 55 33',
'+998 88 796 23 94',
'+998 33 571 33 62',
'+998 33 404 57 99',
'+998 33 301 37 38',
'+998 88 117 73 49',
'+998 33 211 04 23',
'+998 55 906 58 43',
'+998 55 909 42 11',
'+998 33 835 00 54',
'+998 62 299 75 40',
'+998 88 621 52 65',
'+998 88 895 68 28',
'+998 88 605 56 87',
'+998 71 982 19 12',
'+998 33 124 79 13',
'+998 88 636 74 68',
'+998 55 903 88 20',
'+998 33 297 52 01',
'+998 55 503 78 37',
'+998 33 230 79 78',
'+998 61 298 46 75',
'+998 98 094 42 10',
'+998 55 909 55 39',
'+998 98 572 22 97',
'+998 91 657 21 33',
'+998 33 946 08 67',
'+998 88 880 65 46',
'+998 55 503 26 39',
'+998 88 028 69 47',
'+998 33 081 08 97',
'+998 33 772 60 80',
'+998 88 694 22 74',
'+998 55 909 16 05',
'+998 55 906 26 75',
'+998 94 727 45 55',
'+998 55 503 73 82',
'+998 33 817 92 84',
'+998 74 988 20 94',
'+998 88 996 44 49',
'+998 33 943 90 87',
'+998 33 849 80 58']
for i in range(len(Phone)):
    if Phone[i][5]=='3' and Phone[i][6]=='3':
        print(Phone[i])
        '''
Names=[
    'Vivian Kidd',
    'Bradyn Grant',
    'Alexis Strickland',
    'Madeleine Dunn',
    'Emanuel Deleon',
    'Charlotte Moody',
    'Ian Wells',
    'Greyson Sellers',
    'Abril Cordova',
    'Julissa Wolf',
    'Gabrielle Osborne',
    'Brian Webster',
    'Ethen Charles',
    'Ashtyn Cowan',
    'Brycen Benson',
    'Thomas Sexton',
    'Brynlee Park',
    'Keaton Pena',
    'Lily Ochoa',
    'Jaycee Glass',
    'Anderson Stark',
    'Alexandria Harper',
    'Derek Cooley',
    'Savannah Coleman',
    'Chase Cantu',
    'Maverick Gonzales',
    'Wyatt Browning',
    'Brenden Walter',
    'Paula Bullock',
    'Alisha Hicks',
    'Genevieve Petty',
    'Reece Erickson',
    'Brice Pope',
    'Maverick Hammond',
    'Giuliana Morris',
    'Kaelyn Kelley',
    'Paisley French',
    'Cassius Rogers',
    'Gloria French',
    'Hugh Richardson',
    'Braiden Tate',
    'Sophia Wang',
    'Cortez Kirby',
    'Sebastian Wilkinson',
    'Joanna Shannon',
    'Miracle Barrera',
    'Cali Kaiser',
    'Bridget Leon',
    'Gillian Hall',
    'Jade King',
    'Aydin Powell',
    'Anthony Paul',
    'Brittany Rios',
    'Arely Howe',
    'Trace Valenzuela',
    'Aryanna Hicks',
    'Connor Nixon',
    'Santiago Vargas',
    'Kirsten Monroe',
    'Norah Schultz',
    'Danika Hudson',
    'Makena Escobar',
    'Jayce Navarro',
    'Thaddeus Strickland',
    'Michaela Robinson',
    'Remington Hurley',
    'Jairo Sanders',
    'Averie Huber',
    'Cody Jensen',
    'Kennedy Wall',
    'Fiona Huynh',
    'August Tapia',
    'Sarah Manning',
    'Joselyn Allison',
    'Dayton Barnes',
    'Santiago Glenn',
    'Rashad Cuevas',
    'Bernard Nicholson',
    'Will Moyer',
    'Aliza Frazier',
    'Abram Burch',
    'Lilly Klein',
    'Carlee Montes',
    'Madeleine Patton',
    'Brady Osborn',
    'Ruth Monroe',
    'Celia Horn',
    'Braylen Cabrera',
    'Jennifer Tanner',
    'Kendra Cross',
    'Olive Sherman',
    'Aiyana Wolfe',
    'Charlize Cervantes',
    'Braydon Esparza',
    'Kash Osborne',
    'Maximus Mathews',
    'Kamora Richardson',
    'Tripp Sosa',
    'Kameron Taylor',
    'Tyler Jackson']        
Fam=[]
ls = list()

for i in Names:
    a = i.split(" ")
    s = a[2]    
    ls.append(s) 
print(ls)

     



