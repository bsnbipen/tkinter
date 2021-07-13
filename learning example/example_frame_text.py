import tkinter as tk
border_effect={
    "flat":tk.FLAT,
    "raised":tk.RAISED,
    "sunken":tk.SUNKEN,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE
}

window=tk.Tk()

for relief_name,relief in border_effect.items():
    frame=tk.Frame(master=window,relief=relief,border=5)
    frame.pack(side=tk.RIGHT)
    label=tk.Label(master=frame,text=relief_name)
    label.pack()

window.mainloop()