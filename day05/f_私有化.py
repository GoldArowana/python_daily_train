"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: f_私有化.py
@time: 2017/10/10 12:37
@describe:
"""


class Test(object):
    def __init__(self):
        self.__num = 100

t = Test()
# name mangling 防止意外重写
print(t._Test__num)