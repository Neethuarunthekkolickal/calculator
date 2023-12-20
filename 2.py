from tkinter import*
root=Tk()
def clear():
    txt1.delete(0,END)
def clicked(n):
    first_value=txt1.get()
    txt1.delete(0,END)
    txt1.insert(0,str(first_value)+str(n)) 
def add():
    first_num=txt1.get()
    global old_value
    old_value=str(first_num)
    global math
    math="sum"
    txt1.delete(0,END)
def sub():
    first_num=txt1.get()
    global old_value
    old_value=str(first_num)
    global math
    math="sub"
    txt1.delete(0,END)
def mul():
    first_num=txt1.get()
    global old_value
    old_value=str(first_num)
    global math
    math="mul"
    txt1.delete(0,END)
def div():
    first_num=txt1.get()
    global old_value
    old_value=str(first_num)
    global math
    math="div"
    txt1.delete(0,END)

def equal():
    if math=="sum":
        new_value=str(txt1.get())
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)+int(new_value))
    elif math=="sub":
        new_value=str(txt1.get())
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)-int(new_value))
    elif math=="mul":
        new_value=str(txt1.get())
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)*int(new_value))
    elif math=="div":
        new_value=str(txt1.get())
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)/int(new_value))

root.geometry ("250x250")
root.title("Calculator")
lbl=Label(text="   ")
lbl.place(x=80,y=150)

txt1=Entry()
txt1.place(x=50,y=20)

btn7=Button(text="1",command=lambda:clicked("1"))
btn7.place(x=50,y=80)

btn8=Button(text="2",command=lambda:clicked("2"))
btn8.place(x=80,y=80)

btn9=Button(text="3",command=lambda:clicked("3"))
btn9.place(x=110,y=80)

btn10=Button(text="4",command=lambda:clicked("4"))
btn10.place(x=50,y=110)

btn11=Button(text="5",command=lambda:clicked("5"))
btn11.place(x=80,y=110)

btn12=Button(text="6",command=lambda:clicked("6"))
btn12.place(x=110,y=110)

btn13=Button(text="7",command=lambda:clicked("7"))
btn13.place(x=50,y=140)

btn14=Button(text="8",command=lambda:clicked("8"))
btn14.place(x=80,y=140)

btn15=Button(text="9",command=lambda:clicked("9"))
btn15.place(x=110,y=140)

btn16=Button(text="0",command=lambda:clicked("0"))
btn16.place(x=50,y=170)

btn17=Button(text="C",command =clear)
btn17.place(x=80,y=170)

btn18=Button(text="=",command=equal)
btn18.place(x=110,y=170)

btn19=Button(text="*",command=lambda:mul())
btn19.place(x=140,y=80)

btn20=Button(text="/",command=lambda:div())
btn20.place(x=140,y=110)

btn21=Button(text="-",command=lambda:sub())
btn21.place(x=140,y=140)

btn22=Button(text="+",command=lambda:add())
btn22.place(x=140,y=170)

btn23=Button(text="%")
btn23.place(x=50,y=50)

btn24=Button(text=".")
btn24.place(x=80,y=50)

btn25=Button(text="00",command=lambda:clicked("00"))
btn25.place(x=110,y=50)



root.mainloop()