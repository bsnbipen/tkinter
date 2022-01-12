from tkinter import *
from tkinter import font
from os import *
from PIL import Image, ImageTk



class speedentry(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.entr_speed=Entry(self,width=5,borderwidth=3)
        self.entr_speed.insert(0,"5")
        self.lbl_speed=Label(self,text="Travel(MM):",font=('courier','12','bold'))
        self.entr_speed.pack(side=RIGHT,expand=YES,fill=BOTH)
        self.lbl_speed.pack(side=LEFT,expand=YES,fill=BOTH)


if __name__=="__main__":
    root=Tk()
    
    #travel distance variables
    distance_trv=1
    distance_trv_lft=1
    distance_trv_rht=1
    distance_trv_dwn=1

    #for distance display
    display_frame=Frame(root)
    display_frame.pack(side=TOP)
    lbl_x=Label(display_frame,
                        text=str(distance_trv),
                        background='white',
                        fg="black",
                        font=("courier",18,"bold"),
                        justify=CENTER,
                        width=20,
                        borderwidth=5)

    lbl_y=Label(display_frame,
                        text=str(distance_trv_lft),
                        background='white',
                        fg="black",
                        font=("courier",18,"bold"),
                        justify=CENTER,
                        width=20,
                        borderwidth=5)

    lbl_z=Label(display_frame,
                        text=str(distance_trv_rht),
                        background='white',
                        fg="black",
                        font=("courier",18,"bold"),
                        justify=CENTER,
                        width=20,
                        borderwidth=5)

    lbl_x.pack(side=TOP,pady=1)
    lbl_y.pack(side=BOTTOM,pady=2)
    lbl_z.pack(side=BOTTOM,pady=1)
    #for speed entry
    speed_entry=speedentry(root)
    # get the current working directory
    cw_dir=getcwd()
    img_dir=cw_dir+r"/images/direction.png"
    
    #travel distance variables
    distance_trv=1
    distance_trv_lft=1


    #frames
    direction_frame=Frame(root)
    direction_frame.pack(expand=YES,fill=BOTH)
    
    #icn for direction button
    direction_img=Image.open(img_dir)
    direction_img=direction_img.resize((50,50),Image.ANTIALIAS)
    
    #for up button
    def direction_up():
        global distance_trv
        travel_val=speed_entry.entr_speed.get()
        distance_trv=float(travel_val)+distance_trv
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
        distance_trv_lft=distance_trv_lft-float(travel_val)
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
        distance_trv_lft=float(travel_val)+distance_trv_lft
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
        distance_trv=distance_trv-float(travel_val)
        lbl_x.config(text=distance_trv)
        print(distance_trv_dwn)
    
    dwn_frame=Frame(direction_frame)
    dwn_frame.pack(side=TOP)

    direction_img=direction_img.rotate(270)
    dwn_icn=ImageTk.PhotoImage(direction_img)
    btn_dwn=Button(dwn_frame,image=dwn_icn,command=direction_down,borderwidth=0)
    btn_dwn.pack(side=TOP)
    mainloop()
