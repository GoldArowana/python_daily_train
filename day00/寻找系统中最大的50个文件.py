"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 递归遍历子文件夹.py
@time: 2017/11/13 22:46
@describe:
"""

import os

path = "C:\\Program Files\\JetBrains\\"
big_list_size = [0] * 50
big_list_path = [''] * 50


def find50(path):
    """this is a statement"""
    try:
        parents = os.listdir(path)
        for parent in parents:
            child = os.path.join(path, parent)
            # print(child)
            if os.path.isdir(child):
                find50(child)
            # print(child)
            else:
                big_list_path[big_list_size.index(min(big_list_size))] = child
                big_list_size[big_list_size.index(min(big_list_size))] = os.path.getsize(child)
                # print(child, "---", child.split('\\')[-1:][0])
    except PermissionError:
        pass


if __name__ == '__main__':
    find50(path)
    for i in range(50):
        print(big_list_path[i], "---", big_list_size[i])
