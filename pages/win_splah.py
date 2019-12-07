#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
from tkinter import Canvas, Label, Tk

# from PIL import Image, ImageTk

import lib.global_variable as glv
from lib.functions import set_window_center


class Splah(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Doctor's appointment")
        self.w = 300
        self.h = 300
        set_window_center(self, self.w, self.h)
        self.resizable(False, False)
        self.splash()

    def splash(self):
        image_file = os.path.join(
            glv.get_variable("APP_PATH"),
            glv.get_variable("DATA_DIR"),
            "image",
            "splash.jpg",
        )
        canvas = Canvas(self, width=self.w, height=250, bg="white")
        # if os.path.exists(image_file):
        #     img = Image.open(image_file)  # 打开图片
        #     image = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
        #     canvas.create_image(self.w / 2, 250 / 2, image=image)
        # else:
        canvas.create_text(
            self.w / 2, 250 / 2, text="MIT, University of Dhaka", font="time 20", tags="string"
        )

        canvas.pack(fill="both")
        Label(self, text="welcome", bg="green", fg="#fff", height=2).pack(
            fill="both", side="bottom"
        )

        # 设置splash显示的时间，单位是毫秒（milliseconds）
        self.after(4000, self.destroy)
        self.mainloop()
