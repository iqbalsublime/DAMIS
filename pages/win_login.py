#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Button, Entry, Frame, Label, Menu, StringVar, messagebox

import lib.dbcontent as dbcontent
import lib.global_variable as glv
from components.view import MainPage
from lib.functions import set_window_center


class Login():

    def __init__(self, master=None):
        if self.isLoggedIn() is True:
            MainPage(master)
        else:
            self.root = master
            self.root.title("Account login")
            set_window_center(self.root, 300, 180)
            # 定义变量
            self.username = StringVar()
            self.password = StringVar()
            self.init_menu()
            self.init_page()

    def init_page(self):

        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()

        Label(self.page).grid(row=0, stick="W")

        Label(self.page, text="Account: ").grid(row=1, stick="W", pady=10)
        username = Entry(self.page, textvariable=self.username)
        username.grid(row=1, column=1, stick="E")
        username.bind("<Return>", self.returnEnvent)

        Label(self.page, text="password: ").grid(row=2, stick="W", pady=10)
        password = Entry(self.page, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick="E")
        password.bind("<Return>", self.returnEnvent)

        button_login = Button(self.page, text="Login", command=self.doLogin)
        button_login.grid(row=3, column=1, stick="W", pady=10)

        button_cancel = Button(self.page, text="Cancel", command=self.doCancel)
        button_cancel.grid(row=3, column=1, stick="e")

    def init_menu(self):
        
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=self.root.quit)
        menubar.add_cascade(label="file", menu=filemenu)
        self.root.config(menu=menubar)

    def doLogin(self):
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_login(username, password)
        if res is True:
            # if username == "admin" and password == "admin": # 测试账号
            self.page.destroy()

            glv.set_variable("CURRENT_USER_NAME", str(username))
            MainPage(self.root)
        else:
            messagebox.showinfo(title="error", message="Incorrect username or password!")

    def doCancel(self):
        self.page.quit()

    def returnEnvent(self, event):
        self.doLogin()

    def isLoggedIn(self):
        # return True
        return False
