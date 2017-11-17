"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: c_装饰器.py
@time: 2017/10/17 12:43
@describe:
"""

def makeBlock(func):
    def inner():
        return "<b>" + func() + "</b>"
    return inner

def makeItalic(func):
    def inner():
        return "<i>" + func() + "</i>"
    return inner


@makeBlock
@makeItalic
def ret():
    return "Hello world"


print(ret())