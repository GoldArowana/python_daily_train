"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: a_浅拷贝.py
@time: 2017/10/9 13:05
@describe:
"""
print("*****复制引用*****")
# 复制引用
a = [11, 22, 33]
b = a
print(id(a))
print(id(b))

print("*****浅拷贝*****")
# 浅拷贝
import copy

a = [11, 22, 33]
b = [44, 55, 66]
c = [a, b]
d = copy.copy(c)
print(id(c), id(d))
print(id(c[0]), id(d[0]))

print("*****深拷贝*****")
# 深拷贝
import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
b = copy.deepcopy(c)
print(id(c), id(d))
print(id(c[0]), id(d[0]))
