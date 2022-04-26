# class kitob():
#     name=input("Kitob nomini kiriting: ")
#     surname=input("Kitob muallifini kiriting: ")
#     narx=float(input("Kitob narxini kiriting: "))
#     nashiryot=input("Kitobning nashiryotini chiqaring:")
#     print()
#     print("Ma'lumotlaringiz=========================================Ma'lumotlaringiz")
#     def ism(self):
#         print(self.name,"Kitobning nomi")
#     def fam(self):
#         print(self.surname,"Kitobning muallifi")
#     def narxx(self):
#         print(self.narx,"Kitobning narxi")
#     def nashir(self):
#         for i in self.nashir:
#          if i[1]=="A" or i[1]=="B" or i[1]=="C" or i[1]=="D" or i[1]=="E" or i[1]=="F" or i[1]=="G":
#              print(self.nashir,"nashiryotida bosilib chiqqan")
# kitob=kitob()
# kitob.ism()
# kitob.fam()
# kitob.nashir()
'''
class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('14.04.2003', "G'olibbek Ashirov", 'V')
print(student.__dict__)
'''




'''
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")

 
student_data(student_id='SV12', student_name='Jean Garner')

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')
'''




'''
class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nUshbu sinflar o'rnatilgan ob'ekt sinfining pastki sinflari yoki yo'qligini tekshiring .")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 
'''


'''
class Student:
    student_name = 'Terrance Morales'
    marks = 93  
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Angel Brooks')
setattr(Student, 'marks', 95) 
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
'''
