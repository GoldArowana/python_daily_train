"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: e_带参函数怎么使用装饰器.py
@time: 2017/10/17 13:45
@describe:
"""


def decrite(func):
    def inner(a, b):
        print("111")
        func(a, b)
        print("333")

    return inner


@decrite
def print2nums(a, b):
    print(a, b)


print2nums(555, 666)
