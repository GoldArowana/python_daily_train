"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: t2.py
@time: 2017/11/13 22:10
@describe:
"""

from tkinter import *


class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def gettext(self):
        return self.text.get('1.0', END + '-1c')


if __name__ == '__main__':
    root = Tk()
    try:
        st = ScrolledText(file=sys.argv[1])
    except IndexError:
        st = ScrolledText(text='Words\ngo here')


    def show(event):
        print(repr(st.gettext()))


    root.bind('<Key-Escape>', show)
    root.mainloop()
