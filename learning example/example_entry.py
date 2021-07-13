import tkinter as tk
window=tk.Tk()

frame_1=tk.Frame(master=window,height=40,bg="red")
frame_1.pack(fill=tk.X)

frame_2=tk.Frame(master=window,height=40,bg="pink")
frame_2.pack(fill=tk.X)

frame_3=tk.Frame(master=window,height=40,bg="yellow")
frame_3.pack(fill=tk.X)

window.mainloop()