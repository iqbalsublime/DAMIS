#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, messagebox

class MainMenu:

    def __init__(self, master):
        self.master = master 
        self.root = master.root 
        self.init_menu()

    def init_menu(self):


        self.menubar = Menu(self.root)

        self.root.config(menu=self.menubar)

        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.file_new)
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_command(label="Save as", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.root.quit)

        usermenu = Menu(self.menubar, tearoff=0)
        usermenu.add_command(label="User list", command=self.master.open_user_list)
        usermenu.add_command(label="User add", command=self.master.open_user_add)
        usermenu.add_command(label="User info", command=self.master.open_user_info)
        
        articlemenu = Menu(self.menubar, tearoff=0)
        articlemenu.add_command(label="Content list", command=self.master.open_content_list)
        articlemenu.add_command(label="Content add", command=self.master.open_content_add)
        articlemenu.add_command(label="Content count", command=self.master.open_content_count)
        
        docotrmenu = Menu(self.menubar, tearoff=0)
        docotrmenu.add_command(label="Doctor list", command=self.master.open_doctor_list)
        docotrmenu.add_command(label="Doctor add", command=self.master.open_doctor_add)
        docotrmenu.add_command(label="Doctor count", command=self.master.open_doctor_count)

        datamenu = Menu(self.menubar, tearoff=0)
        datamenu.add_command(label="Download", command=self.master.open_download)
        datamenu.add_command(label="Upload", command=self.master.open_upload)
        datamenu.add_command(label="Synchronize", command=self.master.open_synchronize)
        datamenu.add_command(label="Backup", command=self.master.open_backup)
        
        window_menu = Menu(self.menubar)
        window_menu.add_command(label="maximize")
        window_menu.add_command(label="minimize")
        window_menu.add_separator()
        window_menu.add_command(label="Window top", command=self.master.window_to_top)
        window_menu.add_command(label="Unpin", command=self.master.window_not_top)
        window_menu.add_separator()
        window_menu.add_command(label="Main interface", command=self.master.open_home)
        window_menu.add_command(label="Switch to: User")
        window_menu.add_command(label="Switch to: Article list")

        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="welcome", command=self.help_about)
        helpmenu.add_command(label="Documentation", command=self.help_about)
        helpmenu.add_command(label="Copyright Notice", command=self.help_about)
        helpmenu.add_command(label="Privacy statement", command=self.help_about)
        helpmenu.add_separator()
        helpmenu.add_command(label="contact us", command=self.master.open_ontact)
        helpmenu.add_command(label="on", command=self.master.open_about)

        self.menubar.add_cascade(label="File", menu=filemenu)
        self.menubar.add_cascade(label="User", menu=usermenu)
        self.menubar.add_cascade(label="Doctor", menu=docotrmenu)
        self.menubar.add_cascade(label="Article", menu=articlemenu)
        self.menubar.add_cascade(label="Data", menu=datamenu)
        self.menubar.add_cascade(label="Window", menu=window_menu)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

    def file_open(self):
        messagebox.showinfo("turn on", "File-Open!")  # 消息提示框

    def file_new(self):
        messagebox.showinfo("New", "File-New!")  # 消息提示框

    def file_save(self):
        messagebox.showinfo("Save", "File-Save!")  # 消息提示框

    def edit_cut(self):
        messagebox.showinfo("Cut", "Edit-cut!")  # 消息提示框

    def edit_copy(self):
        messagebox.showinfo("Copy", "Edit-Copy！")  # 消息提示框

    def edit_paste(self):
        messagebox.showinfo("Paste", "Edit-Paste!")  # 消息提示框

    def help_about(self):
        messagebox.showinfo(
            "On", "Developed by MIT, University of Dhaka"
        )
