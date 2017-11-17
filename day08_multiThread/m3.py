"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: m3.py
@time: 2017/11/16 23:07
@describe:
"""

from queue import Queue
import random
import threading
import time
import tkinter as tk
import tkinter.messagebox
from tkinter import scrolledtext


# Producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        while (True):
            con.acquire()
            for i in range(5):
                self.data.put(i)
            print('wait')
            con.wait()
            con.release()


con = threading.Condition()


def callback(event):
    con.acquire()
    print('notify')
    con.notify()
    for i in range(5):
        scr.insert(tk.END, str(i) + '\n')
    con.release()


# Main thread
queue = Queue()
producer = Producer('Pro.', queue)
producer.start()
# producer.join()

window = tk.Tk()
window.title('my window')
window.geometry('200x800')
scr = scrolledtext.ScrolledText(window, width=30, height=800)
scr.pack()
for i in range(5):
    scr.insert(tk.INSERT, str(queue.get()) + '\n')
scr.bind('<Button-1>', callback)
window.mainloop()
