from tkinter import *

win=Frame()
win.pack(expand=YES,fill=BOTH)
Button(win,text="Quit").pack(side=LEFT, anchor=N)
Label(win,text="I am here second").pack(side=TOP)
Button(win,text="Press Me").pack(side=BOTTOM)
win.mainloop()