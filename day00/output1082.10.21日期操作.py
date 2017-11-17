"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: output_1982.10.21.py
@time: 2017/10/15 19:10
@describe:修改当前目录下所有 output_YYYY.MM.DD.txt的文件。并将其改写为 output_YYYY-MM-DD-W.txt
"""

import os, re, calendar

dirlist = os.listdir("./")  # 列出当前目录下所有文件
regex = 'output_(\\d{4})\\.(\\d{2})\\.(\\d{2})\\.txt'  # 数小括号，第一组小括号匹配的是1982，取值的时候像第19行那样取： m.group(1)
for i in dirlist[:]:
    if not re.match(regex, i, re.M | re.I):  # 判断是不是日期格式的文件
        dirlist.remove(i)  # 不是日期格式就把该文件从列表中移除
    else:
        m = re.search(regex, i)  # 在这里再进行一次正则匹配，为了方便下一句取值。
        weekday = calendar.weekday(int(m.group(1)), int(m.group(2)),int(m.group(3))) + 1  # 数小括号，正则匹配的第一个小括号匹配的是四位数的年。也就是1982，也就是m.group(1)
        os.rename(i, "output" + m.group(1) + "-" + m.group(2) + "-" + m.group(3) + "-" + str(weekday) + ".txt")  # 重命名

print(dirlist)  # 打印所有符合条件的文件名
