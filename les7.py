# my_list = [1,2,3]
# interator = iter(my_list)
# # print(next(interator))
# # print(next(interator))
# # print(next(interator))
# # print(next(interator))
#
# for elem in interator:
#     print(elem)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(10)
# # for elem in count:
# #     print(elem)
#
# print(count.__next__())
# print(count.__next__())
# print(next(count))
# print(next(count))
# print(next(count))

# def raise_to_the_degress(number, max_degree):
#     i=0
#     for _ in range(max_degree):
#         yield number**1
#         i+=1
# res = raise_to_the_degress(122345, 500)
# print(res)
# for _ in res:
#     print(_)
#
# def raise_to_the_degress(number):
#     Sasha =0
#     while True:
#         yield number**1
#         Sasha+=1
# res = raise_to_the_degress(122345)
# print(res)
# for _ in res:
#     print(_)

# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help you with {work} {work}"
# helper = Helper("homework")
# print(helper("cleaning"))
# print(helper("kikiki"))

import  webbrowser
def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Посилання з помилкою")
    return wrapper
@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://itstep.org/ru")
