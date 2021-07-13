import tkinter as tk
window=tk.Tk()
for i in range(3):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=2,minsize=50)

    for j in range(3):
        frame=tk.Frame(
            master=window,
            relief=tk.SUNKEN,
            borderwidth=1
        )

        frame.grid(row=i,column=j,padx=5,pady=5)

        lbl_name=tk.Label(master=frame,text=f"Row{i},\ncolumn{j}")
        lbl_name.pack(padx=5,pady=5)

window.mainloop()