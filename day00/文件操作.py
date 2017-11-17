"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 文件操作.py
@time: 2017/11/13 22:42
@describe:
"""

# -*- coding: UTF-8 -*-

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print(child)  # .decode('gbk')是解决中文显示乱码问题


# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    for eachLine in fopen:
        print
        "读取到得内容如下：", eachLine
    fopen.close()


# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
    fopen = open(filename, 'w')
    print("请任意输入多行文字", " ( 输入 .号回车保存)")
    while True:
        aLine = input()
        if aLine != ".":
            fopen.write('%s%s' % (aLine, os.linesep))
        else:
            print("文件已保存!")

            break
    fopen.close()


if __name__ == '__main__':
    filePath = "D:\\FileDemo\\Java\\myJava.txt"
    filePathI = "D:\\FileDemo\\Python\\pt.py"
    filePathC = "D:\\"
    eachFile(filePathC)
    # readFile(filePath)
    # writeFile(filePathI)
