from tkinter import *
from tkinter import ttk
from random import randint

root=Tk()
root.geometry("200x200")
a=randint(0,5)
var_show=StringVar()
lbl_show=Label(root,textvariable=var_show)

p_bar=ttk.Progressbar(root,orient=HORIZONTAL,length=150)

e_user=Entry(root)

btn=Button(root,text="send")

#=============pack=============
lbl_show.pack()
p_bar.pack(pady=15)
e_user.pack(pady=15)
btn.pack()

root.mainloop()