from tkinter import *
root = Tk()
root.title("Simple Calculator")
str1 = ""
input1 = Entry(root,width=40)
input1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def num(number):


   global str1
   str1=str1+str(number)
   input1.delete(0,END)
   input1.insert(0,str1)
def addopr():
    global str1
    str1=str1+"+"
    input1.delete(0,END)
    input1.insert(0,str1)
def minusopr():
    global str1
    str1=str1+"-"
    input1.delete(0,END)
    input1.insert(0,str1)
def equalopr():
    global str1
    i=eval(str1)
    str1=str(i)
    input1.delete(0,END)
    input1.insert(0,str1)
def clearopr():
    global str1
    str1=""
    input1.insert(0,str1)
def leftbracket():
    global str1
    str1=str1+"("
    input1.delete(0,END)
    input1.insert(0,str1)
def rightbracket():
    global str1
    str1 = str1 + ")"
    input1.delete(0, END)
    input1.insert(0, str1)
def divide():
    global str1
    str1 = str1 + "/"
    input1.delete(0, END)
    input1.insert(0, str1)
def multiply():
    global str1
    str1 = str1 + "*"
    input1.delete(0, END)
    input1.insert(0, str1)
def decimal():
    global str1
    str1 = str1 + "."
    input1.delete(0, END)
    input1.insert(0, str1)
Button(root,text="(",command=leftbracket,padx=25,pady=15).grid(row=1,column=0)
Button(root,text="(",command=rightbracket,padx=25,pady=15).grid(row=1,column=1)
Button(root,text="/",command=divide,padx=25,pady=15).grid(row=1,column=2)
Button(root,text="*",command=multiply,padx=25,pady=15).grid(row=1,column=3)
Button(root,text="1",command=lambda: num(1),padx=25,pady=15).grid(row=4,column=0)
Button(root,text="2",command=lambda: num(2),padx=25,pady=15).grid(row=4,column=1)
Button(root,text="3",command=lambda: num(3),padx=25,pady=15).grid(row=4,column=2)
Button(root,text="4",command=lambda: num(4),padx=25,pady=15).grid(row=3,column=0)
Button(root,text="6",command=lambda: num(5),padx=25,pady=15).grid(row=3,column=1)
Button(root,text="6",command=lambda: num(6),padx=25,pady=15).grid(row=3,column=2)
Button(root,text="7",command=lambda: num(7),padx=25,pady=15).grid(row=2,column=0)
Button(root,text="8",command=lambda: num(8),padx=25,pady=15).grid(row=2,column=1)
Button(root,text="9",command=lambda: num(9),padx=25,pady=15).grid(row=2,column=2)
Button(root,text="0",command=lambda: num(0),padx=25,pady=15).grid(row=5,column=0)
Button(root,text="+",padx=25,pady=15,command=addopr).grid(row=2,column=3)
Button(root,text="-",padx=25,pady=15,command=minusopr).grid(row=3,column=3)
Button(root,text="=",padx=25,pady=42,command=equalopr).grid(row=4,column=3,rowspan=2)
Button(root,text="C",padx=25,pady=15,command=clearopr).grid(row=5,column=2,columnspan=1)
Button(root,text=".",padx=25,pady=15,command=decimal).grid(row=5,column=1)
root.mainloop()
