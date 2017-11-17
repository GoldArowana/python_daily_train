"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 装饰器的执行时间.py
@time: 2017/10/17 12:56
@describe:
"""

"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: c_装饰器.py
@time: 2017/10/17 12:43
@describe:
"""


def makeBlock(func):
    print("1111111makeBlock里面的makeBlock地址：", id(makeBlock))

    def inner():
        print("22222222inner里面的inner地址：", id(inner))
        return "<b>" + func() + "</b>"

    return inner


print("333333333333makeBlock定义下面的makeBlock地址", id(makeBlock))


def makeItalic(func):
    print("444444444makeItalic里面的makeItalic地址：", id(makeItalic))

    def inner():
        print("55555555555inner里面的inner地址：", id(inner))
        return "<i>" + func() + "</i>"

    return inner


print("666666666MakeItalic定义下面的makeItalic地址", id(makeItalic))


@makeBlock
@makeItalic
def ret():
    return "Hello world"


print("7777777777声明装饰器后的ret地址", id(ret))
print(ret())
print("888888888888执行完后之后的ret地址", id(ret))
