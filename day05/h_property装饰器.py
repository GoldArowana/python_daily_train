"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: h_property装饰器.py
@time: 2017/10/10 13:38
@describe:
"""


class Test:
    def __init__(self):
        self.num = 100

    @property
    def kkk(self):
        print('这里是getter')
        return self.num

    @kkk.setter
    def kkk(self, num):
        print('这里是setter')
        self.num = num


t = Test()
t.kkk = 111
print(t.kkk)
