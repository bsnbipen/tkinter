import tkinter as tk

window=tk.Tk()

ent_name=tk.Entry(text="What is your name",
                 fg="Black",bg="White",
                 width=40)
ent_name.insert(0,"What is your name?")
ent_name.pack()
window.mainloop()
