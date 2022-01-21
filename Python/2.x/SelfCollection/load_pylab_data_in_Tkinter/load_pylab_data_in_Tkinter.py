# coding: utf-8

'''
在Tkinter内加载pylab画出的图

@ Windows 7 64-bit Pro ENU
'''


import os
import sys
import Tkinter as TK
from PIL import Image, ImageTk


def data_matplotlib():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(-10, 10, 10000)
    a = np.sin(x)
    b = np.cos(x)
    c = np.tan(x)
    d = np.log(x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, a, label="$sin(x)$", color="green", linewidth=1)
    plt.plot(x, b, label="$cos(x)$", color='blue', linewidth=1)
    plt.plot(x, c, "b--", label="$tan(x)$", color='red', linewidth=1)
    plt.plot(x, d, "b--", label="$log(x)$", color='grey', linewidth=1)

    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("PyPlot Sample")
    plt.xlim(-10, 10)
    plt.ylim(-1, 1)
    plt.legend()
    plt.savefig('tmp.png')
    return ImageTk.PhotoImage(Image.open('tmp.png'))

# Definition
image  = 'Hydrangeas.jpg'

# Tkinter
root = TK.Tk()
root.title('加载图形数据')
root.geometry('1024x768+1+1')
root.update()
canvas      = TK.Canvas(root, width=1024, height=768, bg='green')
image_data  = ImageTk.PhotoImage(Image.open(image)) #不能直接写到create_image函数，否则图片不显示
canvas.create_image(0, 0, image=image_data, anchor=TK.NW) #anchor=TK.NW使得图片正确显示
i = data_matplotlib()
canvas.create_image(100, 200, image=i, anchor=TK.NW)
canvas.create_text(root.winfo_width()/2, root.winfo_height()/10,
    text='Sample', font=('Arial', 18), fill='white')
canvas.pack(side=TK.TOP, expand=1, fill='both')

root.mainloop()
