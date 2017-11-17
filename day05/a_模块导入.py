"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 模块导入.py
@time: 2017/10/9 12:40
@describe:
"""
import imp
import sys
print(sys.path, end="\n")
# 重新导入模块
imp.reload(sys)
