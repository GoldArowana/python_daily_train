"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: d_浅拷贝中元组的特殊性.py
@time: 2017/10/10 11:26
@describe:
"""
# 浅拷贝在元组时，只是复制引用，不拷贝
import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = (a, b)
d = copy.copy(c)
print(id(c), id(d))
print(id(c[0]), id(d[0]))
