import tkinter as tk
window=tk.Tk()

frame_a=tk.Frame()
frame_b=tk.Frame()

label_a=tk.Label(master=frame_a,text="I am in the Frame A")
label_a.pack()

label_b=tk.Label(master=frame_b,text="I am in the Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()