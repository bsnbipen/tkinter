from textwrap import fill
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import numpy as np

class speed_label(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.lbl_speed=Label(self,text="Enter Speedv (mm/s)",font=("courier",12,'bold'))
        self.entr_speed=Entry(self,width=3,borderwidth=2)
        self.entr_speed.insert(0,'11')
        self.lbl_speed.pack(side=TOP)
        self.entr_speed.pack(side=TOP,expand=YES,fill=BOTH)
        Button(self,text="Select",command=self.select).pack(side=RIGHT,expand=YES,fill=Y,anchor="e")
        Button(self,text="RESET",command=self.reset).pack(side=LEFT,expand=YES,fill=Y,anchor="w")

    

    def select(self):
        speed= self.entr_speed.get()
        if float(speed) >=20:
            showinfo("High Speed!!","High Speed, Slow Down")
        elif float(speed)<=0 :
            showerror("Wrong Entry","Enter a Correct Value")
        else:
            self.entr_speed.config(state=DISABLED)

    def reset(self):
        self.entr_speed.config(state=NORMAL)

if __name__=="__main__":
    root=Tk()
    frame_speed_select=Frame(root,borderwidth=1)
    frame_speed_select.pack(side=TOP)
    entry_1=speed_label(frame_speed_select)
    root.mainloop()