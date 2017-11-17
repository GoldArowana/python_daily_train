"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: g_单例.py
@time: 2017/10/4 14:40
@describe:
"""


class Dog(object):
    __instance = None

    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        self.name = name


a = Dog('旺财')
print(id(a))
print(a.name)

print("*" * 30)

b = Dog('哮天犬')
print(id(b))
print(b.name)
