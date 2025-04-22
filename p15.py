print("welcome to database programming")
from tkinter import *
import mysql.connector

class cmaster3:
    def __init__(self):    
        root=Toplevel()
        root.geometry("600x200")
        root.conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
        root.cur=root.conn.cursor()
        root.cur.execute("SELECT * FROM courses")
        data= root.cur.fetchall()
        dat=[["Ccode","Cname","Duration","Fees"]]
        for r in data:
            ls=[]
            ls.append(r[0])
            ls.append(r[1])
            ls.append(r[2])
            ls.append(r[3])
            dat.append(ls)
            

        #print(dat)
        frm=Frame(root)
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
        frm.place(x=100,y=50,height=400,width=500)


        mainloop()