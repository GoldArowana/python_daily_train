"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: d_继承.py
@time: 2017/10/4 11:06
@describe:
"""


class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def sleep(self):
        print('睡觉')

    def run(self):
        print('跑')


class Dog(Animal):
    def bark(self):
        print("汪汪汪---")


class Cat(Animal):
    def catch(self):
        print('抓老鼠')


