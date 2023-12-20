from tkinter import*
root=Tk()
def add():
    c=int(txt1.get())+int(txt2.get())
    txt3.insert(0,c)
def sub():
    d=int(txt1.get())-int(txt2.get())
    txt3.insert(0,d)

def mul():
    e=int(txt1.get())*int(txt2.get())
    txt3.insert(0,e)
def div():
    f= first=int(txt1.get())/int(txt2.get())
    txt3.insert(0,f)
def clear():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)

root.geometry("500x500")
root.title("Application")
lbl=Label(text="Enter first number  :")
lbl.place(x=50,y=50)
lbl2=Label(text="Enter second number  :")
lbl2.place(x=50,y=100)

txt1=Entry()
txt1.place(x=200,y=50)
txt2=Entry()
txt2.place(x=200,y=100)

btn=Button(text="SUM",command=add)
btn.place(x=150,y=150)

txt3=Entry()
txt3.place(x=150,y=200)

btn=Button(text="SUB",command=sub)
btn.place(x=200,y=150)

btn=Button(text="MUL",command=mul)
btn.place(x=250,y=150)

btn=Button(text="DIV",command=div)
btn.place(x=300,y=150)

btn=Button(text="CLEAR",command=clear)
btn.place(x=350,y=150)

root.mainloop()