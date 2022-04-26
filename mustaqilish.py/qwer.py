

# def flatten_list(n_list):
#     result_list = []
#     if not n_list: return result_list
#     stack = [list(n_list)]
#     while stack:
#         c_num = stack.pop()
#         next = c_num.pop()
#         if c_num: stack.append(c_num)
#         if isinstance(next, list):
#             if next: stack.append(list(next))
#         else: result_list.append(next)
#     result_list.reverse()
#     return result_list 
# n_list = [[3,4,5],3,[4,[3,[5,[3],[4]],[4],[2]]]]
# print("haqiqiy list:") 
# print(n_list)
# print("\ntuganlangan list:")
# print(flatten_list(n_list))


# son= int(input("Son kiriting: "))
# temp= str(son)
# list1=[]
# show=[]
# for i in range(0, len(temp)):
#     h=int(temp[i])
#     list1.append(h)
# for i in range(0, len(list1)):
#     foo=0
#     for j in range(0, len(list1)):
#         if i!=j:
#             if list1[i]>list1[j]:
#                 foo=foo+list1[i]-list1[j]
#             else:
#                 foo=foo+list1[j]-list1[i]
#     show.append(foo)
# print(show)
# print(min(show))






# n=int(input("78 kiritib ko'ringchi natija qanaqa chiqarkin: "))
# a=n//10
# b=n%10
# c=b*10+a
# n1=n+c  # kiritilga 78 ni 87 qildim
# a=n1//100
# b=n1//10%10 # o'rtadagi son
# c=n1%10
# n2=c*100+b*10+a
# n2=n1+n2
# a=n2//100
# b=n2//10%10 
# c=n2%10
# n3=c*100+b*10+a
# n3=n2+n3
# a=n3//1000
# b=n3//100%10
# c=n3//10%10
# d=n3%10
# n4=d*1000+c*100+b*10+a
# n5=n3+n4
# print(f"siz kiritgan sonni palindrom qilish uchun  4 xil amal qilish kerak palindrom bo'lgan son mana {n5} ")




