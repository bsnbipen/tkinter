import tkinter as tk
window=tk.Tk()
window.title("Address Form Entry")
window.columnconfigure([0,1],weight=1)
window.rowconfigure([0,1,2,3,4,5,6,7],weight=1)

form_frame=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
form_frame.pack()

text_window=["First Name:","Last Name:","Address 1:","Address 2","City","Province/State","Postal Code","Country"]

for i in range(2):
    for j in range(8):
        if i ==0:
            lbl=tk.Label(master=form_frame,text=text_window[j])
            lbl.grid(row=j,column=i,stick="w")
        else:
            etr=tk.Entry(master=form_frame)
            etr.grid(row=j,column=i,sticky="w")
form_frame_button=tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
form_frame_button.pack(fill=tk.X)

btn_submit=tk.Button(master=form_frame_button,text="Submit")
btn_submit.pack(side=tk.RIGHT,ipadx=10)

btn_Clear=tk.Button(master=form_frame_button,text="Clear")
btn_Clear.pack(side=tk.RIGHT,ipadx=10)
window.mainloop()