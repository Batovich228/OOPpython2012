# try:
#     print("Hello")
#     print(10/0)
#     print("No error")
# except (NameError, ZeroDivisionError):
#     print("We have an NameError")

# # except ZeroDivisionError:
# #     print("Nuub")
# print("code after capsule")

try:
    try:
        print("Hello")
        print("error")
        print("No error")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)

try:
    print('Hello')
except:
    print("We have problems")
else:
    print("No problems")