"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k4.py
@time: 2017/11/16 19:18
@describe:
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()


def print_selection():
    label.config(text='you have selected ' + var.get())


r1 = tk.Radiobutton(window, text='Option A', indicatoron=0, variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', indicatoron=0, variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', indicatoron=0, variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()
