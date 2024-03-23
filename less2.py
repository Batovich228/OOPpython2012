# class Studetnt:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
# first = Studetnt()

# class Student:
#     amount_of_student = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_student += 1
#
# nick = Student ()
# kate = Student (height=170)
# print(nick.amount_of_student)
# print(Student.amount_of_student)

class Student:
    height = 160
    def __init__(self):
        print(self.height)
        self.height += 10

nick = Student()
kate = Student()