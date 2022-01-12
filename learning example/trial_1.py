from tkinter import *

def fetch():
        print('Input=."%s"' %ent.get())

root=Tk()
ent=Entry(root)
ent.insert(0,'Type Words here')
ent.pack(side=TOP,fill=X)

ent.focus()
ent.bind('<Return>',(lambda event: fetch()))
btn=Button(root,text='Fetch',command=fetch)
btn.pack(side=LEFT)
root.mainloop()