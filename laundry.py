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
      messagebox.showinfo("Laundry"," \tPRICING\n\n\nShirts --> RS 15 \nPants --> RS 25 \nOthers --> RS 10 \n \n \n* Sarees are also counted as shirts\n ")
def submit():
     
      room=roomvariable.get()    
      shirts=shirtvariable.get()
      pants=pantvariable.get()
      others=othervariable.get()
      statement1='SELECT CUSTOMER_ID FROM CUSTOMERS WHERE ROOM_NO=' +  str(room)
      cursor.execute(statement1)
      correct_id= cursor.fetchone()
      

      price=15*(shirts)+25*(pants)+10*(others)
      if price !=0 and cust_id.get()!=0:
            if correct_id[0] == cust_id.get():
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

                  response=messagebox.askokcancel('Laundry',"Click OK to confirm\n\nCOST :"+str(price))
                  if response==1:
                        statement2='insert into laundry_history (ROOM_NO,CUSTOMER_ID,SHIRTS,PANTS,OTHERS,TOTAL,DATE,TIME) values('+str(room)+','+str(cust_id.get())+','+ str(shirts)+','+str(pants)+','+str(others)+','+str(price)+',"'+cdate+'","'+ctime+'")'
                        statement3='UPDATE LAUNDRY SET SHIRTS=SHIRTS+'+ str(shirts)+ ',PANTS=PANTS+' +str(pants)+ ',OTHERS=OTHERS+' +str(others)+ ',TOTAL=TOTAL+' + str(price)+ ' WHERE ROOM_NO=' + str(room)
                        cursor.execute(statement2)
                        connector.commit()
                        cursor.execute(statement3)
                        connector.commit()
                        messagebox.showinfo("Laundry",message="Entry successfully added")
                        resetbutton.configure(state=ACTIVE)
                        
                  else:
                        submitbutton.configure(state=ACTIVE)
                        resetbutton.configure(state=ACTIVE)



                 
     
            else:
                  messagebox.showerror('Landry',"Room Number or Customer ID wrong")

      else:
            messagebox.showerror('Laundry',"Enter proper credentials")  
def reset():
      shirtvariable.set(0)

      pantvariable.set(0)

      othervariable.set(0)

      cust_id.set(0)

      roomvariable.set(available_rooms[0])   
      submitbutton.configure(state=ACTIVE)
def laundry():

      global identry
      global roomvariable
      global shirtvariable
      global pantvariable
      global othervariable
      global cust_id
      global submitbutton
      global resetbutton
      global available_rooms

      

      available_rooms=get_rooms()

      shirtvariable=IntVar()
      shirtvariable.set(0)

      pantvariable=IntVar()
      pantvariable.set(0)

      othervariable=IntVar()
      othervariable.set(0)

      roomvariable=IntVar()   
      cust_id=IntVar()
      cust_id.set(0)
      
      laundry_screen=Toplevel()
      laundry_screen.geometry("600x600")
      laundry_screen.config(bg='salmon2')
      laundry_screen.title("Laundry")
      laundry_screen.iconbitmap(str(os.getcwd())+'/icons/'+'laundry.ico')

      try:
      
           roomvariable.set(available_rooms[0])
      except:
           messagebox.showerror("No customers available") 
           laundry_screen.destroy()
           return


     # title label
      Laundry_label=Label(laundry_screen,text="LAUNDRY",font = 'bahnschrift 25 bold',bg='salmon2',fg='black',padx=20) 
      Laundry_label.place(x=240-30,y=50-30)     
      # for getting roomno
      roomnolabel=Label(laundry_screen,text='Room No',fg='black',bg='salmon2',font='bahnschrift 15 bold',padx=20)
      roomnolabel.place(x=80,y=150-30)

      menu_button=Button(laundry_screen,text='MENU',fg='black',bg='salmon2',font='bahnschrift 15 bold',padx=20,command=menu)
      menu_button.place(x=480,y=50)

      
      roomnooption=OptionMenu(laundry_screen,roomvariable,*available_rooms)
      roomnooption.place(x=400,y=150-30)

      # for getting customerid
      idlabel=Label(laundry_screen,text='Customer id',fg='black',bg='salmon2',font='bahnschrift 15 bold',padx=20)
      idlabel.place(x=80,y=220-30)

      identry=Entry(laundry_screen,textvariable=cust_id)
      identry.place(x=400,y=220-30)

      
      #for getting no of shirts
      shirtlabel=Label(laundry_screen,text='Shirts',fg='black',bg='salmon2',font='bahnschrift 15 bold',padx=20)
      shirtlabel.place(x=80,y=280-30)

      shirtoption=OptionMenu(laundry_screen,shirtvariable,*[i for i in range(0,20)])
      shirtoption.place(x=400,y=280-30)


      #for getting no of pants
      pantlabel=Label(laundry_screen,text='Pants',fg='black',bg='salmon2',font='bahnschrift 15 bold',padx=20)
      pantlabel.place(x=80,y=350-30)

      pantoption=OptionMenu(laundry_screen,pantvariable,*[i for i in range(0,20)])
      pantoption.place(x=400,y=350-30)

      #for getting no of others
      otherlabel=Label(laundry_screen,text='Others',fg='black',bg='salmon2',font='bahnschrift 15 bold',padx=20)
      otherlabel.place(x=80,y=420-30)

      otheroption=OptionMenu(laundry_screen,othervariable,*[i for i in range(0,20)])
      otheroption.place(x=400,y=420-30)

      #submit button
      submitbutton=Button(laundry_screen,text='SUBMIT',fg='black',bg='white',font='bahnschrift 15 bold',padx=20,command=submit)
      submitbutton.place(x=150,y=540-30)

      #reset button
      resetbutton=Button(laundry_screen,text="RESET",fg='black',bg='white',font='bahnschrift 15 bold',padx=20,command=reset)
      resetbutton.place(x=300,y=540-30) 
      
