"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: b_装饰器.py
@time: 2017/10/17 12:36
@describe:
"""


def w1(func):
    def inner():
        print("正在验证。。。")
        func()

    return inner


@w1
def f1():
    print("----1----")


@w1
def f2():
    print("----2----")


f1()
f2()
