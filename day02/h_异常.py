"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: h_异常.py
@time: 2017/10/4 19:22
@describe:
"""

try:
    print(num)
    print("----1----")
except NameError:
    print('nameError异常')

try:
    print(num)
    print("----1----")
except (NameError, FileNotFoundError):
    print('nameError异常')

try:
    print(num)
    print("----1----")
except Exception as msg:
    print('nameError异常:', msg)
else:
    print('没有异常时才会执行的功能')
finally:
    print('finally')
