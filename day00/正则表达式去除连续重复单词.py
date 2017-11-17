"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 正则表达式去除连续重复单词.py
@time: 2017/10/15 18:36
@describe:正则表达式去除连续重复单词
"""

import re as regex

sentence = "this this this this is a this a ok ok cc fun fun"
print(regex.sub("((\\w+\\b) *)(\\1)+", "\\1", sentence+" "))
