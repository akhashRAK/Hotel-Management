from tkinter import *
from tkinter import messagebox
import mysql.connector
import time
import datetime
import os
connector = mysql.connector.connect(host = 'localhost', password = 'akhash', user = 'root', database = 'project')
cursor = connector.cursor()
def get_rooms():
    statement = 'select ROOM_NO from customers where STATUS != "FREE"'
    cursor.execute(statement)
    r = [i[0] for i in cursor]
    return r
def menu():
    messagebox.showinfo("Room service"," \tPRICING\n\n\n Coffee--> RS 20 \nTea --> RS 20 \nMilk --> RS 10 \n \n \n* Other services are free of cost\n ")
def submit():
     
    room=roomvariable.get()    
    serviceneeded= service.get()
    statement1='SELECT CUSTOMER_ID FROM CUSTOMERS WHERE ROOM_NO=' +  str(room)
    cursor.execute(statement1)
    correct_id= cursor.fetchone()

    if serviceneeded=='Cleaning'or serviceneeded=='Water' or serviceneeded=='Hotwater':
        price=0
    if serviceneeded=='Milk':
        price=10
    if serviceneeded=='Coffee':
        price=20
    if serviceneeded=='Tea':
        price=20     
    if correct_id[0]==cust_id.get():
        a=time.localtime()
        hours=a[3]
        mins=a[4]
        sec=a[5]
        ctime=datetime.time(hours,mins,sec)
        cdate= datetime.date.today()
        ctime=str(ctime)
        cdate=str(cdate)

        submitbutton.configure(state=DISABLED)
        resetbutton.configure(state=DISABLED)
        response=messagebox.askokcancel("Room service","Click OK to confirm your order\n\n COST:"+str(price))
        if response==1:
            statement2=  "insert into roomservice (ROOM_NO,SERVICE,TOTAL,DATE,TIME) values('%s' ,'%s' ,%s,'%s','%s')" %(room,serviceneeded,price,cdate,ctime)
            cursor.execute(statement2)
            connector.commit()
            messagebox.showinfo("Room service",message='Entry successfully added')
            resetbutton.configure(state=ACTIVE)
        else:   
            submitbutton.configure(state=ACTIVE)
            resetbutton.configure(state=ACTIVE)
    else:
        messagebox.showerror('Restaurant',"Room Number or Customer ID wrong") 
def reset():
    service.set('Cleaning')
    cust_id.set(0)
    roomvariable.set(available_rooms[0])   
    submitbutton.configure(state=ACTIVE)
def roomservice():
    global identry
    global roomvariable
    global service
    global cust_id
    global submitbutton
    global resetbutton
    global available_rooms
    available_rooms=get_rooms()
    servicelist=['Cleaning','Milk','Tea','Coffee','Water','Hotwater']
    service= StringVar()
    service.set(servicelist[0])
    roomvariable=IntVar()   
    cust_id=IntVar()
    cust_id.set(0)
    roomservice_screen=Toplevel()
    roomservice_screen.geometry("600x600")
    roomservice_screen.config(bg='RosyBrown1')
    roomservice_screen.title("Room service")
    #roomservice_screen.iconbitmap(str(os.getcwd())+'/icons/'+'roomservice.ico')
    try:
      
        roomvariable.set(available_rooms[0])
    except:
        messagebox.showerror("No customers available") 
        roomservice_screen.destroy()
        return
    # title label
    roomservice_label=Label(roomservice_screen,text="ROOM SERVICE",font = 'bahnschrift 24 bold',bg='RosyBrown1',fg='black',padx=20) 
    roomservice_label.place(x=240-30,y=50-30)     
    # for getting roomno
    roomnolabel=Label(roomservice_screen,text='Room No',fg='black',bg='RosyBrown1',font='bahnschrift 15 bold',padx=20)
    roomnolabel.place(x=80,y=170)

    menu_button=Button(roomservice_screen,text='MENU',fg='black',bg='RosyBrown1',font='bahnschrift 15 bold',padx=20,command=menu)
    menu_button.place(x=480,y=100)

    roomnooption=OptionMenu(roomservice_screen,roomvariable,*available_rooms)
    roomnooption.place(x=400,y=170)

    # for getting customerid
    idlabel=Label(roomservice_screen,text='Customer id',fg='black',bg='RosyBrown1',font='bahnschrift 15 bold',padx=20)
    idlabel.place(x=80,y=240)

    identry=Entry(roomservice_screen,textvariable=cust_id)
    identry.place(x=400,y=240)

    #service required

    servicelabel=Label(roomservice_screen,text='Service required',fg='black',bg='RosyBrown1',font='bahnschrift 15 bold',padx=20,pady=20)
    servicelabel.place(x=80,y=310)

    serviceselected=OptionMenu(roomservice_screen,service,*servicelist)
    serviceselected.place(x=400,y=310)

    #submit button
    submitbutton=Button(roomservice_screen,text='SUBMIT',fg='black',bg='white',font='bahnschrift 15 bold',padx=20,command=submit)
    submitbutton.place(x=150,y=540-30)

    #reset button
    resetbutton=Button(roomservice_screen,text="RESET",fg='black',bg='white',font='bahnschrift 15 bold',padx=20,command=reset)
    resetbutton.place(x=300,y=540-30)

      