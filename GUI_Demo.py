import tkinter
from tkinter import *
import tkinter.messagebox as msg

MyObj = tkinter.Tk()
MyObj.geometry("400x400")

def Hello():
    msg.showinfo("You clicked button..")

B1 = tkinter.Button(MyObj,text ="Click Here ....")
B2 = tkinter.Button(MyObj,text = "Output is this ",command = Hello)
B1.pack()
B2.pack()
MyObj.mainloop()