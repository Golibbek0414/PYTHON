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
# n_list = [1, 10, [50, 70], 900, 800, [670, 750, 880], [990, 1020, 8910, 1200]]
# print("haqiqiy list:") 
# print(n_list)
# print("\ntuganlangan list:")
# print(flatten_list(n_list))


lst1 = [1,[4,[5],5],[4,5,[7,9,5],[1,5,9]],[3,5,7]]; lst2 = []
s = str(lst1)
for i in s:
    if i.isalpha():
        lst2.append(i)
    elif i.isdigit():
        lst2.append(int(i))
print(lst2)
