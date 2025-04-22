print ("Welcome to database with Tkinter")
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector

def new():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    t1.focus()

def dell():
    s1="delete from courses where cname='{}'".format(t2.get())
    cur.execute(s1)
    conn.commit()
    showinfo(title="Message for you", message="Delete sucessfully")

def mfy():
    s1="update courses set cname='{}',duration='{}',fees={} where ccode={}".format(t2.get(),t3.get(),t4.get(),t1.get())
    cur.execute(s1)
    conn.commit()
    showinfo(title="Message for you", message="Update sucessfully")



def sch(e):
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)    
    #print(cname.get())
    s1="select * from courses where cname='{}'".format(cname.get())
    cur.execute(s1)
    r=cur.fetchone()
    t1.insert(0,r[0])
    t2.insert(0,r[1])
    t3.insert(0,r[2])
    t4.insert(0,r[3])
            
def save():    
    a=t1.get()
    b=t2.get()
    c=t3.get()
    d=t4.get()
    s1="insert into courses values({0},'{1}','{2}',{3})".format(a,b,c,d)
    cur.execute(s1)
    conn.commit()
    showinfo(title="Message for you", message="Save sucessfully")

    #conn.close()

def disp():
    
    root1=Toplevel()
    root1.geometry("600x200")
    conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
    cur=conn.cursor()
    cur.execute("SELECT * FROM courses")
    data= cur.fetchall()
    dat=[["Ccode","Cname","Duration","Fees"]]
    for r in data:
        ls=[]
        ls.append(r[0])
        ls.append(r[1])
        ls.append(r[2])
        ls.append(r[3])
        dat.append(ls)
        

    #print(dat)
    frm=Frame(root1)
    i=0
    for r in dat:
        j=0
        for c in r:
            e=Entry(frm)
            e.insert(0,c)
            if(i==0):
                e.config(bg="black", fg="white",state="normal")
            else:
                e.config(state="readonly")
            e.grid(row=i,column=j)
            j=j+1
        i=i+1
    frm.place(x=50,y=50,height=400,width=500)


#mainloop()



root=Tk()
root.geometry("1000x1000")
root.config(bg="pink")
conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
cur=conn.cursor()
lb=Label(text="Course Master",bg="pink",font=("Verdana",30))
lb1=Label(text="CCode",font=("Verdana",15))
lb2=Label(text="CName",font=("Verdana",15))
lb3=Label(text="Duration",font=("Verdana",15))
lb4=Label(text="Fees",font=("Verdana",15))

b1=Button(text="Add New",bg="light blue",font=("Verdana",12),command=new)
b2=Button(text="Save",bg="light blue",font=("Verdana",12),command=save)
b3=Button(text="Modify",bg="light blue",font=("Verdana",12),command=mfy)
b4=Button(text="Delete",bg="light blue",font=("Verdana",12),command=dell)
b5=Button(text="Display All Courses",bg="light blue",font=("Verdana",12),command=disp)

lb5=Label(text="Find",font=("Verdana",15))
items=["select course"]
cur.execute("select cname from courses")
row=cur.fetchall()
for r in row:
    items.append(r[0])
    #print(r[0])


cname=StringVar()

cb=ttk.Combobox(root,values=items, state="readonly",textvariable=cname)
cb.set("select course")
cb.bind("<<ComboboxSelected>>", sch)
lb.place(x=150,y=50,width=400,height=100)

lb1.place(x=150,y=200,width=100,height=30)
t1=Entry()
t1.place(x=300,y=200,width=200,height=30)
lb2.place(x=150,y=250,width=100,height=30)
t2=Entry()
t2.place(x=300,y=250,width=200,height=30)
lb3.place(x=150,y=300,width=100,height=30)
t3=Entry()
t3.place(x=300,y=300,width=200,height=30)
lb4.place(x=150,y=350,width=100,height=30)
t4=Entry()
t4.place(x=300,y=350,width=200,height=30)

b1.place(x=150,y=400,width=90,height=30)
b2.place(x=250,y=400,width=90,height=30)
b3.place(x=350,y=400,width=90,height=30)
b4.place(x=450,y=400,width=90,height=30)
b5.place(x=550,y=400,width=180,height=30)

lb5.place(x=150,y=450,width=100,height=30)
cb.place(x=300,y=450,width=200,height=30)





mainloop()

