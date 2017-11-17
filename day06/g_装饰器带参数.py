"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: g_带参数的装饰器.py
@time: 2017/10/17 14:46
@describe:
"""


def outFun(arg):
    def decrite(func):
        def inner():
            print(arg)
            print(".....log.....")
            func()

        return inner

    return decrite


@outFun("嘿嘿")
def test():
    print("test1")


test()
