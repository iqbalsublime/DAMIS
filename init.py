#!/usr/bin/env python3
# -*- coding:utf-8-*-

import tkinter.messagebox
from tkinter import Button, Label, Tk

from lib.functions import set_window_center
from lib.sqlite_helper import DBHelper
from main import App


class InitWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Initialization data")
        set_window_center(self, 300, 180)
        self.resizable(False, False)
        self.win_success = None # 初始化成功的提示窗口
        self.init_page()

    def init_page(self):
        btn_1 = Button(self, text="Initialize the database", command=self.do_init_db)
        btn_1.pack(expand="yes", padx=10, pady=10, ipadx=5, ipady=5)

    def do_init_db(self):
        db_helper = DBHelper()
        db_helper.reset_database()
        db_helper.create_database()
        try:
            tmp = db_helper.insert_user("admin", "admin", "admin")
            tmp1 = db_helper.insert_doctor("Kazi Foyeza", "Asst. Professor", "MBBS,FCPS", "Tejgaon", "6PM-10PM", "1000TK")
            tmp2 = db_helper.insert_content_by_username(
                "admin",
                "Hello World !",
                "https://github.com/iqbalsublime",
                "github",
            )
            tmp3 = db_helper.get_content_by_username("admin")
            print("admin:", tmp)
            print("Doctor Add:", tmp1)
            print("Add content:", tmp2)
            print("Query content:", tmp3)
            self.do_success()
            self.destroy()
        except KeyError:
            print(KeyError)
            self.do_failed()

    def do_failed(self):
        res = tkinter.messagebox.askretrycancel('prompt', 'Initialization failed, whether to retry？', parent=self)
        if res is True:
            self.do_init_db()
        elif res is False:
            self.destroy()

    def do_success(self):
        self.win_success = Tk()
        self.win_success.title("Initialization successful")
        set_window_center(self.win_success, 250, 150)
        self.win_success.resizable(False, False)
        msg = Label(self.win_success, text="Initialization successful")
        msg.pack(expand="yes", fill="both")

        btn = Button(self.win_success, text="confirm", command=self.quit)
        btn.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)
        btn_open_app = Button(self.win_success, text="Start", command=self.open_app)
        btn_open_app.pack(side="right", padx=10, pady=10, ipadx=5, ipady=5)

    def open_app(self):
        self.quit()
        self.win_success.destroy()
        self.win_success.quit()

        App()


if __name__ == "__main__":
    APP_INIT = InitWindow()
    APP_INIT.mainloop()
