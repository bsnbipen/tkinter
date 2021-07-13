import tkinter as tk
window=tk.Tk()

frame_1=tk.Frame(master=window,width=200,height=200,bg="red")
frame_1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame_2=tk.Frame(master=window,width=200,bg="pink")
frame_2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame_3=tk.Frame(master=window,width=200,bg="blue")
frame_3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

window.mainloop()