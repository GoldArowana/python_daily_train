"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 列表生成式.py
@time: 2017/10/5 14:15
@describe:
"""

a = [i for i in range(1, 18)]
print(a)

a = [11 for i in range(1, 18)]
print(a)

a = [i for i in range(1, 18) if i % 2 == 0]
print(a)

a = [(i, j) for i in range(3) for j in range(5)]
print(a)
