import decimal
from tkinter import *
from tkinter import font
from os import *
from PIL import Image, ImageTk
from decimal import *
import numpy as np

getcontext().prec=5
class speedentry(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.entr_speed=Entry(self,width=10,borderwidth=3)
        self.entr_speed.insert(0,"5")
        self.lbl_speed=Label(self,text="Travel(MM):",font=('courier','12','bold'))
        self.entr_speed.pack(side=RIGHT,expand=YES,fill=BOTH)
        self.lbl_speed.pack(side=LEFT,expand=YES,fill=BOTH)


if __name__=="__main__":
    root=Tk()
    main_frame=Frame(root)
    main_frame.pack()
    #travel distance variables
    distance_trv=1
    distance_trv_lft=1
    distance_trv_rht=1
    distance_trv_dwn=1

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
    cw_dir=getcwd()
    img_dir=cw_dir+r"/images/direction.png"
    
    #travel distance variables
    distance_trv=1
    distance_trv_lft=1
    #for up button Z axis
    distance_trv_z=0

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
        global distance_trv
        travel_val=speed_entry.entr_speed.get()
        distance_trv=np.float32(travel_val)+np.float32(distance_trv)
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
        global distance_trv_lft
        travel_val=speed_entry.entr_speed.get()
        distance_trv_lft=distance_trv_lft-np.around(travel_val)
        lbl_y.config(text=distance_trv_lft)
        print(distance_trv_lft)
    
    left_frame=Frame(direction_frame)
    left_frame.pack(side=TOP)

    lft_icn=ImageTk.PhotoImage(direction_img)
    btn_lft=Button(left_frame,image=lft_icn,command=direction_left,borderwidth=0)
    btn_lft.pack(side=LEFT,padx=10)

    #for right button
    def direction_right():
        global distance_trv_lft
        travel_val=speed_entry.entr_speed.get()
        distance_trv_lft=Decimal(travel_val)+Decimal(distance_trv_lft)
        lbl_y.config(text=distance_trv_lft)
        print(distance_trv_rht)

    direction_img=direction_img.rotate(180)
    right_icn=ImageTk.PhotoImage(direction_img)
    btn_right=Button(left_frame,image=right_icn,command=direction_right,borderwidth=0)
    btn_right.pack(side=RIGHT,padx=10)
    
    #for down Button
    def direction_down():
        global distance_trv
        travel_val=speed_entry.entr_speed.get()
        distance_trv=np.float32(distance_trv)-np.float32(travel_val)
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
        global distance_trv_z
        travel_val=speed_entry_z.entr_speed.get()
        distance_trv_z=np.float32(travel_val)+np.float32(distance_trv_z)
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
        distance_trv_z=np.float32(distance_trv_z)-np.float32(travel_val)
        lbl_z.config(text=distance_trv_z)
        print(distance_trv_dwn)
    
    dwn_z_frame=Frame(direction_frame_z)
    dwn_z_frame.pack(side=TOP)

    btn_z_dwn=Button(dwn_z_frame,image=dwn_icn,command=direction_down_z,borderwidth=0)
    btn_z_dwn.pack(side=TOP)

    mainloop()
