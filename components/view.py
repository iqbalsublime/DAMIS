#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Toplevel, Label, Message
from components import frames, menu
from lib.functions import set_window_center
from pages import winAbout


class MainPage():

    def __init__(self, master=None):
        self.root = master 
        set_window_center(self.root, 800, 600)
        menu.MainMenu(self) 
        # 初始化Frames
        self.current_frame = None
        self.page_frame = {
            "home": frames.HomeFrame,
            "content_add": frames.ContentAdd,
            "content_list": frames.ContentList,
            "doctor_add": frames.DoctorAdd,
            "doctor_list": frames.DoctorList,
            "count": frames.CountFrame,
            "contact": frames.AboutFrame,
            "user_list": frames.UserListFrame,
            "user_add": frames.UserAddFrame
        }
        self.open_home()
        self.win_about = None

    def open_page(self, frame_name, title):
        self.root.title(title)
        # 先销毁之前frame
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def open_home(self):
        self.open_page("home", "Application main interface")

    def open_content_add(self):
        self.open_page("content_add", "Article added")

    def open_content_list(self):
        self.open_page("content_list", "Article query")

    def open_content_count(self):
        self.open_page("count", "Article Statistics")
        
    def open_doctor_add(self):
        self.open_page("doctor_add", "Doctor add")

    def open_doctor_list(self):
        self.open_page("doctor_list", "Doctor query")

    def open_doctor_count(self):
        self.open_page("count", "Article Statistics")    
        

    def open_ontact(self):
        self.open_page("contact", "contact us")

    def open_user_info(self):
        page = Toplevel()
        page.title("User details")
        page.resizable(False, False)
        set_window_center(page, 200, 150)

        # Label(page).grid(row=0, stick="w", pady=2)

        Label(page, text="Name: ").grid(row=1, stick="w", pady=2)
        Label(page, text="administrator").grid(row=1, column=1, stick="e")

        Label(page, text="Account: ").grid(row=2, stick="w", pady=2)
        Label(page, text="admin").grid(row=2, column=1, stick="e")

        Label(page, text="password: ").grid(row=3, stick="w", pady=2)
        Label(page, text="admin").grid(row=3, column=1, stick="e")

    def open_user_list(self):
        self.open_page("user_list", "user list")
        # self.page_frame['user_list'].init_data()

    def open_user_add(self):
        self.open_page("user_add", "User add")

    def open_download(self):
        root = Toplevel()
        root.title("Download management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-up windows, with independent window properties.", width=150)
        msg.pack()

    def open_upload(self):
        root = Toplevel()
        root.title("Upload management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-up windows, with independent window properties.", width=150)
        msg.pack()

    def open_synchronize(self):
        root = Toplevel()
        root.title("Sync management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-up windows, with independent window properties.", width=150)
        msg.pack()

    def open_backup(self):
        root = Toplevel()
        root.title("Backup management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-up windows, with independent window properties.", width=150)
        msg.pack()

    def open_about(self):
        if self.win_about and self.win_about.destroy:
            self.win_about.destroy()
        self.win_about = winAbout.Init()

    def window_to_top(self):
        self.root.attributes('-topmost', True)

    def window_not_top(self):
        self.root.attributes('-topmost', False)
