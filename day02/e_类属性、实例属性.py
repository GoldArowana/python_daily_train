"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: e_类属性、实例属性.py
@time: 2017/10/4 13:35
@describe:
"""


class A(object):
    # 类属性
    num = 0

    # 实例方法
    def __init__(self):
        self.name = 'king'

    def write(self):
        print(self.num)
        print(self.name)

    # 类方法
    @classmethod
    def add_num(cls):
        cls.num = 100

    # 静态方法
    @staticmethod
    def printHello():
        print('hello world')


A.add_num()
print(A.num)
A.printHello()
A.num = 200
a = A()
a.write()
