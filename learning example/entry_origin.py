from tkinter import *
from tkinter import filedialog as fd
from tkinter import font
from tkinter.messagebox import showerror, showinfo
from tkinter import ttk
from turtle import right
from PIL import Image, ImageTk
from os import *

class frame_entry(Frame):
    def __init__ (self,axis,parent=None):
        Frame.__init__(self,parent)
        self.pack(side=TOP)
        self.pack(side=TOP)
        self.axis=axis
        self.text="{} Axis Origin:".format(axis)
        self.lbl_axis=Label(self,text=self.text,font=("helvetica",12,"bold"))
        self.entr_val=Entry(self,width=5,borderwidth=2)
        self.entr_val.insert(0,"0")
        self.lbl_axis.pack(side=LEFT)
        self.entr_val.pack(side=RIGHT)
        

class origin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        frame_x=Frame(self)
        frame_x.pack(side=TOP)
        frame_y=Frame(self)
        frame_y.pack(side=TOP)
        frame_z=Frame(self)
        frame_z.pack(side=TOP)
        self.entr_x=frame_entry("X",frame_x)
        self.entr_y=frame_entry("Y",frame_y)
        self.entr_z=frame_entry("Z",frame_z)
        Button(self,text="Select",command=self.select).pack(side=RIGHT,expand=YES,fill=Y,anchor="e")
        Button(self,text="RESET",command=self.reset).pack(side=LEFT,expand=YES,fill=Y,anchor="w")

    

    def select(self):
        global translate_x, translate_y, translate_z
        translate_x= self.entr_x.entr_val.get()
        translate_y= self.entr_y.entr_val.get()
        translate_z=self.entr_z.entr_val.get()
        self.entr_x.entr_val.config(state=DISABLED)
        self.entr_z.entr_val.config(state=DISABLED)
        self.entr_y.entr_val.config(state=DISABLED)
        print(" X Axis Origin:{},\t Y Axis Origin:{},\tZ Axis Origin:{},".format(translate_x, translate_y, translate_z))

    def reset(self):
        self.entr_x.entr_val.config(state=NORMAL)
        self.entr_z.entr_val.config(state=NORMAL)
        self.entr_y.entr_val.config(state=NORMAL)

def select_file():
    global filename
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    entr_file.insert(END, filename)
    showinfo(
        title='Selected File',
        message=filename
    )

def browsefunc():
    location_dir =fd.askdirectory()
    entr_file_location.insert(END, location_dir)
    showinfo(
        title='Directory Selected',
        message=location_dir
    )

def run():
    if origin_widgets.entr_x.entr_val["state"]=="normal":
        showerror("Insufficient Info","Cannot Proceed Further")
    elif not entr_file.get():
        showerror("Insufficient Info","Cannot Proceed Further")
    elif not entr_file_location.get():
        showerror("Insufficient Info","Cannot Proceed Further")
    elif not entr_file_name:
        file_name="g_code_translated"
    else:
        print("Y State:",origin_widgets.entr_y.entr_val.get())
        print("Z State:",origin_widgets.entr_z.entr_val.get())
        print("Z State:",origin_widgets.entr_z.entr_val.get())
        print("File Location:",entr_file.get())
        print("Save Location:",entr_file_location.get())
    

if __name__=="__main__":
    cw_dir=getcwd()
    img_dir=cw_dir+r"/tkinter/images/browse-folder.png"
    browse_img=Image.open(img_dir)


    root=Tk()
    frame_try=Frame(root)
    browse_img=browse_img.resize((50,50),Image.ANTIALIAS)
    browse_icn=ImageTk.PhotoImage(browse_img)
    frame_try.pack()
    origin_widgets=origin(frame_try)
    
    frame_file_location=Frame(root)
    frame_file_location.pack(side=TOP)
    lbl_locate_file=Label(frame_file_location,
                    text="Select File",
                    font=("helvetica",15,"bold")
)
    lbl_locate_file.pack(side=TOP,fill="y",anchor="n")
    entr_file=Entry(frame_file_location,
              font=12
)
    entr_file.pack(side=LEFT,fill="x",anchor="e")
    open_button = Button(
                frame_file_location,
                text='Select File',
                image=browse_icn,
                borderwidth=0,
                command=select_file
    )

    open_button.pack(side=RIGHT,fill="x",anchor="w")

    frame_save_location=Frame(root)
    frame_save_location.pack(side=TOP)
    frame_file_save=Frame(frame_save_location)
    frame_file_save.pack(side=TOP)
    lbl_save_file=Label(frame_file_save,
                    text="Select Directory",
                    font=("helvetica",15,"bold")
)
    lbl_save_file.pack(side=TOP)
    entr_file_location=Entry(frame_file_save,
                        font=12
)
    entr_file_location.pack(side=LEFT,fill="x",anchor="e")


    btn_browse=Button(frame_file_save,
                text="Browse",
                image=browse_icn,
                font=("helvetica",12,"bold"),
                borderwidth=0,command=browsefunc
)
    btn_browse.pack(side=RIGHT,fill="x",anchor="w")
    frame_filename=Frame(frame_save_location)
    frame_filename.pack(side=BOTTOM)
    lbl_filename=Label(frame_filename,text="File Name",font=("helvetica",9))
    lbl_filename.pack(side=RIGHT,fill="x",anchor="w")
    entr_file_name=Entry(frame_filename,font=9)
    entr_file_name.pack(side=LEFT,fill="x",anchor="e")
    
    frame_run_btn=Frame(root)
    frame_run_btn.pack(side=TOP)
    btn_run=Button(frame_run_btn,text="RUN",command=run)
    btn_run.pack(side=TOP,fill="x",anchor="center")

    mainloop()
