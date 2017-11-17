"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k2.py
@time: 2017/11/16 17:44
@describe:
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

e = tk.Entry(window, show=None)  # show='*'
e.pack()

t = tk.Text(window, height=2)
t.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_xy():
    var = e.get()
    t.insert(1.1, var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()
window.mainloop()
