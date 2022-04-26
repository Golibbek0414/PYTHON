
# f = open("kom.txt","r")
# new = f.readlines()
# lst1 = []; k = 0; dict1 = {}
# for i in new:
#     x = i.split(",")
#     s = x[3].split(",")
#     lst1.append(s[-1])
# for i in lst1:
#      dict1[i] = lst1.count(i)
# print(max(dict1.values()))
# for i in dict1.keys():
#         if dict1[i]==21:
#             print(i,end=" ")
# f = open("kom.txt","r")
# new = f.readlines()
# k = 0; a= 0 
# for i in new:
#     x = i.split(",")
#     s = x[3]
#     for j in range(len(s)):
#         if s[j]=="Thai":
#             k += 1
#     if k == 4:
#         print(x[0],x[1],x[2])
#     k = 0        
# with open("kom.txt",'r') as f:
#     komp=f.readlines()
# temp=[]; max=0; til=""
# for i in komp:
#     x=i.split(",")
#     temp.append(x[3])
# for i in temp:
#     if max<temp.count(i):
#         max=temp.count(i)
#         til=i
# print("Eng kup takrorlangan til",til,max,"marta")
# temp=[];s=0
# for i in komp:
#     x=i.split(",")
#     if x[3]==til:
#         print(x[0],",",x[4])




