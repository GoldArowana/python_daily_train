"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: a_给类添加属性.py
@time: 2017/10/4 0:00
@describe:
"""


class Cat:
    def __str__(self):
        pass
    def eat(self):
        print("吃鱼")



tom = Cat()
tom.name = '汤姆'
print(tom.name)
