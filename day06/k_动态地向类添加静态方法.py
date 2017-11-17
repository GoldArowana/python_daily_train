"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k_动态地向类添加静态方法.py
@time: 2017/10/17 17:15
@describe:
"""


class Person:
    pass


@staticmethod
def test():
    print("----static ----  test---")


# 向类添加静态方法
Person.test = test
Person.test()

if __name__ == '__main__':
    pass
