print("welcome to database")
from tkinter import *
import mysql.connector

class cmaster5:
    def __init__(self):    
        root=Tk()
        root.geometry("1200x1200")
        root.conn=mysql.connector.connect(host="localhost",database="pythonproject",user="root",password="")
        root.cur=root.conn.cursor()
        root.cur.execute("SELECT * FROM student")
        data= root.cur.fetchall()
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
        frm=Frame(root)
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



        mainloop()
#obj4=cmaster5()       