from tkinter import *
from tkinter import messagebox

def ok():
    uname = e1.get()
    password = e2.get()
    if uname == "" and password == "":
        messagebox.showinfo("", "Blank not allowed")
    elif uname == "Admin" and password == "123":
        messagebox.showinfo("", "Login Success")
        root.destroy()
    else:
        messagebox.showinfo("", "Incorrect username or password")
root =Tk()
root.title("LOGIN")
root.geometry("300x200")
# bg = PhotoImage(file = "pngtree.JPG")
# label1 = Label( root, image = bg)
# label1.place(x = 0, y = 0)
global e1
global e2
Label(root, text="Username:").place(x=10, y=10)
Label(root, text="password:").place(x=10, y=40)
e1 = Entry(root)
e1.place(x=90, y=10)
e2 = Entry(root)
e2.place(x=90, y=40)
e2.config(show="*")
Button(root, text="Login", command=ok, height=2, width=10).place(x=10, y=100)
root.mainloop()
class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
   def displayStudent(self):
       print ("name:", self.firstname, "lname:", self.lastname, "age:", self.age, "section:", self.section)
# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")
stu1.displayStudent()