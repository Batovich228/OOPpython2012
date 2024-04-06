# try:
#     print("Hello")
#     print(10/0)
#     print("No error")
# except (NameError, ZeroDivisionError):
#     print("We have an NameError")

# # except ZeroDivisionError:
# #     print("Nuub")
# print("code after capsule")

# try:
#     try:
#         print("Hello")
#         print("error")
#         print("No error")
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)
#
# try:
#     print('Hello')
# except:
#     print("We have problems")
# else:
#     print("No problems")

# class BuildingEror(Exception):
#     def __str__(self):
#         return f"З такої кількості матеріалу будинок не збудувати!"
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "enough material"
#     else:
#         raise BuildingEror(amount_of_material)
# materials = 123
# check_material(materials, 300)

try:
    numerator = int(input("Введіть чисельник: "))
    denominator = int(input("Введіть знаменик:"))
    result = numerator / denominator
    print("Результат", result)
except ZeroDivisionError:
    print("Помилка: Ділення на нуль неможливе.")
except ValueError:
    print("Помилка: Введенні дані не є числом.")
