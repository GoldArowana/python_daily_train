"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: i_动态添加属性和方法.py
@time: 2017/10/17 15:22
@describe:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("king", 21)
print(p1.age)
# 动态地给实例添加属性
p1.addr = "北京"
print(p1.addr)

# 动态地给类添加属性
Person.do = "吃饭"
print(p1.do)
print(Person.do)

if __name__ == '__main__':
    pass
