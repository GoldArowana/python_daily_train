"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: a.py
@time: 2017/10/1 21:56
@describe:
"""

# 输出
# print("hello world");

# 输入
# age = input("请输入您的年龄：")

# 转化为字符串型
# age = str(age)

# 转化为整形
# age = int(age)

# 格式化打印
# print("您的年龄是%d"%age);

# 字符串连接
# a = 'hello'
# b = 'word'
# print(a+b)

# 切片
# name = 'abcdef'
# print(name[1:4])
# print(name[1:-1])
# print(name[1:])

# 切片，步长
# name = 'abcdef'
# print(name[1:6:2])
# print(name[1:len(name):2])
# print(name[1::2])

# 切片，逆向遍历
# name = 'abcdef'
# print(name[3:1])  # 空
# print(name[3:1:-1])  # 逆向遍历
# print(name[-1:0:-1])
# print(name[-1::-1])
# print(name[::-1])

# 查找子串
# msg = 'hello'
# i = msg.find('ll');
# print(i)


# 文档帮助
# print(dir(str))
# help(str)
# print(str.split.__doc__)

# # 列表
# names = ['小名', '小花', '小兰', '小狗', '小汪']
# print(names)

# 列表末尾添加
# names = ['小名', '小花', '小兰', '小狗', '小汪']
# names.append('小苗')
# print(names)

# 列表插入
# names = ['小名', '小花', '小兰', '小狗', '小汪']
# names.insert(2, '小鸟')
# print(names)

# 列表合并
# names1 = ['小猫', '小狗']
# names2 = ['小驴']
# print(names1 + names2)

# 列表添加列表
# nums1 = [1, 2]
# nums2 = [2, 3, 4,]
# nums1.extend(nums2)
# print(nums1)

# 列表pop()
# nums = [1, 2, 3, 4]
# nums.pop()
# print(nums)

# 列表删除元素(删最后一个)
# nums = [1, 2, 3, 4]
# nums.pop(0)
# print(nums)

# 列表删除元素(根据内容)
# names = ['小名', '小花', '小鸟', '小哈']
# names.remove('小名')
# print(names)

# 列表删除元素(根据下标)
# names = ['小名', '小花', '小鸟', '小哈']
# del names[1]
# print(names)

# 列表中查找
# names = ['小名', '小花', '小鸟', '小哈']
# if '小鸟' in names:
#     print('ok')

# 字典
# infor = {'name': 'king'}
# print(infor)

# 字典增、改元素
# infor = {'name': 'king'}
# infor = {'name': 'jinlong'}
# infor['age'] = 28
# print(infor)

# 字典删除元素
# infor = {'name': 'king', 'age': 18}
# del infor['name']
# print(infor)

# 字典无异常获取
# infor = {'name': 'king', 'age': 29}
# print(infor.get('name'))
# print(infor.get('home'))

# while循环
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1

# for循环
# for i in (1, 4, 6):
#     print(i)

# 元组
# a, b = (11, 22)
# print(a, b)

# 利用元组遍历字典
# infor = {'name': 'king', 'age': 12, 'tall': 170}
# for key, value in infor.items():
#     print(key + " : " + str(value))

# global
# a = 'hello'
# def fun1():
#     global a
#     a = 'world'
#     print(a)
# fun1()
# print(a)

# 不定长参数
# def test(a, b, c=33, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
# test(11, 22, 33, 44, 55, task=66, done=77)

# 拆包
# def test(a, b, c=33, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
# A = (44, 55, 66)
# B = {'name': '小名', 'age': 11}
# test(11, 22, 33, *A, **B)

# 匿名函数
# infors = [{'name': 'alina', 'age': 11}, {'name': 'catalina', 'age': 21}, {'name': 'giter', 'age': 8}]
# infors.sort(key=lambda x: x['name'])
# print(infors)
# infors.sort(key=lambda x: x['age'])
# print(infors)

# 匿名函数当作实参
# def test(a,b,func):
#     result = func(a,b)
#     return result
# num = test(11,22,lambda x,y: x+y)
# print(num)

# 匿名函数+动态
# def test(a, b, func):
#     result = func(a, b)
#     return result
# strCommand = "lambda x,y:x+y"
# func_new = eval(strCommand)
# num = test(11, 22, func_new)
# print(num)

# 交换两个变量
# a = 1
# b = 2
# a, b = (b, a)  # a, b = b, a
# print(a, b)

# 列表中+=和=的区别
# a = [100]
# def test(num):
#     num = num + num
#     print(num)
# test(a)
# print(a)  # 没变
#
# b = [200]
# def test(num):
#     num += num
#     print(num)
# test(b)
# print(b)  # 变了

# 写文件
# f = open('testtest.txt', 'w')
# f.write("abcdefg")
# f.close()

# 读文件
# f = open('testtest.txt', 'r')
# context = f.read()
# print(context)

# 拷贝文件
# f = open('testtest.txt', 'r')
# context = f.read()
# f = open('testtest2.txt', 'w')
# f.write(context)

# 按量读取
# f = open('testtest.txt', 'r')
# print(f.read(1))
# print(f.read(3))
# print(f.read(2))
# print(f.read(1))

# 读取的行的长度，如果是0 则代表到文件尾。
# f = open('testtest.txt', 'r')
# print(len(f.readline()))

# 读取文件。readlines(),列表
# f = open('testtest.txt', 'r')
# list = f.readlines()
# print(list)

# 拷贝大文件
# old_file_name = 'testtest.txt'
# new_file_name = 'testtest2.txt'
# old_file = open(old_file_name, 'r')
# new_file = open(new_file_name, 'w')
# while True:
#     context = old_file.read(1024)
#     if len(context) == 0:
#         break
#     new_file.write(context)
# old_file.close()
# new_file.close()

# 获取当前读写头的位置
# f = open("testtest.txt", "r")
# str = f.read(3)
# position = f.tell()
# print(position)
# str = f.read(3)
# position = f.tell()
# print(position)
# f.close()

# 读写头重定位;第一个参数:偏移量;第二个参数-->0:相对于文件头，1:当前位置，2:文件结尾
# f = open('testtest.txt', 'r')
# f.seek(5, 0)
# print(f.read(), end='\n\n')
# f.seek(2, 0)
# print(f.read())

# 文件的重命名
# import os
# os.rename('testtest2.txt','testtest3.txt')

# 文件的删除
# import os
# os.remove('testtest3.txt')

# 创建文件jia
# import os
# os.mkdir('test2')

# 获取当前目录
# import os
# print(os.getcwd())

# 改变默认目录
# import os
# os.chdir("../")
# print(os.getcwd())

# 获取目录列表
# import os
# print(os.listdir("./"))

# 删除文件夹
# import os
# os.rmdir('test2')

# 批量重命名
# import os
# folder_name = 'test'
# file_names = os.listdir(folder_name)
# for name in file_names:
#     print(name)
#     old_file_name = folder_name+"/"+name
#     new_file_name = folder_name+"/"+"[附件]-"+name
#     os.rename(old_file_name, new_file_name)
