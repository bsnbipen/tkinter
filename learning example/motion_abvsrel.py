from tkinter import *
from tkinter.messagebox import *
from zaber_motion.ascii import Connection
from zaber_motion.exceptions.connection_failed_exception import ConnectionFailedException

# to travel in abosolute or relative



#
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
      
        

#main frame
if __name__=="__main__":
    root=Tk()
    frame_ab_rel=Frame(root)
    frame_ab_rel.pack()
    radio_btn=radio_motion(frame_ab_rel)
    root.mainloop()
    print(radio_btn.var.get())


