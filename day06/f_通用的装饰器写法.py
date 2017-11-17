"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: f_通用的装饰器写法.py
@time: 2017/10/17 14:31
@describe:
"""


def decrite(parameterFunciton):
    def inner(*args, **kwargs):
        print("。。。innenr。。。")
        ret = parameterFunciton(*args, **kwargs)
        return ret

    return inner


@decrite
def fun1():
    print("---111---")
    return "xxxxxxxxx"


@decrite
def fun2():
    print("---222---")


@decrite
def fun3(a):
    print("---333---", a)


a = fun1()
print("(((%s)))"%a)

b = fun2()
print("(((%s)))"%b)

c = fun3(123456)
print("(((%s)))"%c)
