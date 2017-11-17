"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: b_私有方法.py
@time: 2017/10/4 10:43
@describe:
"""


class Cat:
    # __两个下划线表示私有方法
    def __send_msg(self):
        print('正在发送短信')

    def send_msg(self, new_money):
        if new_money > 10:
            self.__send_msg()
        else:
            print('余额不足')


cat = Cat()
cat.send_msg(100)
