"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: j_函数引用.py
@time: 2017/10/10 14:05
@describe:
"""


def test():
    print("******")


# 函数引用。让k指向test所指向的函数体
k = test

test()
k()
