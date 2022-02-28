import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
root=tkinter.Tk()
root.title("demo,combobox,scrolledtext")
root.geometry("600x600")
# #label
# label=(tkinter.Label(root,text="hi welcome",bg="red",fg="blue")).grid(column=6,row=10)
# #button
# b=Button(root,text="subscribe",bg="orange",fg="red")
# b.grid(column=1,row=0)
# #radio button
# r=Radiobutton(root,text="python",value=1)
# r.grid(column=3,row=3)
# r=Radiobutton(root,text="java",value=2)
# r.grid(column=3,row=4)
# r=Radiobutton(root,text="linux",value=3)
# r.grid(column=3,row=5)
# #entry
# t=Entry(root,width="20")
# t.grid(column=6,row=2)

#messagebox
# def Button1():
#     messagebox.showinfo("status","please subscribe")
# b=Button(root,text='python life',command=Button1)
# b.pack()
#combobox
ttk.Label(root,text="Pyhton life",background="pink",foreground="red").grid(column=2,row=2)
# n=tkinter.StringVar()
# course=ttk.Combobox(root,width=20,textvariable=n)
# course['values']=('python','java','machine learning')
# course.grid(column=3,row=3)
# course.current()
text1=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,width=50,heigh=20)
text1.grid(column=3,pady=10,padx=10)
text1.focus()
root.mainloop()
