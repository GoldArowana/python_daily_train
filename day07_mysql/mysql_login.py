"""
@arthor:金龙
@school:hrbust
@depart:computer
@file: s1.py
@time: 2017/11/16 23:50
@describe:
"""

from day07_mysql.mysql_dao import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('hello')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='tu.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y=150)
tk.Label(window, text='Password: ').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('king')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

daoFactory = DaoFactory()
studentDaoImpl = daoFactory.getStudentDaoImpl()
loginDaoImpl = daoFactory.getLoginDaoImpl()


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    login_flag = loginDaoImpl.login(usr_name, usr_pwd)
    print(login_flag)
    if login_flag is True:
        tk.messagebox.showinfo(title='Welcome', message='Hello ' + usr_name)
        managerwindow = tk.Toplevel(window)
        managerwindow.geometry('420x300')
        managerwindow.title('Sign up window')
        loopManagerWindow(managerwindow)
    else:
        tk.messagebox.showerror(message='Error, your password is wrong, try again.')


def loopManagerWindow(managerwindow):
    label_name = tk.Label(managerwindow, text='Name:', justify=tk.RIGHT, width=50)
    label_name.place(x=10, y=5, width=50, height=20)
    var_name = tk.StringVar(value=' ')
    entry_name = tk.Entry(managerwindow, width=120, textvariable=var_name)
    entry_name.place(x=70, y=5, width=120, height=20)
    label_grade = tk.Label(managerwindow, text='Grade:', justify=tk.RIGHT, width=50)
    label_grade.place(x=10, y=40, width=50, height=20)
    student_classes = {'1': ['1', '2', '3', '4'], '2': ['1', '2'], '3': ['1', '2', '3']}
    combo_grade = tk.ttk.Combobox(managerwindow, values=tuple(student_classes.keys()), width=50)
    combo_grade.place(x=70, y=40, width=50, height=20)

    def comboChange(event):
        grade = combo_grade.get()
        if grade:
            combo_class["values"] = student_classes.get(grade)
        else:
            combo_class.set([])

    combo_grade.bind('<<ComboboxSelected>>', comboChange)
    label_class = tk.Label(managerwindow, text='Class:', justify=tk.RIGHT, width=50)
    label_class.place(x=130, y=40, width=50, height=20)
    combo_class = tk.ttk.Combobox(managerwindow, width=50)
    combo_class.place(x=190, y=40, width=50, height=20)
    label_sex = tk.Label(managerwindow, text='Sex:', justify=tk.RIGHT, width=50)
    label_sex.place(x=10, y=70, width=50, height=20)

    sex = tk.IntVar(value=1)
    radio_man = tk.Radiobutton(managerwindow, variable=sex, value=1, text='Man')
    radio_man.place(x=70, y=70, width=50, height=20)
    radio_woman = tk.Radiobutton(managerwindow, variable=sex, value=0, text='Woman')
    radio_woman.place(x=130, y=70, width=70, height=20)

    monitor = tk.IntVar(value=0)
    check_monitor = tk.Checkbutton(managerwindow, text='Is Monitor?', variable=monitor, onvalue=1, offvalue=0)
    check_monitor.place(x=20, y=100, width=100, height=20)

    def addInformation():
        ele = ''
        ele = ele + "id:" + str(studentDaoImpl.queryMaxId()+1) + ","
        ele = ele + "name:" + entry_name.get() + ","
        ele = ele + "grade:" + combo_grade.get() + ","
        ele = ele + "class:" + combo_class.get() + ","
        ele = ele + "sex:" + ('M' if sex.get() else 'F') + ","
        ele = ele + "isMonitor" + ('T' if monitor.get() else 'F') + "\n"
        listbox_students.insert(0, ele)
        studentDaoImpl.insert(Student(entry_name.get(),combo_grade.get(),combo_class.get(),'M' if sex.get() else 'F','T' if monitor.get() else 'F'))

    button_add = tk.Button(managerwindow, text='Add', width=40, command=addInformation)
    button_add.place(x=130, y=100, width=40, height=20)

    def deleteSelection():
        selection = listbox_students.curselection()
        cur_id = int(str(listbox_students.get(selection)).split(',')[0].split(':')[1])
        if not selection:
            tk.messagebox.showinfo(title='Information', message='No Selection')
        else:
            studentDaoImpl.delete(cur_id)
            listbox_students.delete(selection)

    button_delect = tk.Button(managerwindow, text='DelectSelection', width=100, command=deleteSelection)
    button_delect.place(x=180, y=100, width=100, height=20)
    listbox_students = tk.Listbox(managerwindow, width=300)
    listbox_students.place(x=10, y=130, width=400, height=200)
    list_query = studentDaoImpl.queryAll()
    list_len = len(list_query)

    for i in list_query:
        ele = ''
        ele = ele + "id:" + str(i['id']) + ","
        ele = ele + "name:" + i['name']+","
        ele = ele + "grade:" + str(i['grade']) + ","
        ele = ele + "class:" + str(i['classid']) + ","
        ele = ele + "sex:" +i['sex']+","
        ele = ele + "isMonitor" + i['isMonitor']+"\n"
        listbox_students.insert(0, ele)


def usr_sign_up():
    def sign_to_Mofan_Python():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        if npf != np:
            tk.messagebox.showerror('Error', '两次密码不一致!')
        elif loginDaoImpl.login(nn, np) is True:
            tk.messagebox.showerror('Error', '您已注册过!')
        else:
            new_user = Login(nn, np)
            loginDaoImpl.insert(new_user)
            tk.messagebox.showinfo('Welcome', '成功注册!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)


# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
