import tkinter as tk
from tkinter.constants import NW
window=tk.Tk()
window.columnconfigure(0,weight=1,minsize=75)
window.rowconfigure([0,1],weight=1,minsize=60)
lbl_a=tk.Label(text="A")
lbl_b=tk.Label(text="B")
lbl_a.grid(row=0,column=0,padx=5,pady=5,sticky="NE")
lbl_b.grid(row=1,column=0,padx=5,pady=5,sticky="NW")
window.mainloop()