"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k_闭包.py
@time: 2017/10/10 14:07
@describe:
"""


def test(number):
    print("---1----")

    def inner():
        print("-----2----")
        print(number)

    print("----3----")

    return inner


ret = test(123)
print("============分割线=========")
ret()
print("============分割线=========")
ret()