from cgitb import text
from json.tool import main
from tkinter import *
import os
from tkinter.messagebox import *
from zaber_motion import Units
from zaber_motion.ascii import Connection
from zaber_motion.exceptions.no_device_found_exception import NoDeviceFoundException
import sys
from PIL import Image, ImageTk
from decimal import *
from tkinter import ttk

port=('COM1',"COM2","COM3","COM4","COM5","COM6")

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
            #notebook
            notebook=ttk.Notebook(root)
            notebook.pack(pady=10,expand=True)
            
            main_frame=Frame(notebook)
            main_frame.pack(fill="Both",expand=YES)
            main_frame_2=Frame(notebook)
            main_frame_2.pack(fill="Both",expand=YES)
            notebook.add(main_frame,text="Stage and Pump Control")
            notebook.add(main_frame_2,text="G-Code Translation")

            frame_ab_rel=Frame(root)
            frame_ab_rel.pack()
            #travel distance variables
            distance_trv=1
            distance_trv_lft=1
            distance_trv_rht=1
            distance_trv_dwn=1
            #axis
            device_list = connection.detect_devices()
            device = device_list[0]
            
            #naming axis
            axis_x = device.get_axis(2)
            axis_y=device.get_axis(3)
            axis_z=device.get_axis(1)

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
                                text=str(distance_trv),
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
                                text=str(distance_trv_lft),
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
                                text=str(distance_trv_rht),
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
            
            getcontext().prec=4

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
                if radio_btn.var.get()==0:
                    axis_x.move_absolute(float(Decimal(travel_val)), Units.LENGTH_MILLIMETRES)
                    print("Absolute")
                elif radio_btn.var.get()==1:
                    axis_x.move_relative(Decimal(travel_val), Units.LENGTH_MILLIMETRES)
                distance_trv=Decimal(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES))
                lbl_x.config(text=distance_trv)
                print(distance_trv)


            up_frame=Frame(direction_frame)
            up_frame.pack(side=TOP)
            
            up_icn=direction_img.rotate(270)
            up_icn=ImageTk.PhotoImage(up_icn)
            btn_up=Button(up_frame,image=up_icn,command=direction_up,borderwidth=0)
            btn_up.pack(side=TOP)

            #for left button
            def direction_left():
                travel_val=speed_entry.entr_speed.get()
                if radio_btn.var.get()==0:
                    axis_y.move_absolute(float(travel_val), Units.LENGTH_MILLIMETRES)
                    #print("Absolute")
                elif radio_btn.var.get()==1:
                    axis_y.move_relative(float(-1*float(travel_val)), Units.LENGTH_MILLIMETRES)
                    #print("Relative")
                #distance_trv=Decimal(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES))
                distance_trv_lft=Decimal(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES))
                lbl_y.config(text=distance_trv_lft)
                print(distance_trv_lft)
            
            left_frame=Frame(direction_frame)
            left_frame.pack(side=TOP)

            lft_icn=ImageTk.PhotoImage(direction_img)
            btn_lft=Button(left_frame,image=lft_icn,command=direction_left,borderwidth=0)
            btn_lft.pack(side=LEFT,padx=10)

            #for right button
            def direction_right():
                travel_val=speed_entry.entr_speed.get()
                if radio_btn.var.get()==0:
                    axis_y.move_absolute(float(travel_val), Units.LENGTH_MILLIMETRES)
                    print("Absolute")
                elif radio_btn.var.get()==1:
                    axis_y.move_relative(float(travel_val), Units.LENGTH_MILLIMETRES)
                distance_trv_lft=Decimal(axis_y.get_position(unit=Units.LENGTH_MILLIMETRES))
                lbl_y.config(text=distance_trv_lft)
                print(distance_trv_rht)

            direction_img=direction_img.rotate(180)
            right_icn=ImageTk.PhotoImage(direction_img)
            btn_right=Button(left_frame,image=right_icn,command=direction_right,borderwidth=0)
            btn_right.pack(side=RIGHT,padx=10)
            
            #for down Button
            def direction_down():

                travel_val=speed_entry.entr_speed.get()
                if radio_btn.var.get()==0:
                    axis_x.move_absolute(float(travel_val), Units.LENGTH_MILLIMETRES)
                    #print("Absolute")
                elif radio_btn.var.get()==1:
                    axis_x.move_relative(float(-1*float(travel_val)), Units.LENGTH_MILLIMETRES)
                    #print("Relative")
                distance_trv=Decimal(axis_x.get_position(unit=Units.LENGTH_MILLIMETRES))
                lbl_x.config(text=distance_trv)
                print(distance_trv_dwn)
            
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
                if radio_btn.var.get()==0:
                    axis_z.move_absolute(int(travel_val), Units.LENGTH_MILLIMETRES)
                    print("Absolute")
                elif radio_btn.var.get()==1:
                    axis_z.move_relative(float(travel_val), Units.LENGTH_MILLIMETRES)
                distance_trv_z=Decimal(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES))
                lbl_z.config(text=distance_trv_z)
                print(distance_trv_z)


            up_z_frame=Frame(direction_frame_z)
            up_z_frame.pack(side=TOP)
            
            btn_up_z=Button(up_z_frame,image=up_icn,command=direction_up_z,borderwidth=0)
            btn_up_z.pack(side=TOP)
            
            #for down Button
            def direction_down_z():
                global distance_trv_z
                travel_val=speed_entry_z.entr_speed.get()

                if radio_btn.var.get()==0:
                    axis_z.move_absolute(float(travel_val), Units.LENGTH_MILLIMETRES)
                    print("Absolute")
                elif radio_btn.var.get()==1:
                    axis_z.move_relative(float(-1*float(travel_val)), Units.LENGTH_MILLIMETRES)
                    print("Relative")
                
                distance_trv_z=Decimal(axis_z.get_position(unit=Units.LENGTH_MILLIMETRES))
                lbl_z.config(text=distance_trv_z)
                print(distance_trv_z)
            
            dwn_z_frame=Frame(direction_frame_z)
            dwn_z_frame.pack(side=TOP)

            btn_z_dwn=Button(dwn_z_frame,image=dwn_icn,command=direction_down_z,borderwidth=0)
            btn_z_dwn.pack(side=TOP)
            radio_btn=radio_motion(frame_ab_rel)
            root.mainloop()
    except NameError:
        showerror("Cannot Proceed","You did not select any port. Cannot proceed further.\n Closing Program")
        sys.exit()
    
    



        
