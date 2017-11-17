"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: g_property.py
@time: 2017/10/10 13:06
@describe:
"""


class Test(object):
    def __init__(self):
        self.__num = 20

    def getNum(self):
        return self.__num

    def setNum(self, num):
        self.__num = num

    kkk = property(getNum, setNum)


t = Test()
print(t.kkk)  # print(t.getNum())
t.kkk = 123  # t.setNum(123)
print(t.kkk)
