"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: i_自定义异常.py
@time: 2017/10/4 20:02
@describe:
"""


class ShortInputException(Exception):
    def __init__(self, num):
        self.num = num


def main():
    try:
        raise ShortInputException(3)
    except ShortInputException as result:
        print("抛出自定义异常",result.num)
    else:
        print("没有发生异常")


main()
