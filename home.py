from tkinter import *
from tkinter import ttk
import math

pi=math.pi
win=Tk()
win.title('simple prime number')
main=Frame(win)
win.geometry("700x350")


def forget():
        for i in options:
                if clicked.get() == 'cone':
                        myButton1['state'] = NORMAL
                        a.place_forget()
                        myDel2.place_forget()
                        myButton23.place_forget()
                        mylabel.place_forget()
                        b.place_forget()
                        wlabel.place_forget()
                else:
                        myButton1['state'] = NORMAL
                        a.place_forget()
                        myDel2.place_forget()
                        myButton23.place_forget()
                        mylabel.place_forget()
                        wlabel.place_forget()                        


def cal_cone():
       global wlabel
       t1=int(a.get())
       t2=int(b.get())
       myButton23['state'] = DISABLED
       t3=(1/3)*pi*t1*t1*t2
       
       
       if t1>0 and t2 >0:
                wlabel.config(text=t3)
                wlabel.place(x=305, y=211)
       else:
               wlabel = Label(win, text="Please input with right minimum number")
               wlabel.place(x=255, y=211)

               
def cal_ball():
       global wlabel
       t1=int(a.get())
       myButton23['state'] = DISABLED
       t3=(4/3)*pi*t1**3
       
       
       if t1>0 :
                
                wlabel.config(text=t3)
                wlabel.place(x=305, y=211)
       else:
               wlabel = Label(win, text="Please input with right minimum number")
               wlabel.place(x=255, y=211)
               
       
def myDel(): 
    wlabel.place_forget()
    myButton23['state'] = NORMAL      

           
def show():
    global mylabel
    global a
    global myButton23
    global myDel2
    global b
    global wlabel
         
    for i in options:
        if clicked.get() == 'cone':
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="Volume Cone")
                mylabel.place(x=315, y=125)
                a=Entry(win, width=21)
                a.place(x=200, y=155)
                b=Entry(win, width=22)
                b.place(x=375, y=155)
                myDel2 = Button(win, text="CLEAR VOLUME CONE", command=myDel)
                myDel2.place(x=200, y=178)
                myButton23 = Button(win,width=18, text="calculate", command=cal_cone , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")
                break
                
        else:
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="Volume Sphere or Ball")
                mylabel.place(x=305, y=125)
                a=Entry(win, width=29)
                a.place(x=275, y=155)
                myDel2 = Button(win, text="CLEAR VOLUME CONE", command=myDel)
                myDel2.place(x=210, y=178)
                myButton23 = Button(win,width=18, text="calculate", command=cal_ball , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")
                break
            

            

options =[
    "cone",
    "Ball"
    ]

clicked = StringVar()
clicked.set(options[0])
Label(win, text="Enter Number", font=('Calibri 10')).place(x=315, y=5)
drop = ttk.Combobox(win, width = 27, textvariable = clicked, value=options)
drop.place(x=265, y=35)


myButton1 = Button(win, text="Show Selection", command=show)
myButton1.place(x=265, y=61)
myButton2 = Button(win,width=11, text="delete con", command=forget)
myButton2.place(x=365, y=61)


win.mainloop()
