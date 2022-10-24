4from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  
import math

pi=math.pi
win=Tk()
win.title('simple prime number')
main=Frame(win)
win.geometry("700x350")


bg= PhotoImage(file="images/haikal_ganteng2.png")
your_label=Label(win, image=bg)
your_label.place(x=0, y=0, relwidth=1,relheight=1)


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
                        my_label2.place_forget()
                        mylabelq.place_forget()
                        mylabels.place_forget()
                        
                elif clicked.get() == 'Beam':
                        myButton1['state'] = NORMAL
                        a.place_forget()
                        myDel2.place_forget()
                        myButton23.place_forget()
                        mylabel.place_forget()
                        b.place_forget()
                        c.place_forget()
                        wlabel.place_forget()
                        my_label2.place_forget()
                        mylabelq.place_forget()
                        mylabels.place_forget()
                        mylabelw.place_forget()
                else:
                        myButton1['state'] = NORMAL
                        a.place_forget()
                        myDel2.place_forget()
                        myButton23.place_forget()
                        mylabel.place_forget()
                        wlabel.place_forget()
                        my_label2.place_forget()


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


def cal_cube():
       global wlabel
       t1=int(a.get())
       myButton23['state'] = DISABLED
       t3=t1**3
       
       
       if t1>0 :
                
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

def cal_beam():
       global wlabel
       t1=int(a.get())
       t2=int(b.get())
       t4=int(c.get())
       myButton23['state'] = DISABLED
       t3=t1*t2*t4
       
       
       if t1>0 and t2 >0:
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
    global c
    global wlabel
    global my_label2
    global mylabelq
    global mylabels
    global mylabelw    
    
         
    for i in options:
        if  clicked.get() == 'cone':
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="Volume Cone",bg="yellow", fg="black")
                mylabel.place(x=315, y=125)
                mylabels = Label(win, text="r : ",bg="yellow", fg="black")
                mylabels.place(x=180, y=155)
                mylabelq = Label(win, text="h : ",bg="yellow", fg="black")
                mylabelq.place(x=350, y=155)
                a=Entry(win, width=21)
                a.place(x=200, y=155)
                b=Entry(win, width=22)
                b.place(x=375, y=155)
                myDel2 = Button(win, text="CLEAR VOLUME CONE", command=myDel)
                myDel2.place(x=200, y=178)
                my_label2 = Label(height=89,width=259,image=my_img)
                my_label2.place(x=225, y=238)
                myButton23 = Button(win,width=18, text="calculate", command=cal_cone , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")
                break
                
        elif clicked.get() == 'Cube':
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="Volume Cube")
                mylabel.place(x=305, y=125)
                a=Entry(win, width=29)
                a.place(x=275, y=155)
                myDel2 = Button(win, text="CLEAR VOLUME Cube", command=myDel)
                myDel2.place(x=210, y=178)
                my_label2 = Label(height=89,width=259,image=my_img4)
                my_label2.place(x=225, y=238)
                myButton23 = Button(win,width=18, text="calculate", command=cal_cube , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")
                break


        elif  clicked.get() == 'Beam':
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="Volume Cone",bg="yellow", fg="black")
                mylabel.place(x=315, y=125)
                mylabels = Label(win, text="P : ",bg="yellow", fg="black")
                mylabels.place(x=180, y=155)
                mylabelq = Label(win, text="L : ",bg="yellow", fg="black")
                mylabelq.place(x=350, y=155)
                mylabelw = Label(win, text="T : ",bg="yellow", fg="black")
                mylabelw.place(x=520, y=155)                
                a=Entry(win, width=21)
                a.place(x=200, y=155)
                b=Entry(win, width=22)
                b.place(x=375, y=155)
                c=Entry(win, width=22)
                c.place(x=545, y=155)                
                myDel2 = Button(win, text="CLEAR VOLUME BEAM", command=myDel)
                myDel2.place(x=200, y=178)
                my_label2 = Label(height=89,width=259,image=my_img3)
                my_label2.place(x=225, y=238)
                myButton23 = Button(win,width=18, text="calculate", command=cal_beam , bg="red", fg="white")
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
                my_label2 = Label(height=89,width=259,image=my_img2)
                my_label2.place(x=225, y=238)
                myButton23 = Button(win,width=18, text="calculate", command=cal_ball , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")
                break
                
            

            

options =[
    "cone",
    "Ball",
    "Cube",
    "Beam"
    ]

clicked = StringVar()
clicked.set(options[0])
Label(win, text="Enter Number", font=('Calibri 10'), bg="yellow", fg="black").place(x=315, y=5)
drop = ttk.Combobox(win, width = 27, textvariable = clicked, value=options)
drop.place(x=265, y=35)
my_img = ImageTk.PhotoImage(Image.open("images/popo.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/haikal_tampan.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/balok.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/kubus.png"))




myButton1 = Button(win, text="Show Selection", bg="red", fg="white", command=show)
myButton1.place(x=265, y=61)
myButton2 = Button(win,width=11, text="delete con", bg="pink", fg="white", command=forget)
myButton2.place(x=365, y=61)
exit_button = Button(win,width=5, text="Exit",bg="red", command=win.destroy)
exit_button.place(x=485, y=35)


win.mainloop()
