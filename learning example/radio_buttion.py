import decimal
from distutils import command
import re
from tkinter import *
import os
from tkinter.messagebox import *
from turtle import speed
from zaber_motion import Units
from zaber_motion.ascii import AxisSettings
from zaber_motion.ascii import DeviceIO
from zaber_motion.ascii import Connection
from zaber_motion.exceptions.no_device_found_exception import NoDeviceFoundException
from zaber_motion.exceptions.command_failed_exception import CommandFailedException
from numpy.core._exceptions import _UFuncNoLoopError
import sys
from PIL import Image, ImageTk
from decimal import *
import numpy as np
from zaber_motion.ascii import DeviceIO

port=('COM1',"COM2","COM3","COM4","COM5","COM6")
class speed_label(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.lbl_speed=Label(self,text="Change Speed (mm/s)",font=("courier",12,'bold'))
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
            axis_x.settings.set('maxspeed',np.round(float(speed),decimals=5), unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
            axis_y.settings.set('maxspeed',np.round(float(speed),decimals=5), unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
            axis_z.settings.set('maxspeed',np.round(float(speed),decimals=5), unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
            self.entr_speed.config(state=DISABLED)

    def reset(self):
        self.entr_speed.config(state=NORMAL)

class absolute_movement:
                try:   
                    def __init__ (self,dict_info):
                
                        self.dict_info=dict_info
                        command_move=[]
                        command_wait=[]
                        for axis,value in dict_info.items():
                            command_move.append("axis_{}.move_absolute({}, Units.LENGTH_MILLIMETRES,wait_until_idle=False)".format(axis,(np.round(float(value),decimals=5))))
                            command_wait.append("axis_{}.wait_until_idle()".format(axis))
                        for commands in command_move:
                            exec(commands)
                        for commands in command_wait:
                            exec(commands)
                        lbl_x.config(text=np.round(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5))
                        lbl_y.config(text=np.round(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5))
                        lbl_z.config(text=np.round(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5))

                except CommandFailedException:
                        showerror("Out of Range","Travel is Out of Range!!")
                        
class relative_movement:
                try:
                    def __init__ (self,dict_info):
                        self.dict_info=dict_info
                        command_move=[]
                        command_wait=[]
                        for axis,value in dict_info.items():
                            command_move.append("axis_{}.move_absolute({}, Units.LENGTH_MILLIMETRES,wait_until_idle=False)".format(axis,(np.round(float(value),decimals=5))))
                            command_wait.append("axis_{}.wait_until_idle()".format(axis))
                        for commands in command_move:
                            exec(commands)
                        for commands in command_wait:
                            exec(commands)
                        lbl_x.config(text=np.round(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5))
                        lbl_y.config(text=np.round(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5))
                        lbl_z.config(text=np.round(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5))

                except CommandFailedException:
                        showerror("Out of Range","Travel is Out of Range!!")



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
                for key_s in list_key:
                    coordinate_movement.pop(key_s)
                absolute_movement(coordinate_movement)


                        
        

            elif self.var.get()=="G92 G01":
                for key,value in coordinate_movement.items():
                    if not value:
                        list_key.append(key)
                for key_s in list_key:
                        coordinate_movement.pop(key_s)
                relative_movement(coordinate_movement)

            else:
                showinfo("G-Code Not Selected","Select a G-Code")
                        
        except _UFuncNoLoopError:
             showerror("Value Error","Enter a Number")         

class radio_bar(Toplevel):

    def __init__(self, parent=None, **options):
        Toplevel.__init__(self,parent,**options)
        self.title('Configuring Ports')
        Label(self, text="Com Port Configuration").pack(side=TOP)
        self.var=StringVar()
        for name in port:
            Radiobutton(self,text=name,
                            variable=self.var,
                            value=name).pack(side=TOP)
        self.var.set(name)
        Button(self,text='Check',command=self.check).pack(side=LEFT)
        Button(self,text="Select",command=self.select).pack(side=RIGHT)
        self.focus_set()
        self.grab_set()
        self.wait_window()

    def check(self):
        try:
            with Connection.open_serial_port(self.var.get()) as connection:
                device_list = connection.detect_devices()
                showinfo('Device Found', "Found {} devices".format(len(device_list)))
        except NoDeviceFoundException:
            showerror("Device Not Found","Zaber Device was not Found")
    
    def select(self): #This is to check the connection
        try:
            with Connection.open_serial_port(self.var.get()) as connection:
                device_list_2 = connection.detect_devices()
                showinfo("Selected","{} Port Selected".format(self.var.get()))
                global port_select
                port_select=self.var.get()
                self.destroy()

        except NoDeviceFoundException:
            showerror("Device Not Found","Zaber Device was not Found")
'''    
    def select(self):
        showinfo('Selected',"{} Port Selected".format(self.var.get()))
        global port_select
        port_select=self.var.get()
        self.destroy()
'''



# for absolute and relative motion

class radio_motion(Frame):
    def __init__(self,Parent=None,**option):
        Frame.__init__(self,Parent,**option)
        self.pack()
        self.var=IntVar(0)
        motion_type=["Absolute Motion","Relative Motion"]
        Label(self, text="Selection the Motion Type",font=("courier",15,"bold")).pack(side=TOP)
        for key in range(2):
            rad=Radiobutton(self,
                        text=motion_type[key],
                        variable=self.var,
                        font=("courier",12,"bold"),
                        value=key).pack(anchor=NW)
      
        
class speedentry(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.entr_speed=Entry(self,width=10,borderwidth=3)
        self.entr_speed.insert(0,"5")
        self.lbl_speed=Label(self,text="Travel(MM):",font=('courier','12','bold'))
        self.entr_speed.pack(side=RIGHT,expand=YES,fill=BOTH)
        self.lbl_speed.pack(side=LEFT,expand=YES,fill=BOTH)

if __name__=='__main__':
    root=Tk()
    radio_bar()

    try:
        with Connection.open_serial_port(port_select) as connection:
            main_frame=Frame(root)
            main_frame.pack()
            frame_ab_rel=Frame(root)
            frame_ab_rel.pack()
            #travel distance variables
            distance_trv=0
            distance_trv_lft=0
            distance_trv_rht=0
            distance_trv_dwn=0
            #axis
            device_list = connection.detect_devices()
            device = device_list[0]
            
            #naming axis
            axis_x = device.get_axis(2)
            axis_y=device.get_axis(3)
            axis_z=device.get_axis(1)
            #SET VELOCTIY
            axis_x.settings.set('maxspeed',11, unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
            axis_y.settings.set('maxspeed',11, unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
            axis_z.settings.set('maxspeed',11, unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
            


            #for distance display

            #display frame indivisual axis
            display_frame=Frame(main_frame)
            display_frame.pack(side=TOP)

        #for x axis
            display_frame_x=Frame(display_frame)
            display_frame_x.pack(side=TOP)
            lbl_x_distance=Label(display_frame_x,
                                text="X Axis", 
                                background="Black",
                                fg="White",
                                font=("courier",18,"bold"),
                                justify=CENTER)

            lbl_x=Label(display_frame_x,
                                text=str(np.round(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)),
                                background='white',
                                fg="black",
                                font=("courier",18,"bold"),
                                justify=CENTER,
                                width=20,
                                borderwidth=5)
            lbl_x.pack(side=RIGHT,pady=1)
            lbl_x_distance.pack(side=LEFT)


        #for y axis
            display_frame_y=Frame(display_frame)
            display_frame_y.pack(side=TOP)
            lbl_y_distance=Label(display_frame_y,
                                text="Y Axis", 
                                background="Black",
                                fg="White",
                                font=("courier",18,"bold"),
                                justify=CENTER)
            lbl_y=Label(display_frame_y,
                                text=str(np.round(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)),
                                background='white',
                                fg="black",
                                font=("courier",18,"bold"),
                                justify=CENTER,
                                width=20,
                                borderwidth=5)
            lbl_y.pack(side=RIGHT,pady=1)
            lbl_y_distance.pack(side=LEFT)

        #for Z-Axis
            display_frame_z=Frame(display_frame)
            display_frame_z.pack(side=BOTTOM)
            lbl_z_distance=Label(display_frame_z,
                                text="Z Axis", 
                                background="Black",
                                fg="White",
                                font=("courier",18,"bold"),
                                justify=CENTER)
            lbl_z=Label(display_frame_z,
                                text=str(np.round(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)),
                                background='white',
                                fg="black",
                                font=("courier",18,"bold"),
                                justify=CENTER,
                                width=20,
                                borderwidth=5)
            lbl_z.pack(side=RIGHT,pady=1)
            lbl_z_distance.pack(side=LEFT)


            # get the current working directory
            cw_dir=os.getcwd()
            img_dir=cw_dir+r"/images/direction.png"
            

            #frames
            direction_frame=Frame(main_frame)
            direction_frame.pack(side=LEFT,expand=YES,fill=BOTH)
            #for speed entry
            speed_entry=speedentry(direction_frame)
            #icn for direction button
            direction_img=Image.open(img_dir)
            direction_img=direction_img.resize((50,50),Image.ANTIALIAS)
            
            #for up button
            def direction_up():
                travel_val=speed_entry.entr_speed.get()
                try:
                    if radio_btn.var.get()==0:
                        axis_x.move_absolute(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                        #print("Absolute")
                    elif radio_btn.var.get()==1:
                        axis_x.move_relative(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                    
                except CommandFailedException:
                    showerror("Out of Range","Travel is Out of Range!!")
                distance_trv=np.round(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)
                lbl_x.config(text=distance_trv)
                #print(distance_trv)


            up_frame=Frame(direction_frame)
            up_frame.pack(side=TOP)
            
            up_icn=direction_img.rotate(270)
            up_icn=ImageTk.PhotoImage(up_icn)
            btn_up=Button(up_frame,image=up_icn,command=direction_up,borderwidth=0)
            btn_up.pack(side=TOP)

            #for left button
            def direction_left():
                travel_val=speed_entry.entr_speed.get()
                try:
                    if radio_btn.var.get()==0:
                        axis_y.move_absolute(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                        #print("Absolute")
                    elif radio_btn.var.get()==1:
                        axis_y.move_relative(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                    #print("Relative")
                #distance_trv=Decimal(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES))
                except CommandFailedException:
                    showerror("Out of Range","Travel is Out of Range!!")
                distance_trv_lft=np.round(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)
                lbl_y.config(text=distance_trv_lft)
                #print(distance_trv_lft)
            
            left_frame=Frame(direction_frame)
            left_frame.pack(side=TOP)

            lft_icn=ImageTk.PhotoImage(direction_img)
            btn_lft=Button(left_frame,image=lft_icn,command=direction_left,borderwidth=0)
            btn_lft.pack(side=LEFT,padx=10)

            #for right button
            def direction_right():
                travel_val=speed_entry.entr_speed.get()
                try:
                    if radio_btn.var.get()==0:
                        axis_y.move_absolute(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                        #print("Absolute")
                    elif radio_btn.var.get()==1:
                        axis_y.move_relative(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                except CommandFailedException:
                    showerror("Out of Range","Travel is Out of Range!!")
                distance_trv_lft=np.round(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)
                lbl_y.config(text=distance_trv_lft)
                #print(distance_trv_rht)

            direction_img=direction_img.rotate(180)
            right_icn=ImageTk.PhotoImage(direction_img)
            btn_right=Button(left_frame,image=right_icn,command=direction_right,borderwidth=0)
            btn_right.pack(side=RIGHT,padx=10)
            
            #for down Button
            def direction_down():

                travel_val=speed_entry.entr_speed.get()
                try:
                    if radio_btn.var.get()==0:
                        axis_x.move_absolute(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                        #print("Absolute")
                    elif radio_btn.var.get()==1:
                        axis_x.move_relative(np.round((-1*float(travel_val)),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                    #print("Relative")
                except CommandFailedException:
                    showerror("Out of Range","Travel is Out of Range!!")
                distance_trv=np.round(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)
                lbl_x.config(text=distance_trv)
                #print(distance_trv_dwn)
            
            dwn_frame=Frame(direction_frame)
            dwn_frame.pack(side=TOP)

            direction_img=direction_img.rotate(270)
            dwn_icn=ImageTk.PhotoImage(direction_img)
            btn_dwn=Button(dwn_frame,image=dwn_icn,command=direction_down,borderwidth=0)
            btn_dwn.pack(side=TOP)
            
            #direction frames for z buttons
            #frames
            direction_frame_z=Frame(main_frame)
            direction_frame_z.pack(side=RIGHT,expand=YES,fill=BOTH)
            #for speed entry
            speed_entry_z=speedentry(direction_frame_z)
            


            def direction_up_z():
                travel_val=speed_entry_z.entr_speed.get()
                try:
                    if radio_btn.var.get()==0:
                        axis_z.move_absolute(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                        #print("Absolute")
                    elif radio_btn.var.get()==1:
                        axis_z.move_relative(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                except CommandFailedException:
                    showerror("Out of Range","Travel is Out of Range!!")
                distance_trv_z=np.round(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)
                lbl_z.config(text=distance_trv_z)
                #print(distance_trv_z)


            up_z_frame=Frame(direction_frame_z)
            up_z_frame.pack(side=TOP)
            
            btn_up_z=Button(up_z_frame,image=up_icn,command=direction_up_z,borderwidth=0)
            btn_up_z.pack(side=TOP)
            
            #for down Button
            def direction_down_z():
                global distance_trv_z
                travel_val=speed_entry_z.entr_speed.get()
                try:
                    if radio_btn.var.get()==0:
                        axis_z.move_absolute(np.round(float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES,wait_until_idle=TRUE)
                        #print("Absolute")
                    elif radio_btn.var.get()==1:
                        axis_z.move_relative(np.round(-1*float(travel_val),decimals=5), Units.LENGTH_MILLIMETRES, wait_until_idle=TRUE)
                        #print("Relative")
                except CommandFailedException:
                    showerror("Out of Range","Travel is Out of Range!!")
                distance_trv_z=np.round(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES),decimals=5)
                lbl_z.config(text=distance_trv_z)
                #print(distance_trv_z)
            
            dwn_z_frame=Frame(direction_frame_z)
            dwn_z_frame.pack(side=TOP)

            btn_z_dwn=Button(dwn_z_frame,image=dwn_icn,command=direction_down_z,borderwidth=0)
            btn_z_dwn.pack(side=TOP)
            radio_btn=radio_motion(frame_ab_rel)


            #pump buttons 
            var_pump_state_1=int(0)
            var_pump_state_2=int(0)

            #Frame
            lbl_frame_tb2=Frame(root)
            lbl_frame_tb2.pack()

            #image COnfiguration
            off_image=Image.open(cw_dir+r"\images\off.png")
            off_image = off_image.resize((50,50), Image.ANTIALIAS)                        #off button
            off_icn=ImageTk.PhotoImage(off_image)

            on_image=Image.open(cw_dir+"\images\on.png")
            on_image = on_image.resize((50,50), Image.ANTIALIAS)                        #on button
            on_icn=ImageTk.PhotoImage(on_image)


            def state_pump():
                global var_pump_state_1
                if var_pump_state_1==1:
                    btn_pump_1.config(image=off_icn)
                    var_pump_state_1=0
                    device.io.set_digital_output(1, var_pump_state_1)
                    lbl_pump_1.config(text="Pump One: Off")
                    #print(var_pump_state_1)
                else: 
                    var_pump_state_1=1
                    device.io.set_digital_output(1, var_pump_state_1)
                    lbl_pump_1.config(text="Pump One: On")
                    btn_pump_1.config(image=on_icn)
                    #print(var_pump_state_1)

            def state_pump_2():
                global var_pump_state_2
                if var_pump_state_2==1:
                    btn_pump_2.config(image=off_icn)
                    var_pump_state_2=0
                    device.io.set_digital_output(2, var_pump_state_2)
                    lbl_pump_2.config(text="Pump Two: Off")
                    #print(var_pump_state_2)
                else: 
                    var_pump_state_2=1
                    device.io.set_digital_output(2, var_pump_state_2)
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

            #Gcode
            frame_gcode=Frame(root,border=2,highlightbackground="Black",highlightthickness=1)
            frame_gcode.pack(side=TOP)
            gcode(frame_gcode)
                                    #speed frame
            frame_speed_select=Frame(root,borderwidth=1)
            frame_speed_select.pack(side=TOP)
            entry_1=speed_label(frame_speed_select)
            root.mainloop()
    except NameError:
        showerror("Cannot Proceed","You did not select any port. Cannot proceed further.\n Closing Program")
        sys.exit()
    
    



        
