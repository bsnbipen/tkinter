import tkinter as tk
window=tk.Tk()
window.title("Address From Entry")
window.columnconfigure([0,1],weight=1)
window.rowconfigure([0,1,2,3,4,5,6,7],weight=1)

text_window=["First Name:","Last Name:","Address 1:","Address 2","City","Province/State","Postal Code","Country"]

for i in range(2):
    for j in range(8):
        if i ==0:
            lbl=tk.Label(text=text_window[j])
            lbl.grid(row=j,column=i,stick="w")
        else:
            etr=tk.Entry()
            etr.grid(row=j,column=i,sticky="w")

window.mainloop()