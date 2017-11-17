"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: i_迭代器.py
@time: 2017/10/10 13:53
@describe:
"""

# 判断是否是可迭代对象
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance("adsf", Iterable))

a = [11, 22, 33]
a_iter = iter(a)
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))