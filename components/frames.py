#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import (Button, Label, Frame, Entry, LabelFrame, StringVar, messagebox,
                     scrolledtext, ttk)

import lib.dbcontent as dbcontent
from lib import global_variable
from lib.functions import treeview_sort_column
from pages import win_user_edit, win_user_info, winContentEdit, winContentInfo


class HomeFrame(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_user_info = None
        self.win_user_edit = None
        self.init_page()

    def init_page(self):
        Label(self, text="User:").pack()

        Label(self, text="Welcome" + str(global_variable.get_variable("CURRENT_USER_NAME"))).pack()
        Button(self, text="View").pack()
        
        self.list = dbcontent.user_list()

        head_frame = LabelFrame(self, text="User action")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="Details", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="edit", command=self.edit)
        btn_edit.pack(side="left")
        btn_reset = Button(head_frame, text="reset Password", command=self.reset)
        btn_reset.pack(side="left")
        btn_delete = Button(head_frame, text="delete", command=self.delete)
        btn_delete.pack(side="left")

     
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "name", "username", "password", "op")
        
        # self.tree_view.column("id", width=100) 
        # self.tree_view.column("name", width=100)
        # self.tree_view.column("password", width=100)
        # self.tree_view.column("op", width=100)
        
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("name", text="Name")
        self.tree_view.heading("username", text="User Name")
        self.tree_view.heading("password", text="Password")
        self.tree_view.heading("op", text="OP")

        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["name"], item["username"], item["password"], "Details"),
            )

        self.tree_view.bind("<<TreeviewSelect>>", self.select)

 
        for col in self.tree_view["columns"]:
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")
        Label(self, text="Bottom action bar").grid(sticky="swe")


class DoctorAdd(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.name = StringVar()
        self.designation = StringVar()
        self.degree = StringVar()
        self.address = StringVar()
        self.time = StringVar()
        self.fee = StringVar()
        self.init_page()

    def init_page(self):

        Label(self).grid(row=0, stick="w", pady=10)

        lb1 = Label(self, text="Name: ")
        lb1.grid(row=1, stick="w", pady=10)

        et1 = Entry(self, textvariable=self.name)
        et1.grid(row=1, column=1, stick="we")

        lb2 = Label(self, text="Designation: ")
        lb2.grid(row=2, stick="nw", pady=10)

        et2 = Entry(self, textvariable=self.designation)
        et2.grid(row=2, column=1, stick="nswe")
       
        #et2.grid(row=2, column=1, ipadx=10, stick="nswe")
        #self.content_textarea = et2

        lb3 = Label(self, text="Degree: ")
        lb3.grid(row=3, stick="w", pady=10)

        et3 = Entry(self, textvariable=self.degree)
        et3.grid(row=3, column=1, columnspan=2, stick="we")
        
        
        lb4 = Label(self, text="Address: ")
        lb4.grid(row=4, stick="w", pady=10)

        et4 = Entry(self, textvariable=self.address)
        et4.grid(row=4, column=1, columnspan=2, stick="we")
        
        lb5 = Label(self, text="Time: ")
        lb5.grid(row=5, stick="w", pady=10)

        et5 = Entry(self, textvariable=self.time)
        et5.grid(row=5, column=1, columnspan=2, stick="we")
        
        lb6 = Label(self, text="Fee: ")
        lb6.grid(row=6, stick="w", pady=10)

        et6 = Entry(self, textvariable=self.fee)
        et6.grid(row=6, column=1, columnspan=2, stick="we")

        bt1 = Button(self, text="Add to", command=self.do_add)
        bt1.grid(row=7, column=0, stick="e", pady=10)

    def do_add(self):
        name = self.name.get()
        designation = self.designation.get()
        degree = self.degree.get()
        address = self.address.get()
        time = self.time.get()
        fee = self.fee.get()
        
        #username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        res = dbcontent.doctor_add(name, designation, degree, address, time, fee)
        if res is True:
            self.name.set("")
            self.designation.set("")
            self.degree.set("")
            self.address.set("")
            self.time.set("")
            self.fee.set("")
            messagebox.showinfo(title="success", message="Doctor added successfully")
        else:
            messagebox.showinfo(title="error", message="add failed")


class DoctorList(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_content_info = None
        self.win_content_edit = None
        self.init_page()

    def init_page(self):

        #username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        self.list = dbcontent.doctor_list()

        head_frame = LabelFrame(self, text="Doctor list")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        """
        btn_info = Button(head_frame, text="Details", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="edit", command=self.edit)
        btn_edit.pack(side="left")
        btn_delete = Button(head_frame, text="delete", command=self.delete)
        btn_delete.pack(side="left")
        """
   
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("name", "designation", "degree", "fee", "address")
       
        self.tree_view.column("name", width=100)
        # self.tree_view.column("title", width=100)
        # self.tree_view.column("content", width=100)
        # self.tree_view.column("tag", width=100)
       
        self.tree_view.heading("name", text="Name")
        self.tree_view.heading("designation", text="Designation")
        self.tree_view.heading("degree", text="Degree")
        self.tree_view.heading("fee", text="Fee")
        self.tree_view.heading("address", text="Address")


        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["name"], item["designation"], item["degree"], item["fee"], item["address"]),
            )
       
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        
        for col in self.tree_view["columns"]: 
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")

    def select(self, event):
       
     
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
        
        print("Details", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please select first")
        else:
            if self.win_content_info is not None and hasattr(self.win_content_info.destroy, "__call__"):
                # if self.win_content_info and self.win_content_info.destroy:
                self.win_content_info.destroy()
            self.win_content_info = winContentInfo.Init(self.selected_item)
            # self.win_content_info = winAbout.Init()

    def edit(self):
        print("edit", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please select first")
        else:
            if self.win_content_edit and self.win_content_edit.destroy:
                self.win_content_edit.destroy()
            self.win_content_edit = winContentEdit.Init(self.selected_item)

    def delete(self):
        print(self.selected_item)
        messagebox.showinfo("delete?", self.selected_item)



class ContentAdd(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.content_title = StringVar()
        self.content_textarea = StringVar()
        self.content_tag = StringVar()
        self.init_page()

    def init_page(self):

        Label(self).grid(row=0, stick="w", pady=10)

        lb1 = Label(self, text="Title: ")
        lb1.grid(row=1, stick="w", pady=10)

        et1 = Entry(self, textvariable=self.content_title)
        et1.grid(row=1, column=1, stick="we")

        lb2 = Label(self, text="content: ")
        lb2.grid(row=2, stick="nw", pady=10)

        """
        et2 = scrolledtext.ScrolledText(
            self,
            height=10,
            font=("Courier New", 13),
            fg="#333",
            borderwidth=1,
            highlightcolor="#ddd",
        )
        """
        et2 = Entry(self, textvariable=self.content_textarea)
        et2.grid(row=2, column=1, stick="nswe")
       
        #et2.grid(row=2, column=1, ipadx=10, stick="nswe")
        #self.content_textarea = et2

        lb3 = Label(self, text="label: ")
        lb3.grid(row=3, stick="w", pady=10)

        et3 = Entry(self, textvariable=self.content_tag)
        et3.grid(row=3, column=1, columnspan=2, stick="we")

        bt1 = Button(self, text="Add to", command=self.do_add)
        bt1.grid(row=4, column=0, stick="e", pady=10)

    def do_add(self):
        title = self.content_title.get()
        content = self.content_textarea.get()
        tag = self.content_tag.get()
        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        res = dbcontent.content_add(username, title, content, tag)
        if res is True:
            self.content_title.set("")
            self.content_tag.set("")
            self.content_textarea.set("")  # 清空
            #self.content_textarea.update()
            messagebox.showinfo(title="success", message="Added successfully")
        else:
            messagebox.showinfo(title="error", message="add failed")


class ContentList(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_content_info = None
        self.win_content_edit = None
        self.init_page()

    def init_page(self):

        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        self.list = dbcontent.content_list_by_username(username)

        head_frame = LabelFrame(self, text="Article operation")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="Details", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="edit", command=self.edit)
        btn_edit.pack(side="left")
        btn_delete = Button(head_frame, text="delete", command=self.delete)
        btn_delete.pack(side="left")

   
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "title", "content", "tag")
       
        self.tree_view.column("id", width=100)
        # self.tree_view.column("title", width=100)
        # self.tree_view.column("content", width=100)
        # self.tree_view.column("tag", width=100)
       
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("title", text="Title")
        self.tree_view.heading("content", text="Content")
        self.tree_view.heading("tag", text="Tag")


        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["title"], item["content"], item["tag"]),
            )
       
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        
        for col in self.tree_view["columns"]: 
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")

    def select(self, event):
       
     
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
        
        print("Details", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please select first")
        else:
            if self.win_content_info is not None and hasattr(self.win_content_info.destroy, "__call__"):
                # if self.win_content_info and self.win_content_info.destroy:
                self.win_content_info.destroy()
            self.win_content_info = winContentInfo.Init(self.selected_item)
            # self.win_content_info = winAbout.Init()

    def edit(self):
        print("edit", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please select first")
        else:
            if self.win_content_edit and self.win_content_edit.destroy:
                self.win_content_edit.destroy()
            self.win_content_edit = winContentEdit.Init(self.selected_item)

    def delete(self):
        print(self.selected_item)
        messagebox.showinfo("delete?", self.selected_item)


class CountFrame(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        Label(self, text="Statistics interface").pack()


class AboutFrame(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        # Label(self, text="关于界面").grid()
        Label(self, text="Hello").grid()
        Label(self, text="Similar to pop-up windows, with independent window properties.", width=150).grid()


class UserListFrame(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_user_info = None
        self.win_user_edit = None
        self.init_page()

    def init_page(self):

        self.list = dbcontent.user_list()

        head_frame = LabelFrame(self, text="User action")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="Details", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="edit", command=self.edit)
        btn_edit.pack(side="left")
        btn_reset = Button(head_frame, text="reset Password", command=self.reset)
        btn_reset.pack(side="left")
        btn_delete = Button(head_frame, text="delete", command=self.delete)
        btn_delete.pack(side="left")

        
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "name","username", "password", "op")
        # 列设置
        # self.tree_view.column("id", width=100) # 表示列,不显示
        # self.tree_view.column("name", width=100)
        # self.tree_view.column("password", width=100)
        # self.tree_view.column("op", width=100)
        # 显示表头
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("name", text="Name")
        self.tree_view.heading("username", text="Username")
        self.tree_view.heading("password", text="Password")
        self.tree_view.heading("op", text="OP")

        
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["name"],item["username"], item["password"], "Details"),
            )
        
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        
        for col in self.tree_view["columns"]:
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")
        Label(self, text="(c) MIT, DU").grid(sticky="swe")

    def select(self, event):

        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])

    def info(self):

        print("Details", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please select first")
        else:
            if self.win_user_info is not None and (
                hasattr(self.win_user_info.destroy, "__call__")
            ):
                self.win_user_info.destroy()
            self.win_user_info = win_user_info.Init(self.selected_item)

    def edit(self):

        print("Edit", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please select first")
        else:
            if self.win_user_edit is not None and hasattr(
                self.win_user_edit.destroy, "__call__"
            ):
                self.win_user_edit.destroy()
            self.win_user_edit = win_user_edit.Init(self.selected_item)

    def delete(self):

        print(self.selected_item)
        messagebox.showinfo("delete users?", self.selected_item)

    def reset(self):
        """User delete"""
        print("User delete")


class UserAddFrame(Frame):


    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.username = StringVar()
        self.name = StringVar()
        self.password = StringVar()
        self.init_page()

    def init_page(self):

        Label(self).grid(row=0, stick="w")

        Label(self, text="Username: ").grid(row=1, stick="w", pady=10)
        username = Entry(self, textvariable=self.username)
        username.grid(row=1, column=1, stick="e")
        
        Label(self, text="Name: ").grid(row=2, stick="w", pady=10)
        name = Entry(self, textvariable=self.name)
        name.grid(row=2, column=1, stick="e")

        Label(self, text="Password: ").grid(row=3, stick="w", pady=10)
        password = Entry(self, textvariable=self.password, show="*")
        password.grid(row=3, column=1, stick="e")

        button_login = Button(self, text="Add", command=self.do_add)
        button_login.grid(row=4, column=1, stick="w", pady=10)

    def do_add(self):
        # print(event)
        username = self.username.get()
        name = self.name.get()
        password = self.password.get()
        res = dbcontent.user_add(username, name, password)
        if res is True:
            self.username.set("")
            self.name.set("")
            self.password.set("")
            messagebox.showinfo(title="success", message="Added successfully")
        else:
            messagebox.showinfo(title="error", message="error")
