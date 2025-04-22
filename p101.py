print ("Welcome to database with Tkinter")
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector

class cmaster:
        
    def new(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.t1.focus()

    def dell(self):
        s1="delete from courses where cname='{}'".format(self.t2.get())
        self.cur.execute(s1)
        self.conn.commit()
        showinfo(title="Message for you", message="Delete sucessfully")

    def mfy(self):
        s1="update courses set cname='{}',duration='{}',fees={} where ccode={}".format(self.t2.get(),self.t3.get(),self.t4.get(),self.t1.get())
        self.cur.execute(s1)
        self.conn.commit()
        showinfo(title="Message for you", message="Update sucessfully")



    def sch(self,e):
        #global t1,self.t2,self.t3,self.t4,self.cur,self.conn,
        #global cname
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)    
        #print(cb.get())
        s1="select * from courses where cname='{}'".format(self.cname.get())
        self.cur.execute(s1)
        r=self.cur.fetchone()
        self.t1.insert(0,r[0])
        self.t2.insert(0,r[1])
        self.t3.insert(0,r[2])
        self.t4.insert(0,r[3])
                
    def save(self):    
        a=self.t1.get()
        b=self.t2.get()
        c=self.t3.get()
        d=self.t4.get()
        s1="insert into courses values({0},'{1}','{2}',{3})".format(a,b,c,d)
        self.cur.execute(s1)
        self.conn.commit()
        showinfo(title="Message for you", message="Save sucessfully")

        #self.conn.close()

    def disp(self):
        
        root1=Toplevel()
        root1.geometry("600x200")
        self.cur.execute("SELECT * FROM courses")
        data= self.cur.fetchall()
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



    def __init__(self):    
        root=Toplevel()
        root.geometry("1000x1000")
        root.config(bg="pink")
        lb=Label(root,text="Course Master",bg="pink",font=("Verdana",30,"bold"))
        lb1=Label(root,text="CCode",font=("Verdana",15))
        lb2=Label(root,text="CName",font=("Verdana",15))
        lb3=Label(root,text="Duration",font=("Verdana",15))
        lb4=Label(root,text="Fees",font=("Verdana",15))
        self.conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
        self.cur=self.conn.cursor()
    
        b1=Button(root,text="Add New",bg="light blue",font=("Verdana",12),command=self.new)
        b2=Button(root,text="Save",bg="light blue",font=("Verdana",12),command=self.save)
        b3=Button(root,text="Modify",bg="light blue",font=("Verdana",12),command=self.mfy)
        b4=Button(root,text="Delete",bg="light blue",font=("Verdana",12),command=self.dell)
        b5=Button(root,text="Display All Courses",bg="light blue",font=("Verdana",12),command=self.disp)

        lb5=Label(root,text="Find",font=("Verdana",15))
        items=["select course"]
        self.cur.execute("select cname from courses")
        row=self.cur.fetchall()
        for r in row:
            items.append(r[0])
            #print(r[0])


        self.cname=StringVar()

        self.cb=ttk.Combobox(root,values=items, state="readonly",textvariable=self.cname)
        self.cb.set("select course")
        self.cb.bind("<<ComboboxSelected>>", self.sch)
        lb.place(x=150,y=50,width=400,height=100)

        lb1.place(x=150,y=200,width=100,height=30)
        self.t1=Entry(root)
        self.t1.place(x=300,y=200,width=200,height=30)
        lb2.place(x=150,y=250,width=100,height=30)
        self.t2=Entry(root)
        self.t2.place(x=300,y=250,width=200,height=30)
        lb3.place(x=150,y=300,width=100,height=30)
        self.t3=Entry(root)
        self.t3.place(x=300,y=300,width=200,height=30)
        lb4.place(x=150,y=350,width=100,height=30)
        self.t4=Entry(root)
        self.t4.place(x=300,y=350,width=200,height=30)

        b1.place(x=150,y=400,width=90,height=30)
        b2.place(x=250,y=400,width=90,height=30)
        b3.place(x=350,y=400,width=90,height=30)
        b4.place(x=450,y=400,width=90,height=30)
        b5.place(x=550,y=400,width=180,height=30)

        lb5.place(x=150,y=450,width=100,height=30)
        self.cb.place(x=300,y=450,width=200,height=30)
        mainloop()
#obj1=cmaster()
