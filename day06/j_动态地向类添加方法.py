"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: j_动态地向类添加方法.py
@time: 2017/10/17 16:45
@describe:
"""
import types


class Person(object):
    pass


def fun1(self):
    print("123" + self.name)


p1 = Person()
p1.name = 'king'  # Person.name = 'king'
p1.fun = types.MethodType(fun1, p1)  # Person.fun = types.MethodType(fun1,Person)
p1.fun()
