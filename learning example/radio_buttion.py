from tkinter import *
from tkinter.messagebox import *
from zaber_motion.ascii import Connection
from zaber_motion.exceptions.connection_failed_exception import ConnectionFailedException


port=('COM1',"COM2","COM3","COM4","COM5")
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
            with Connection.open_serial_port("COM3") as connection:
                device_list = connection.detect_devices()
                showinfo('Device Found', "Found {} devices".format(len(device_list)))
        except ConnectionFailedException:
            showerror("Device Not Found","Zaber Device was not Found")
    
    def select(self):
        showinfo('Selected',"{} Port Selected".format(self.var.get()))
        global port_select
        port_select=self.var.get()
        self.destroy()

''' def select(self): This is to check the connection
        try:
            with Connection.open_serial_port("COM3") as connection:
                device_list = connection.detect_devices()
                showinfo("Selected","{} Port Selected".format(self.var.get()))
                global port_select
                port_select=self.var.get()
                self.destroy()

        except ConnectionFailedException:
            showerror("Device Not Found","Zaber Device was not Found")
       
'''
if __name__=='__main__':
    root=Tk()
    radio_bar()
    with Connection.open_serial_port(port_select) as connection:
        Button(root,text='Try to Press this').pack(side=TOP)
    
        print(port_select)
    root.mainloop()
    



        
