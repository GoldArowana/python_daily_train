"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: c_del方法.py
@time: 2017/10/4 10:48
@describe:
"""
import sys


class Cat:
    def __del__(self):
        print("cat对象释放")


cat1 = Cat()
print('引用计数(比实际值多1)：', sys.getrefcount(cat1))
cat2 = cat1
print('引用计数(比实际值多1)：', sys.getrefcount(cat1))
cat3 = cat1
print('引用计数(比实际值多1)：', sys.getrefcount(cat1))

del cat1
del cat2
del cat3  # 当所有连接都del后对象自动释放
print("*******************")
