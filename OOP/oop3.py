
# yillar topish
class year:
    def yillar(self, num):
        yil = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        for (n, rimraqam) in yil:   
            (d, num) = divmod(num, n)
            res += rimraqam * d
        return res
print(year().yillar(1))
print(year().yillar(500))
print(year().yillar(755))
print(year().yillar(1200))
print(year().yillar(3456))


'''
# yilni topish
class yil:
    def roman_to_int(self, s):
        year = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        k = 0
        for i in range(len(s)):
            if i > 0 and year[s[i]] > year[s[i - 1]]:
                k += year[s[i]] - 2 * year[s[i - 1]]
            else:
                k += year[s[i]]
        return k

print(yil().roman_to_int('MMMCMLXXXVI'))
print(yil().roman_to_int('MMMM'))
print(yil().roman_to_int('C'))
'''




'''
# ayirmasi nol chiqadiganlar
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
'''


'''
class yigindi:
  def sum(self, nums, number):
       lookup = {}
       for i, num in enumerate(nums):
           if number - num in lookup:
               return (lookup[number - num], i )
           lookup[num] = i
print("index1=%d, index2=%d" % yigindi().sum((10,20,10,40,50,60,70),60))
'''

# class Rectangle():
#     def __init__(self, l, w):
#         self.length = l
#         self.width  = w

#     def rectangle_area(self):
#         return self.length*self.width

# newRectangle = Rectangle(12, 11)
# print(newRectangle.rectangle_area())


# class IOString():
#     def __init__(self):
#         self.str1 = ""

#     def get_String(self):
#         self.str1 = input()

#     def print_String(self):
#         print(self.str1.upper())

# str1 = IOString()
# str1.get_String()
# str1.print_String()



class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('salom dunyo '))

