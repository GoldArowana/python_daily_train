"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k12.py
@time: 2017/11/16 22:09
@describe:
"""
import tkinter as tk
import tkinter.messagebox
from tkinter import scrolledtext

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 滚动文本框
scrolW = 30  # 设置文本框的长度
scrolH = 30  # 设置文本框的高度
var = tk.StringVar()
scr = scrolledtext.ScrolledText(window, width=scrolW, height=scrolH,
                                wrap=tk.WORD)  # wrap=tk.WORD   这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示,比如输入hello，he在第一行的行尾,llo在第二行的行首, 这时如果wrap=tk.WORD，则表示会将 hello 这个单词挪到下一行行首显示, wrap默认的值为tk.CHAR
# scr.grid(column=0, columnspan=3)  # columnspan 个人理解是将3列合并成一列   也可以通过 sticky=tk.W  来控制该文本框的对齐方式
scr.pack()
scr.insert(tk.INSERT, 'asdfasdfasdf')
print(scr.get(1.0, tk.END))
window.mainloop()  # 当调用mainloop()时,窗口才会显示出来
