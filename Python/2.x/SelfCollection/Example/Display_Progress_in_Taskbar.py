from Tkinter import *
import clr
clr.AddReference('Microsoft.WindowsAPICodePack.Shell')
from Microsoft.WindowsAPICodePack.Taskbar import TaskbarManager


def onMove(value):
    TaskbarManager.Instance.SetProgressValue(value, 100)

root = Tk()
tbar = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=onMove)
tbar.pack()
root.mainloop()
