print("database form")
from tkinter import *
from tkinter import ttk
from datetime import datetime 
from tkinter.messagebox import *
import mysql.connector
class cmaster1:

    def dell(self):
        s1="delete from student where adno='{}'".format(self.t12.get())
        #print(s1)
        self.cur.execute(s1)
        self.conn.commit()
        showinfo(title="Message for you", message="Delete sucessfully")

    def mfy(self):
        s1="update student set studentname='{}',fathername='{}',age={} where adno={}".format(self.t3.get(),self.t4.get(),self.t6.get(),self.t1.get())                                                      
        #print(s1)
        self.cur.execute(s1)
        self.conn.commit()
        showinfo(title="Message for you", message="Update sucessfully")
        
    def fd(self):
        self.t1.config(state="normal")
        self.t2.config(state="normal")
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.t6.delete(0,END)
        self.cb1.set("Select City")
        self.cb.set("Select Course")
        self.t9.delete(0,END)
        self.t10.delete(0,END)
        self.t11.delete(0,END)   
        s1="select * from student where adno='{}'".format(self.t12.get())
        #print(s1)
        self.cur.execute(s1)
        r=self.cur.fetchone()
        if(r):
            self.t1.insert(0,r[0])
            self.t2.insert(0,r[1])
            self.t3.insert(0,r[2])
            self.t4.insert(0,r[3])
            gn=r[5]
            self.t6.insert(0,r[4])
            self.cb1.set(r[6])
            self.cb.set(r[7])
            self.t9.insert(0,r[8])
            self.t10.insert(0,r[9])
            self.t11.insert(0,r[10])
            if gn=="Male":
                self.gen.set(1)
            else:
                self.gen.set(2)
        else:
             showwarning(title="Warning", message="Rollno does not exist")



    def new(self):
        self.t1.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.t6.delete(0,END)
        self.cb1.set("Select City")
        self.cb.set("Select Course")
        self.t9.delete(0,END)
        self.t10.delete(0,END)
        self.t11.delete(0,END)
        self.t1.focus()
        s1="select max(adno) from student"
        self.cur.execute(s1)
        r=self.cur.fetchone()
        if(r[0]>0):
            a=r[0]+1
            self.t1.insert(0,a)
            self.t1.config(state="readonly")
        #t1.focus()

    def sch(self,e):
        self.t9.delete(0,END)
        self.t10.delete(0,END)  
        #print(cname.get())
        s1="select * from courses where cname='{}'".format(self.cname.get())
        #print(s1)
        try:
            self.cur.execute(s1)
            r=self.cur.fetchone()
            self.t9.insert(0,r[2])
            self.t10.insert(0,r[3])
            #cur.close()
            #conn.close()
        except IOError as e:
            print(e.strerror())



    def save(self):
        a=self.t1.get()
        b=self.t2.get()
        c=self.t3.get()
        d=self.t4.get()
        f=self.t6.get()
        g=self.cb1.get()
        h=self.cb.get()
        i=self.t9.get()
        j=self.t10.get()
        k=self.t11.get()
        z=int(j)-int(k)
        if(self.gen.get()==1):
            gn="Male"
        else:
            gn="Female"

        s1="insert into student values({0},'{1}','{2}','{3}',{4},'{5}','{6}','{7}','{8}',{9},{10},{11})".format(a,b,c,d,f,gn,g,h,i,j,k,z)
        #print(s1)
        self.cur.execute(s1)
        self.conn.commit()
        showinfo(title="Message for you", message="Save sucessfully")
    
        #conn.close()

    def disp(self):
        root1=Toplevel()
        root1.geometry("1300x400")
        conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
        cur=conn.cursor()
        cur.execute("SELECT * FROM student")
        data= cur.fetchall()
        dat=[["Adno.","Adadte","Student name","Father name","Age","Gender","City","Cname","Duration","Fee","Amtpaid","Balance"]]
        for r in data:
            ls=[]
            ls.append(r[0])
            ls.append(r[1])
            ls.append(r[2])
            ls.append(r[3])
            ls.append(r[4])
            ls.append(r[5])
            ls.append(r[6])
            ls.append(r[7])
            ls.append(r[8])
            ls.append(r[9])
            ls.append(r[10])
            ls.append(r[11])
            dat.append(ls)
        

    #print(dat)
        frm=Frame(root1)
        i=0
        for r in dat:
            j=0
            for c in r:
                e=Entry(frm,width=16)
                e.insert(0,c)
                if(i==0):
                   e.config(bg="black", fg="white",state="normal")
                else:
                    e.config(state="readonly")
                e.grid(row=i,column=j)
                j=j+1
            i=i+1
        frm.place(x=40,y=50)

    
    def __init__(self):    
              
        root=Tk()
        root.geometry("1000x1000")
        root.config(bg="peachpuff")
        self.conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
        self.cur=self.conn.cursor()
            
        lb=Label(root,text="Addmission Form",bg="rosybrown",font=("Verdana",30))
        lb1=Label(root,text="Adno",bg="mediumaquamarine",font=("Verdana",15))
        lb2=Label(root,text="Addate",bg="mediumaquamarine",font=("Verdana",15))
        #d=datetime(1,1,1).now()
        lb3=Label(root,text="Sname",bg="mediumaquamarine",font=("Verdana",15))
        lb4=Label(root,text="Fname",bg="mediumaquamarine",font=("Verdana",15))
        lb5=Label(root,text="Gender",bg="mediumaquamarine",font=("Verdana",15))
        self.gen=IntVar()
        rd1=Radiobutton(root,text="Male",var=self.gen, value=1,font=("Verdana",12))
        rd=Radiobutton(root,text="Female",value=2,var=self.gen,font=("Verdana",12))
        lb6=Label(root,text="Age",bg="mediumaquamarine",font=("Verdana",15))
        lb7=Label(root,text="City",bg="mediumaquamarine",font=("Verdana",15))
        self.cty=["Select City","Hisar","Fatehabad","Sirsa","Delhi","Chandhigarh"]

        self.city=StringVar()
        self.cb1=ttk.Combobox(root,values=self.cty, state="readonly",textvariable=self.city)
        self.cb1.set("Select City")
        self.cb1.bind("<<ComboboxSelected>>")
        lb8=Label(root,text="Cname",bg="mediumaquamarine",font=("Verdana",15))
        items=["Select Course"]
        self.cur.execute("select cname from courses")
        row=self.cur.fetchall()
        for r in row:
            items.append(r[0])
            #print(r[0])
        self.conn.commit()
        #conn.close()
        self.cname=StringVar()

        self.cb=ttk.Combobox(root,values=items, state="readonly",textvariable=self.cname)
        self.cb.set("Select course")
        self.cb.bind("<<ComboboxSelected>>",self.sch)
        lb9=Label(root,text="Duration",bg="mediumaquamarine",font=("Verdana",15))
        lb10=Label(root,text="Fees",bg="mediumaquamarine",font=("Verdana",15))
        lb11=Label(root,text="Amtpaid",bg="mediumaquamarine",font=("Verdana",15),)
        #lb12=Label(text="Find", font=("Verdana",15))
        b1=Button(root,text="Add New",bg="rosybrown",font=("Verdana",12),command=self.new)
        b2=Button(root,text="Save",bg="rosybrown",font=("Verdana",12),command=self.save)
        b3=Button(root,text="Modify",bg="rosybrown",font=("Verdana",12),command=self.mfy)
        b4=Button(root,text="Delete",bg="rosybrown",font=("Verdana",12),command=self.dell)
        b5=Button(root,text="Find",bg="rosybrown",font=("Verdana",15),command=self.fd)
        b6=Button(root,text="Display student detail",bg="rosybrown",font=("Verdana",12),command=self.disp)

        adno=StringVar()

        lb.place(x=150,y=20,width=800,height=50)

        lb1.place(x=150,y=100,width=100,height=25)
        self.t1=Entry(root)
        self.t1.place(x=300,y=100,width=200,height=25)
        lb2.place(x=150,y=150,width=100,height=25)
        d=datetime(1,1,1).now()
        cd=StringVar()
        cd=d.strftime("%Y-%m-%d")
        #print(cd)
        #print('{}-{}-{}'.format(d.year,d.month,d.day))
        self.t2=Entry(root)
        self.t2.insert(0,cd)
        self.t2.config(state="readonly")
        self.t2.place(x=300,y=150,width=200,height=25)
        lb3.place(x=150,y=200,width=100,height=25)
        self.t3=Entry(root)
        self.t3.place(x=300,y=200,width=200,height=25)
        lb4.place(x=150,y=250,width=100,height=25)
        self.t4=Entry(root)
        self.t4.place(x=300,y=250,width=200,height=25)
        lb5.place(x=150,y=300,width=100,height=25)
        rd1.place(x=300,y=300,width=90,height=25)
        rd.place(x=400,y=300,width=90,height=25)
        lb6.place(x=150,y=350,width=100,height=25)
        self.t6=Entry(root)
        self.t6.place(x=300,y=350,width=200,height=25)
        lb7.place(x=150,y=400,width=100,height=25)
        self.cb1.place(x=300,y=400,width=200,height=25)
        lb8.place(x=150,y=450,width=100,height=25)
        self.cb.place(x=300,y=450,width=200,height=25)
        lb9.place(x=150,y=500,width=100,height=25)
        self.t9=Entry(root)
        self.t9.place(x=300,y=500,width=200,height=25)
        lb10.place(x=150,y=550,width=100,height=25)
        self.t10=Entry(root)
        self.t10.place(x=300,y=550,width=200,height=25)
        lb11.place(x=150,y=600,width=100,height=25)
        self.t11=Entry(root)
        self.t11.place(x=300,y=600,width=200,height=25)


        b1.place(x=550,y=300,width=90,height=40)
        b2.place(x=650,y=300,width=90,height=40)
        b3.place(x=750,y=300,width=90,height=40)
        b4.place(x=850,y=300,width=90,height=40)
        b5.place(x=550,y=400,width=100,height=25)
        b6.place(x=650,y=500,width=200,height=25)

        self.t12=Entry(root)
        self.t12.place(x=700,y=400,width=200,height=25)

        mainloop()


#obj=cmaster()