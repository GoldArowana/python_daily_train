"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: k10.py
@time: 2017/11/16 20:45
@describe:
"""

import tkinter as tk

window = tk.Tk()
window.geometry('200x200')


# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)


tk.Label(window, text='1').pack(side='top')
tk.Label(window, text='1').pack(side='bottom')
tk.Label(window, text='1').pack(side='left')
tk.Label(window, text='1').pack(side='right')

tk.Label(window, text=2).place(x=70, y=40, anchor='nw')

window.mainloop()
