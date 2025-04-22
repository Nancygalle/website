print("welcome to fees record")
from tkinter import *
#from tkinter import ttk
from datetime import datetime
from tkinter.messagebox import *
import mysql.connector

class cmaster4:

    def __init__(self): 
        root=Tk()
        root.geometry("1000x1000")
        root.config(bg="light blue")
        self.conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
        self.cur=self.conn.cursor()
        lb=Label(root,text="Fees Form",bg="pink",font=("Verdana",30))
        lb1=Label(root,text="RecpNo.",font=("Verdana",15))
        lb2=Label(root,text="Rdate",font=("Verdana",15))
        lb3=Label(root,text="Adno",font=("Verdana",15))
        lb4=Label(root,text="Sname",font=("Verdana",15))
        lb5=Label(root,text="Fname",font=("Verdana",15))
        lb6=Label(root,text="Cname",font=("Verdana",15))
        lb7=Label(root,text="Totalfees",font=("Verdana",15))
        lb8=Label(root,text="Bal.amt",font=("Verdana",15))
        lb9=Label(root,text="Amtpaid",font=("Verdana",15))

        b1=Button(root,text="Add New",bg="pink",font=("Verdana",15),command=self.new)
        b2=Button(root,text="Save",bg="pink",font=("Verdana",15),command=self.save,state="disabled")
        b3=Button(root,text="Find",bg="pink",font=("Verdana",15),command=self.find) 
        b4=Button(root,text="Show",bg="pink",font=("Verdana",15),command=self.search) 
        lb.place(x=150,y=20,width=700,height=50)

        lb1.place(x=150,y=100,width=100,height=25)
        self.t1=Entry(root)
        #t1.config(state="readonly")
        self.t1.place(x=300,y=100,width=200,height=25)
        lb2.place(x=150,y=150,width=100,height=25)
        self.d=datetime(1,1,1).now()
        self.cd=StringVar()
        self.cd=self.d.strftime("%Y-%m-%d")
        #print(cd)
        #print('{}-{}-{}'.format(d.year,d.month,d.day))
        self.t2=Entry(root)
        self.t2.place(x=300,y=150,width=200,height=25)
        lb3.place(x=150,y=200,width=100,height=25)
        self.t3=Entry(root)
        self.t3.place(x=300,y=200,width=200,height=25)
        lb4.place(x=150,y=250,width=100,height=25)
        self.t4=Entry(root)
        self.t4.place(x=300,y=250,width=200,height=25)
        lb5.place(x=150,y=300,width=100,height=25)
        self.t5=Entry(root)
        self.t5.place(x=300,y=300,width=200,height=25)
        lb6.place(x=150,y=350,width=100,height=25)
        self.t6=Entry(root)
        self.t6.place(x=300,y=350,width=200,height=25)
        lb7.place(x=150,y=400,width=100,height=25)
        self.t7=Entry(root)
        self.t7.place(x=300,y=400,width=200,height=25)
        lb8.place(x=150,y=450,width=100,height=25)
        self.t8=Entry(root)
        self.t8.place(x=300,y=450,width=200,height=25)
        lb9.place(x=150,y=500,width=100,height=25)
        self.t9=Entry(root)
        self.t9.place(x=300,y=500,width=200,height=25)

        b1.place(x=150,y=550,width=100,height=40)
        b2.place(x=300,y=550,width=100,height=40)
        b3.place(x=450,y=550,width=100,height=40)
        self.t10=Entry(root)
        self.t10.place(x=600,y=550,width=200,height=35)
        b4.place(x=550,y=200,width=200,height=35)
        

        mainloop()

        


    def find(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.t5.delete(0,END)
        self.t6.delete(0,END)
        self.t7.delete(0,END)
        self.t8.delete(0,END)
        self.t9.delete(0,END)   
        s1="SELECT fees.recpno,fees.rdate,fees.adno,studentname,fathername,cname,student.fee,fees.balamt,fees.amtpaid  from student , fees where student.adno=fees.adno and fees.recpno={}".format(self.t10.get())
        #print(s1)
        self.cur.execute(s1)
        r=self.cur.fetchone()
        self.t1.insert(0,r[0])
        self.t2.insert(0,r[1])
        self.t3.insert(0,r[2])
        self.t4.insert(0,r[3])
        self.t5.insert(0,r[4])
        self.t6.insert(0,r[5])
        self.t7.insert(0,r[6])
        self.t8.insert(0,r[7])
        self.t9.insert(0,r[8])

    def search(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        #self.t3.delete(0,END) 
        self.t4.delete(0,END) 
        self.t5.delete(0,END) 
        self.t6.delete(0,END) 
        self.t7.delete(0,END) 
        self.t8.delete(0,END) 
        self.t9.delete(0,END)  
        s1="select * from student where adno='{}'".format(self.t3.get())
        #print(s1)
        self.cur.execute(s1)
        r=self.cur.fetchone()
        self.t4.insert(0,r[2])
        self.t5.insert(0,r[3])
        self.t6.insert(0,r[7])
        self.t7.insert(0,r[9])
        self.t8.insert(0,r[11])
        self.t9.insert(0,r[11])
        self.t4.config(state="disabled")
        self.t5.config(state="disabled")
        self.t6.config(state="disabled")
        self.t7.config(state="disabled")
        #self.t8.config(state="disabled")

    def new(self):
        self.t4.config(state="normal")
        self.t5.config(state="normal")
        self.t6.config(state="normal")
        self.t7.config(state="normal")
        #self.t8.config(state="normal")
        self.t1.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.t5.delete(0,END)
        self.t6.delete(0,END)
        self.t7.delete(0,END)
        self.t8.delete(0,END)
        self.t9.delete(0,END)
        s1="select max(recpno) from fees"
        #print(s1)
        self.cur.execute(s1)
        r=self.cur.fetchone()
        if(r[0]>0):
            a=r[0]+1
            self.t1.insert(0,a)
            self.t1.config(state="readonly")

        self.d=datetime(1,1,1).now()
        self.cd=StringVar()
        self.cd=self.d.strftime("%Y-%m-%d")
        self.t2.insert(0,self.cd)
        self.t2.config(state="readonly")
        self.t2.config(state="normal")
    
        self.t3.focus()

    def save(self):
        a=self.t1.get()
        b=self.t2.get()
        c=self.t3.get()
        j=self.t8.get()
        k=self.t9.get()
        d=int(k)-int(j)
        if d==0:
            self.b2.config(state="normal") 
            s1="insert into fees values({0},'{1}',{2},{3},{4})".format(a,b,c,j,k)
            #print(s1)
            s2="update student set balance=0, amtpaid=amtpaid+balance where adno='{}'".format(self.t3.get())
            #print(s2)
            self.cur.execute(s1)
            self.cur.execute(s2)
            self.conn.commit()
        else:
             self.b2.config("disabled")  
             showinfo(title="Message for you",message="Pay Rs. First")  



#obj2=cmaster4()


