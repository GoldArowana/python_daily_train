"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k5.py
@time: 2017/11/16 19:32
@describe:
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()


def print_selection(v):
    label.config(text='you have selected ' + v)


s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
