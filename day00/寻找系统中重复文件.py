"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: 寻找系统中重复文件.py
@time: 2017/11/13 23:34
@describe:
"""

import os

path = "C:\\Program Files\\JetBrains\\"

dictionary = {}


def find_duplicated(path):
    """this is a statement"""
    try:
        parents = os.listdir(path)
        for parent in parents:
            child = os.path.join(path, parent)
            # print(child)
            if os.path.isdir(child):
                find_duplicated(child)
            # print(child)
            else:
                file_name = child.split("\\")[-1:][0]
                temp_list = [] if dictionary.get(file_name) is None else dictionary.get(file_name)
                temp_list.append(child)
                dictionary.update({file_name: temp_list})
                # print(child, "---", child.split('\\')[-1:][0])
    except PermissionError:
        pass


dictionary2 = {}
if __name__ == '__main__':
    find_duplicated(path)
    for key in dictionary:
        if len(dictionary[key]) > 1:
            dictionary2.update({key: dictionary[key]})

    dictionary = dictionary2
    del dictionary2

    for key in dictionary:
        print("--------", key, "--------")
        for i in range(len(dictionary[key])):
            file_path = dictionary[key][i]
            print("大小：", os.path.getsize(file_path), "创建时间:", os.path.getctime(file_path), "路径：", file_path)
