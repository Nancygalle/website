print("welcome to database")
from tkinter import *
import mysql.connector
from p101 import *
from p11 import *
from p15 import *
from p13 import *
from p16 import *

def dispcmaster():
    #mroot.withdraw()
    obj=cmaster()
    

def dispform():
    obj1=cmaster1()

def dispcourse():
    obj3=cmaster3()

def dispstudent():
    obj4=cmaster5()

def dispfee():
    obj2=cmaster4()


def dell():
     t1.delete(0,END)
     t2.delete(0,END)



def save():
    a=t1.get()
    b=t2.get()

    s1="select count(*) from login where userid='{0}' and password='{1}'".format(a,b)
    #print(s1)
    cur.execute(s1)
    r=cur.fetchone()
    if(r[0]>0):
       # showinfo(title="Message for you", message="Login sucessfully")
       disp()        
    else:
        showinfo(title="Message for you", message="Invalid")


def disp():
    b1.destroy()
    b2.destroy()
    lb1.destroy()
    lb2.destroy()
    t1.destroy()
    t2.destroy()
    lb.config(text="Welcome to Admin",bg="salmon",font=("Verdana",30,"bold"))

    b3=Button(text="Course Master",bg="darkcyan",font=("Comic Sans MS",30,"bold"),command=dispcmaster)
    b4=Button(text="Addmission Form",bg="darkcyan",font=("Comic Sans MS",30,"bold"),command=dispform)
    b5=Button(text="Fee Receipt",bg="darkcyan",font=("Comic Sans MS",30,"bold"),command=dispfee)
    b6=Button(text="Course Detail",bg="darkcyan",font=("Comic Sans MS",30,"bold"),command=dispcourse)
    b7=Button(text="Addmission detail",bg="darkcyan",font=("Comic Sans MS",30,"bold"),command=dispstudent)
    
    b3.place(x=150,y=200,width=400,height=50)
    b4.place(x=200,y=300,width=400,height=50)
    b5.place(x=350,y=400,width=400,height=50)
    b6.place(x=450,y=500,width=400,height=50)
    b7.place(x=550,y=600,width=400,height=50)




mroot=Tk()
mroot.geometry("1000x1000")
mroot.config(bg="moccasin")
conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
cur=conn.cursor()
''''

'''


lb=Label(text="School Management System",bg="darkcyan",font=("Comic Sans MS",30,"bold"))
lb1=Label(text="User ID",bg="lightsalmon",font=("Verdana",15,"bold"))
lb2=Label(text="Password",bg="lightsalmon",font=("Verdana",15,"bold"))

b1=Button(text="Login",bg="darkcyan",font=("Comic Sans MS",20,"bold"),command=save)
b2=Button(text="Cancel",bg="darkcyan",font=("Comic Sans MS",20,"bold"),command=dell)


lb.place(x=100,y=50,width=800,height=100)

lb1.place(x=300,y=250,width=150,height=30)
t1=Entry()
t1.place(x=500,y=250,width=300,height=30)
lb2.place(x=300,y=350,width=150,height=30)
t2=Entry(show="*")
t2.place(x=500,y=350,width=300,height=30)


b1.place(x=350,y=450,width=150,height=40)
b2.place(x=550,y=450,width=150,height=40)

'''
lb.place(x=100,y=50,width=800,height=100)

b1.place(x=200,y=250,width=250,height=30)
b2.place(x=200,y=350,width=250,height=30)
b3.place(x=350,y=450,width=250,height=30)
b4.place(x=500,y=250,width=250,height=30)
b5.place(x=500,y=350,width=250,height=30)

'''
















mainloop()


