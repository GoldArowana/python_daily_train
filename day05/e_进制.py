"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: e_进制.py
@time: 2017/10/10 12:08
@describe:
"""
print('****18 的二进制*****')
# 18 的二进制
print(bin(18))
a = 0b10010
print(a)

print('****# 18 的八进制*****')
# 18 的八进制
print(oct(18))
b = 0o22
print(b)

print('****# 18 的十六进制*****')
# 18 的十六进制
print(hex(18))
c = 0x12
print(c)

print('****# 其他进制转为 十进制*****')
# 其他进制转为 十进制
d = int('0b10010', 2)
print(d)
