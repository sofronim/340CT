from tkinter import *
from sqlite3 import *
from datetime import *
import sqlite3

conn=sqlite3.connect("stocks.db")
c=conn.cursor()
c.execute('''CREATE TABLE stockk
         (name TEXT,quantity INTEGER
         ,date INTEGER,code INTEGER)''')

def create():
    try:
        c.execute("""CREATE TABLE stockk
                  name,quantity,date,code""")
    except:
        pass

class App(Frame):

    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)
        root.geometry('400x200')

        topFrame = Frame(master)      #Frames
        topFrame.pack()
        middleFrame= Frame(master)
        middleFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack()

        title = Label(topFrame,text="Login", font=("Helvetica", 18), fg="red")
        title.pack(side=TOP)
        
        login = Button(bottomFrame, text="Log in", command=self.viewNavigation)
        login.pack(pady=5)


    def viewNavigation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Navigation(self.newWindow)

class Navigation(Frame):
    
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)


        title=Label(master,text="Welcome Page",font=("Helvetica",18),fg="blue")
        title.pack(side=TOP)

        window=Button(master,text="View",command=self.viewWindow)
        window.pack(pady=5)

        report=Button(master,text="Reports",command=self.viewReport)
        report.pack(side=TOP)

        add=Button(master,text="Add",command=self.viewAdd)
        add.pack(pady=5)

        remove=Button(master,text="Remove",command=self.viewRemove)
        remove.pack(pady=5)

        

    def viewWindow(self):
        self.newWindow = Toplevel(self.master)
        self.app= viewDatabase(self.newWindow)

    def viewReport(self):
        self.newWindow = Toplevel(self.master)
        self.app = Reports(self.newWindow)

    def viewAdd(self):
        self.newWindow = Toplevel(self.master)
        self.app = Add(self.newWindow)


    def viewRemove(self):
        self.newWindow = Toplevel(self.master)
        self.app = Remove(self.newWindow)




class Reports(Frame):
    def __init__(self, master):
        self.master = master
        topFrame = Frame(master)      #Frames
        topFrame.pack() 
        middleFrame = Frame(master)
        middleFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack()

        title = Label(topFrame,text="Report of the day", font=("Helvetica", 18), fg="blue")
        title.pack(side=TOP)
        
        report = Button(bottomFrame, text="See the daily orders", command=self.dailyOrders)
        report.pack(pady=5)


        
    def dailyOrders(self):
        
        c.execute("""SELECT name,quantity
               FROM stockk """)

        data = c.fetchall ()

# print the rows
        for row in data :
            print (row[1])

class viewDatabase(Frame):
    def __init__(self, master):
        self.master = master
        topFrame = Frame(master)      #Frames
        topFrame.pack() 
        middleFrame = Frame(master)
        middleFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack()

        self.t = Text(topFrame, height=20, width=120)
        self.t.pack(side=TOP)

        self.p = Button(bottomFrame, text="View", command=self.vDB)
        self.p.pack(side=BOTTOM)

    def vDB(self):
        c.execute("""SELECT *
                   FROM stockk""")

        data = c.fetchall ()

# print the rows
        for row in data :
            print (row[1])


class Add(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)

        self.name=Entry(master)
        self.name.pack(side=TOP)

        self.quantity=Entry(master)
        self.quantity.pack(side=TOP)

        self.date=Entry(master)
        self.date.pack(side=TOP)

        

        self.add=Button(master,text="Add",command=self.addData)
        self.add.pack(pady=20)
        

    def addData(self):
        
        Item = self.name.get()
        Quan = self.quantity.get()
        da=self.date.get()

        c.execute("""INSERT INTO stockk 
               (name,quantity,date)
               VALUES(?,?,?)"""[Item,Quan,da])
        
        conn.commit()

        print(Item,Quan,da)
   

class Remove(Frame):
    def __init__(self, master):

        self.master = master
        topFrame = Frame(master)      #Frames
        topFrame.pack() 
        middleFrame = Frame(master)
        middleFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack()
        
        
        self.code=Entry(topFrame)
        self.code.pack(side=TOP)

        

        delete = Button(bottomFrame, text="Delete", command=self.removeData)
        delete.pack(pady=5)

        
        
        

    def removeData(self):
        item = self.code.get()

        c.execute("""DELETE FROM stockk
                WHERE  code = ?""",[item])
        conn.commit()
        
        

if __name__=="__main__":
    root = Tk()
    root.title('POS')    
    root.resizable(width=False, height=False)
    
    app = App(master=root)
    app.mainloop()

conn.commit()
conn.close()    
