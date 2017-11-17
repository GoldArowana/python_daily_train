"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: a_生成器.py
@time: 2017/10/17 12:28
@describe:
"""


def w1(func):
    def inner():
        print("正在验证。。。")
        func()

    return inner


def f1():
    print("----1----")


def f2():
    print("----2----")


f1 = w1(f1)
f1()

print("************")

f2 = w1(f2)
f2()