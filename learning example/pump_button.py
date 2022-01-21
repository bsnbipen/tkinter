from tkinter import *
import tkinter.ttk
from glob import glob
import random
import os
from PIL import Image, ImageTk
from zaber_motion.ascii import DeviceIO

os_dir=os.getcwd()
img_dir=(os_dir+r"\tkinter\images")


    

root=Tk()

var_pump_state_1=int(0)
var_pump_state_2=int(0)

#Frame
lbl_frame_tb2=Frame(root)
lbl_frame_tb2.pack()

#image COnfiguration
off_image=Image.open(img_dir+r"\off.png")
off_image = off_image.resize((50,50), Image.ANTIALIAS)                        #off button
off_icn=ImageTk.PhotoImage(off_image)

on_image=Image.open(img_dir+"\on.png")
on_image = on_image.resize((50,50), Image.ANTIALIAS)                        #on button
on_icn=ImageTk.PhotoImage(on_image)


def state_pump():
    global var_pump_state_1
    if var_pump_state_1==1:
        btn_pump_1.config(image=off_icn)
        var_pump_state_1=0
        lbl_pump_1.config(text="Pump One: Off")
        #print(var_pump_state_1)
    else: 
        var_pump_state_1=1
        lbl_pump_1.config(text="Pump One: On")
        btn_pump_1.config(image=on_icn)
        #print(var_pump_state_1)

def state_pump_2():
    global var_pump_state_2
    if var_pump_state_2==1:
        btn_pump_2.config(image=off_icn)
        var_pump_state_2=0
        lbl_pump_2.config(text="Pump Two: Off")
        #print(var_pump_state_2)
    else: 
        var_pump_state_2=1
        lbl_pump_2.config(text="Pump Two: On")
        btn_pump_2.config(image=on_icn)
        #print(var_pump_state_2)

#pump 1 button configuration
frm_btn_1=Frame(lbl_frame_tb2)
frm_btn_1.pack(side=LEFT,padx=10)
btn_pump_1=Button(frm_btn_1,image=off_icn,borderwidth=0,command=(lambda : state_pump()))
lbl_pump_1=Label(frm_btn_1,text="Pump One: Off", font=('courier',13,'bold'))

lbl_pump_1.pack(side=TOP,expand=YES,fill=BOTH)
btn_pump_1.pack(expand=YES,fill=BOTH)

#pump 2 button configuration
frm_btn_2=Frame(lbl_frame_tb2)
frm_btn_2.pack(side=RIGHT,padx=10)
btn_pump_2=Button(frm_btn_2,image=off_icn,borderwidth=0,command=(lambda : state_pump_2()))
lbl_pump_2=Label(frm_btn_2,text="Pump Two: Off", font=('courier',13,'bold'))

lbl_pump_2.pack(side=TOP,expand=YES,fill=BOTH)
btn_pump_2.pack(expand=YES,fill=BOTH)

mainloop()