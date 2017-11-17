"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: w1.py
@time: 2017/11/13 10:49
@describe:
"""

# 导入所需要的模块
import urllib.request

# 调用模块中的urlopen方法，该方法返回的是一个文件
response = urllib.request.urlopen('http://pic2.sc.chinaz.com/files/pic/pic9/201710/zzpic7481.jpg')

# 使用read()方法读取文件中的内容,二进制的形式
cat_img = response.read()

# 以二进制的形式将文件写入本地
with open('D:\\猫.jpg', 'wb') as f:
    f.write(cat_img)

if __name__ == '__main__':
    pass
