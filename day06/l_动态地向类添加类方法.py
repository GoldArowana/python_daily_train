"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: l_动态地向类添加类方法.py
@time: 2017/10/17 17:22
@describe:
"""


class Person:
    pass


@classmethod
def func(cls):
    print("test --- class method---")


Person.func = func

Person.func()
if __name__ == '__main__':
    pass
