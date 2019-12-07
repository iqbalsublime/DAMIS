#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Tk, Label, Message, Toplevel

# import lib.global_variable as glv
# from lib.functions import set_window_center


class Init(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("")
        # set_window_center(self, 400, 400)
        self.app_name = "Doctor's Appointment System" # glv.get_variable("APP_NAME")
        self.app_version = "0.1.1"
        self.app_desc = "Brief description"
        self.app_url = "https://du.ac.com"
        self.app_ = "Copyright © 2019 MIT, DU. All rights reserved."
        # self.resizable(False, False)
        self.init_page()

    def init_page(self):
        Label(self, text="LOGO").pack(fill="both")
        Label(self, text=self.app_name).pack()
        Label(self, text=self.app_version).pack()
        Label(self, text=self.app_url).pack()
        Label(self, text=self.app_).pack()
        Message(self, text=self.app_desc).pack()
        # Label(self, text="你好你好你好你好").grid()
        # Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()

if __name__ == "__main__":
    APP_ABOUT = Init()
    APP_ABOUT.mainloop()