"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: b_==、is.py
@time: 2017/10/9 12:54
@describe:
"""

a = [11, 22, 33]
b = [11, 22, 33]
print(a == b)
print(a is b)

c = 100
d = 100
print(c is d)

e = 100000
f = 100000
print(e is f) # 在pycharm演示不出结果
print(id(e))
print(id(f))
