"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k1.py
@time: 2017/11/16 17:25
@describe:
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

lableString = tk.StringVar()
l = tk.Label(window, textvariable=lableString, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit is False:
        on_hit = True
        lableString.set('you hit me')
    else:
        on_hit = False
        lableString.set('')


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()
window.mainloop()
