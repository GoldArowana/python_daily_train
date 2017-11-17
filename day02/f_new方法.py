"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: f_new方法.py
@time: 2017/10/4 14:40
@describe:
"""


class A(object):
    def __new__(cls):
        print('__new__方法')
        return object.__new__(cls)

    def __init__(self):
        print('__init__方法')


A()
