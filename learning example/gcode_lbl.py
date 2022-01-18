from asyncio.windows_events import NULL
import decimal
from itertools import dropwhile
from textwrap import fill
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import numpy as np
from numpy.core._exceptions import _UFuncNoLoopError


class absolute_movement(axis,distance):
    def __init__ (axis,distance):
        self.axis=axis
        self.distance=distance
        if self.axis=="x":
            axis_x.move_absolute(self.distance, Units.LENGTH_MILLIMETRES)
        elif axis=="y":
            axis_y.move_absolute(self.distance, Units.LENGTH_MILLIMETRES)
        elif axis=="z":
            axis_z.move_aboslute(self.distance,Units.LENGTH_MILLIMETRES)

class relative_movement(axis,distance):
    def __init__(axis,distance):
        self.axis=axis;
        self.distance=distance
        if axis=="x":
            axis_x.move_relative(self.distance, Units.LENGTH_MILLIMETRES)
        elif axis=="y":
            axis_y.move_relative(self.distance, Units.LENGTH_MILLIMETRES)
        elif axis=="z":
            axis_z.move_relative(self.distance,Units.LENGTH_MILLIMETRES)

class lbl_entr(Frame):
    def __init__(self,lbl_name,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.lbl_name=lbl_name
        Label(self,text=self.lbl_name,font=("courier",12,'bold')).pack(side=LEFT,expand=YES,fill=BOTH)
        self.entr_lbl=Entry(self,width=10,borderwidth=2)
        self.entr_lbl.pack(side=RIGHT,expand=YES,fill=BOTH)
    
class gcode(Frame): 
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.drp_option=["G90 G01","G92 G01"]
        Label(self,text="Run G-CODE",font=("courier",15,"bold")).pack(side=TOP)
        self.var=StringVar()
        #drop frame
        drp_frame=Frame(self)
        drp_frame.pack(side=TOP,expand=YES,fill=X)
        self.drp_gcod=OptionMenu(drp_frame,self.var,*self.drp_option)
        self.drp_gcod.pack(side=LEFT,fill=X,anchor="center")
        #buttonframe
        frame_button=Frame(self)
        frame_button.pack(side=BOTTOM)
        Button(self,text="Run",width=10,command=self.g_code_run).pack(side=BOTTOM,fill=Y,anchor="e")
        #frames
        frame_x=Frame(drp_frame)
        frame_y=Frame(drp_frame)
        frame_z=Frame(drp_frame)
        frame_z.pack(side=RIGHT)
        frame_y.pack(side=RIGHT)
        frame_x.pack(side=RIGHT)
        
        self.x_axis=lbl_entr("X Axis:",frame_x)
        self.y_axis=lbl_entr("Y Axis:",frame_y)
        self.z_axis=lbl_entr("Z Axis:",frame_z)
        
    
    def g_code_run(self):
        try:    
            print(self.var.get())
            coordinate_movement={"x": self.x_axis.entr_lbl.get(),
                "y":self.y_axis.entr_lbl.get(),
                "z":self.z_axis.entr_lbl.get()}
            list_key=[]
            if self.var.get()=="G90 G01":
                print("Moving in Absolute:")
                for key,value in coordinate_movement.items():
                    if not value:
                        list_key.append(key)
                for key_s in list_key():
                    coordinate_movement.pop(key_s)
                for axis,distance in coordinate_movement.items():
                    absolute_movement(axis,distance)


                        
        

            elif self.var.get()=="G92 G01":
                for key,value in coordinate_movement.items():
                    if not value:
                        list_key.append(key)
                    for key_s in list_key():
                        coordinate_movement.pop(key_s)
                    for axis,distance in coordinate_movement.items():
                        relative_movement(axis,distance)

            else:
                showinfo("G-Code Not Selected","Select a G-Code")
                        
        except _UFuncNoLoopError:
             showerror("Value Error","Enter a Number")         


if __name__=="__main__":
    root=Tk()
    frame_gcode=Frame(root,border=2,highlightbackground="Black",highlightthickness=1)
    frame_gcode.pack(side=TOP)
    gcode(frame_gcode)
    root.mainloop()

