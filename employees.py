from tkinter import ttk
import tkinter as tk
import mysql.connector
import time
connector = mysql.connector.connect(host = 'localhost', password = 'akhash', user = 'root', database = 'project')
cursor = connector.cursor()
def employees():
    window=tk.Toplevel()
    window.title("Employees")
    window.resizable(False,False)
    window.geometry('600x600')
    window.configure(bg="slategray1")
    tk.Label(window,text="EMPLOYEE",font=("bahnschrift",20,"bold"),pady=20,bg="slategray1").pack()
    treev=ttk.Treeview(window,show="headings",height="15")
    treev.pack()
    mystyle=ttk.Style()
    mystyle.theme_use("alt")
    mystyle.configure("Treeview",background="light cyan",fieldbackground="silver",rowheight="25",foreground="white")
    mystyle.map("Treeview",background=[('selected', 'dodger blue')])
    treev["columns"]=("1","2","3","4","5")
    treev['show']='headings'
    treev.column("1", width=100, anchor='c')
    treev.column("2", width=100, anchor='c')
    treev.column("3", width=100, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=100,anchor='c')
    treev.heading("1", text="EMP_ID")
    treev.heading("2", text="EMP_NAME")
    treev.heading("3", text="DUTY")
    treev.heading("4", text="DATE OF JOIN")
    treev.heading("5", text="SHIFT")
    #sql queries
    a=time.localtime()
    hours=a[3]
    if hours in [8,9,10,11,12,13,14,15,16]:
        statement1='select EMP_ID,EMP_NAME,DUTY,DATE_OF_JOIN,SHIFT from employees where SHIFT ="DAY";'
        cursor.execute(statement1)
    if hours in [17,18,19,20,21,22,23,24]:
        statement2='select EMP_ID,EMP_NAME,DUTY,DATE_OF_JOIN,SHIFT from employees where SHIFT ="EVENING";'
        cursor.execute(statement2)
    if hours in [0,1,2,3,4,5,6,7]:
        statement3='select EMP_ID,EMP_NAME,DUTY,DATE_OF_JOIN,SHIFT from employees where SHIFT ="NIGHT";'
        cursor.execute(statement3)
    details=cursor.fetchall()
    # adding details
    for j in details:
        treev.insert("", 'end', values=j)

     


  
    
    
    

    
    
    

    






    


