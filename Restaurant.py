from tkinter import *
from tkinter import messagebox
import mysql.connector
import random
import time
import datetime
import os
connector = mysql.connector.connect(host = 'localhost', password = 'akhash', user = 'root', database = 'project')
cursor = connector.cursor()
def get_ids():
    cursor.execute('select BOOKING_ID from restaurant where BOOKING_ID IS NOT NULL')
    available_ids = [i[0] for i in cursor]
    return available_ids
idlist=get_ids() 
def generate_id():
        s="123456789"
        b_id = ''.join(random.sample('123456789',1)) + ''.join(random.sample(s,4))
        if b_id not in idlist:
            idlist.append(b_id)
            bookingid.set(b_id)
        else:
            generate_id()
def restaurant():

    def menu():
        messagebox.showinfo("Restaurant","\tPRICING\n\nBREAKFAST:(8 AM-12 AM)\nAdult(VEG)--> RS 200\nChild(VEG)--> RS 100\nAdult(NONVEG)--> RS 250\nChild(NONVEG)--> RS 150"+
                                                        "\n\nLUNCH:(12 PM-5 PM)\nAdult(VEG)--> RS 250\nChild(VEG)--> RS 150\nAdult(NONVEG)--> RS 325\nChild(NONVEG)--> RS 200"+
                                                        "\n\nDINNER:(7 PM-12 PM)\nAdult(VEG)--> RS 275\nChild(VEG)--> RS 200\nAdult(NONVEG)--> RS 350\nChild(NONVEG)--> RS 250"+
                                                        "\n\n*Please note that we only offer BUFFET"+
                                                        "\n*BUFFETS are open only during the time mentioned above"+
                                                        "\n*Food cannot be provided directly through ROOM SERVICE"+
                                                        "\n*CHILD - 14 AND BELOW")
                                                        
    def findcustomertype():
            if meal.get() not in["Breakfast","Dinner","Lunch"]:
                confirm_button.configure(state=DISABLED)
                messagebox.showerror('',"Meal not selected")
            else:
                global type1
                type1=r.get()
                if type1=="Hotel Guest":
                    hotelguest()
            
                elif type1=='Restaurant Guest':
                    Restaurantguest()
                else:
                    messagebox.showerror('',"Please select customer type")    


    global r            

    

    # for hotel guest

    def submit2():
            a=time.localtime()
            hours=a[3]
            price_breakfast= 200*(vegadult1no.get())+100*(vegchild1no.get())+250*(nonvegadult1no.get())+150*(nonvegchild1no.get())
            price_lunch= 250*(vegadult1no.get())+150*(vegchild1no.get())+325*(nonvegadult1no.get())+200*(nonvegchild1no.get())
            price_dinner= 275*(vegadult1no.get())+200*(vegchild1no.get())+350*(nonvegadult1no.get())+250*(nonvegchild1no.get())
            statement1='SELECT CUSTOMER_ID FROM CUSTOMERS WHERE ROOM_NO=' +  str(roomnovariable.get())
            cursor.execute(statement1)
            correct_id= cursor.fetchone()
            if meal.get()=='Breakfast':
                price=price_breakfast
            if meal.get()=='Lunch':
                price=price_lunch
            if meal.get()=='Dinner':     
                price=price_dinner  

            if  price!=0:

                if correct_id[0] == cust_id.get() :
                    a=time.localtime()
                    hours=a[3]
                    mins=a[4]
                    sec=a[5]
                    ctime=datetime.time(hours,mins,sec)
                    cdate= datetime.date.today()
                    ctime=str(ctime)
                    cdate=str(cdate)

                    submit1button.configure(state=DISABLED)
                    reset1button.configure(state=DISABLED)
                    previous1button.configure(state=DISABLED)

                    response=messagebox.askokcancel("Restaurant","Click OK to confirm your order\n\n COST:"+str(price))
                    if response==1:
                        statement2=  'insert into restaurant (CUSTOMER_ID,CUSTOMER_TYPE,ADULTS_VEG,CHILDREN_VEG,ADULTS_NONVEG,CHILDREN_NONVEG,TOTAL,DATE,TIME) values('+str(identry.get())+',"'+ type1+'",'+str(vegadult1no.get())+','+str(vegchild1no.get())+','+str(nonvegadult1no.get())+','+str(nonvegchild1no.get())+','+str(price)+',"'+cdate+'","'+ctime+'")'
                        cursor.execute(statement2)
                        connector.commit()
                        messagebox.showinfo("Restaurant",message='Entry successfully added')
                        reset1button.configure(state=ACTIVE)
                        previous1button.configure(state=ACTIVE)
                    else:   
                        submit1button.configure(state=ACTIVE)
                        reset1button.configure(state=ACTIVE)
                        previous1button.configure(state=ACTIVE) 
                else:
                
                    messagebox.showerror('Restaurant',"Room Number or Customer ID wrong")
                    
            else:

                messagebox.showerror('Restaurant',"Enter proper credentials")

    def reset2():

            vegadult1no.set(0)
            nonvegadult1no.set(0)
            vegchild1no.set(0)
            nonvegchild1no.set(0)
            cust_id.set(0)
            submit1button.configure(state=ACTIVE)

    def previous2():
            confirm_button.config(state=ACTIVE)
            mealdropdown.config(state=ACTIVE)

            vegadult1label.destroy()
            vegadult1option.destroy()

            vegchild1label.destroy()
            vegchild1option.destroy()

            nonvegadult1label.destroy()
            nonvegadult1option.destroy()

            nonvegchild1label.destroy()
            nonvegchild1option.destroy()

            roomnolabel.destroy()
            roomnooption.destroy()
            idlabel.destroy()
            identry.destroy()

            submit1button.destroy()
            reset1button.destroy()
            previous1button.destroy()
           
    def hotelguest():
        global identry

        global vegadult1no
        global vegchild1no
        global nonvegadult1no
        global nonvegchild1no

        global vegadult1label
        global vegchild1label
        global nonvegadult1label
        global nonvegchild1label


        global vegadult1option
        global vegchild1option
        global nonvegadult1option
        global nonvegchild1option

        global previous1button
        global reset1button
        global submit1button

        global roomnolabel
        global roomnooption
        global cust_id
        global idlabel

        global roomnovariable




        vegadult1no=IntVar()

        vegchild1no=IntVar()

        nonvegadult1no=IntVar()

        nonvegchild1no=IntVar()
        cust_id=IntVar()
        cust_id.set(0)

        confirm_button.config(state=DISABLED)
        mealdropdown.config(state=DISABLED)

        def get_rooms():
            statement = 'select ROOM_NO from customers where OCCUPANTS is not NULL'
            cursor.execute(statement)
            r = [i[0] for i in cursor]
            return r

        available_rooms=get_rooms()    
        roomnovariable= IntVar()
        try:
            roomnovariable.set(available_rooms[0])
        except:
            messagebox.showerror("No customers available") 
            Restaurant_screen.destroy()
            return


        
        roomnolabel=Label(Restaurant_screen,text="Room no",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        roomnolabel.place(x=80,y=210)

        roomnooption=OptionMenu(Restaurant_screen,roomnovariable,*available_rooms)
        roomnooption.place(x=400,y=210)

        idlabel=Label(Restaurant_screen,text='Customer id',fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',padx=20)
        idlabel.place(x=80,y=270)

        identry=Entry(Restaurant_screen,textvariable= cust_id)
        identry.place(x=400,y=270)

        vegadult1label=Label(Restaurant_screen,text="VEG(Adults)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        vegadult1label.place(x=80,y=320)

        vegadult1option=OptionMenu(Restaurant_screen,vegadult1no,*[i for i in range(0,5)])
        vegadult1option.place(x=400,y=320)


        vegchild1label=Label(Restaurant_screen,text="VEG(Kids)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        vegchild1label.place(x=80,y=370)

        vegchild1option=OptionMenu(Restaurant_screen,vegchild1no,*[i for i in range(0,5)])
        vegchild1option.place(x=400,y=370)
        
        nonvegadult1label=Label(Restaurant_screen,text="NONVEG(Adults)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        nonvegadult1label.place(x=80,y=420)

        nonvegadult1option=OptionMenu(Restaurant_screen,nonvegadult1no,*[i for i in range(0,5)])
        nonvegadult1option.place(x=400,y=420)

        nonvegchild1label=Label(Restaurant_screen,text="NONVEG(Kids)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        nonvegchild1label.place(x=80,y=470)

        nonvegchild1option=OptionMenu(Restaurant_screen,nonvegchild1no,*[i for i in range(0,5)])
        nonvegchild1option.place(x=400,y=470)

        submit1button=Button(Restaurant_screen,text="SUBMIT",fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',padx=20,command=submit2)
        submit1button.place(x=100,y=550)

        #reset button
        reset1button=Button(Restaurant_screen,text="RESET",fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',padx=20,command=reset2)
        reset1button.place(x=220,y=550)    

        #previous page

        previous1button=Button(Restaurant_screen,text="PREVIOUS",fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',padx=20,command=previous2)
        previous1button.place(x=330,y=550)


    # for restaurant guest

    def submit1():
        global bookingid
        global bookingidlabel
        global bookingidentry
        global costlabel
        global costlabel1
        global bill
        

        bookingid=StringVar()
        a=time.localtime()
        hours=a[3]
        price_breakfast= 200*(vegadultno.get())+100*(vegchildno.get())+250*(nonvegadultno.get())+150*(nonvegchildno.get())
        price_lunch= 250*(vegadultno.get())+150*(vegchildno.get())+325*(nonvegadultno.get())+200*(nonvegchildno.get())
        price_dinner= 275*(vegadultno.get())+200*(vegchildno.get())+350*(nonvegadultno.get())+250*(nonvegchildno.get())
        if meal.get()=='Breakfast':
            price=price_breakfast
        if meal.get()=='Lunch':
            price=price_lunch
        if meal.get()=='Dinner':     
            price=price_dinner  
        if price!=0:
            a=time.localtime()
            hours=a[3]
            mins=a[4]
            sec=a[5]
            ctime=datetime.time(hours,mins,sec)
            cdate=datetime.date.today()
            ctime=str(ctime)
            cdate=str(cdate)
            cost= price+ (5/100)*price
            

            #cancelbutton=Button(Restaurant_screen,text='CANCEL',fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20,command=cancel)
            #cancelbutton.place(x=250,y=540)
            costlabel=Label(Restaurant_screen,text="COST",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 12 bold',padx=20)
            costlabel.place(x=350,y=550)

            costlabel1=Label(Restaurant_screen,text=str(cost),fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 12 bold',padx=20)
            costlabel1.place(x=450,y=550)
            submitbutton.configure(state=DISABLED)
            resetbutton.configure(state=DISABLED)
            previousbutton.configure(state=DISABLED)
            response=messagebox.askokcancel("Restaurant","Click OK to confirm your order\n\nCOST(Tax included) :" +str(price+ ((5/100)*price)))

            if response == 1:
             
                bookingidlabel=Label(Restaurant_screen,text="BOOKING ID",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 12 bold',padx=20)
                bookingidlabel.place(x=10,y=550)

                bookingidentry=Entry(Restaurant_screen,textvariable= bookingid,font = 'bahnschrift 12 bold')
                bookingidentry.place (x=170,y=550) 

                generate_id()

                bookingidentry.configure(state= DISABLED)
                
                statement=  'insert into restaurant (BOOKING_ID,CUSTOMER_TYPE, ADULTS_VEG,CHILDREN_VEG,ADULTS_NONVEG,CHILDREN_NONVEG,TOTAL,DATE,TIME) values('+str(bookingid.get())+',"'+ type1 +'",'+str(vegadultno.get())+','+str(vegchildno.get())+','+str(nonvegadultno.get())+','+str(nonvegchildno.get())+','+str(cost)+',"'+cdate+'","'+ctime+'")'
                cursor.execute(statement)
                connector.commit()
                messagebox.showinfo("Restaurant",message="Entry successfully added\nBookingID:"+ str(bookingid.get()))
#-------------------------------------------------------------------billscreen---------------------------------------------------------------
                Restaurant_screen.geometry("1250x600")
                bill=Text( Restaurant_screen, height = 28, width = 60, bg = 'white',fg='black', font = 'bahnschrift 15 bold ',relief = SUNKEN)
                bill.insert(INSERT,"\t\t\tHOTEL NAME\n\n"     )
                bill.insert(INSERT,"DATE : "+ cdate+"\n"    )
                bill.insert(INSERT,"TIME : "+ ctime+ "\n\n"  ) 
                bill.insert(INSERT,"  -------------------------------------------------------------------------------------- \n")  
                bill.insert(INSERT,"\t\t\tRESTAURANT\n\n\n")
                bill.insert(INSERT,"Booking ID : "+str(bookingid.get())+"\n\n")
                bill.insert(INSERT,"S.NO\tPRODUCT\t\tQUANTITY\t\tCOST\n\n")
                if price==price_breakfast:
                    if vegadultno.get()!=0:
                        bill.insert(INSERT,"1\tVEG(ADULT)\t\t"+str(vegadultno.get())+"\t\t"+str(int(vegadultno.get())*200)+'\n')
                    if vegchildno.get()!=0:
                        bill.insert(INSERT,"2\tVEG(CHILD)\t\t"+str(vegchildno.get())+"\t\t"+str(int(vegchildno.get())*100)+'\n')
                    if nonvegadultno.get()!=0:
                        bill.insert(INSERT,"3\tNON-VEG(ADULT)\t\t"+str(nonvegadultno.get())+"\t\t"+str(int(nonvegadultno.get())*250)+'\n')
                    if nonvegchildno.get()!=0:
                        bill.insert(INSERT,"4\tNON-VEG(CHILD)\t\t"+str(nonvegchildno.get())+"\t\t"+str(int(nonvegchildno.get())*150)+'\n')
                if price==price_lunch:
                    if vegadultno.get()!=0:
                        bill.insert(INSERT,"1\tVEG(ADULT)\t\t"+str(vegadultno.get())+"\t\t"+str(int(vegadultno.get())*250)+'\n')
                    if vegchildno.get()!=0:
                        bill.insert(INSERT,"2\tVEG(CHILD)\t\t"+str(vegchildno.get())+"\t\t"+str(int(vegchildno.get())*150)+'\n')
                    if nonvegadultno.get()!=0:
                        bill.insert(INSERT,"3\tNON-VEG(ADULT)\t\t"+str(nonvegadultno.get())+"\t\t"+str(int(nonvegadultno.get())*325)+'\n')
                    if nonvegchildno.get()!=0:
                        bill.insert(INSERT,"4\tNON-VEG(CHILD)\t\t"+str(nonvegchildno.get())+"\t\t"+str(int(nonvegchildno.get())*200)+'\n')
                   
                if price==price_dinner:
                    if vegadultno.get()!=0:
                        bill.insert(INSERT,"1\tVEG(ADULT)\t\t"+str(vegadultno.get())+"\t\t"+str(int(vegadultno.get())*275)+'\n')
                    if vegchildno.get()!=0:
                        bill.insert(INSERT,"2\tVEG(CHILD)\t\t"+str(vegchildno.get())+"\t\t"+str(int(vegchildno.get())*200)+'\n')
                    if nonvegadultno.get()!=0:
                        bill.insert(INSERT,"3\tNON-VEG(ADULT)\t\t"+str(nonvegadultno.get())+"\t\t"+str(int(nonvegadultno.get())*350)+'\n')
                    if nonvegchildno.get()!=0:
                        bill.insert(INSERT,"4\tNON-VEG(CHILD)\t\t"+str(nonvegchildno.get())+"\t\t"+str(int(nonvegchildno.get())*250)+'\n')    
                bill.insert(INSERT,"\t\t\t\t\t-----------\n")
                bill.insert(INSERT,"\t\t\tTOTAL\t\t" +str(price)+"\n")
                bill.insert(INSERT,"\t\t\t\t\t-----------\n")
                bill.insert(INSERT,"\tTAX = 5%(CGST+SGST)\n")
                bill.insert(INSERT,"\t\tCOST:\t\t\t" +str(((5/100)*price )+ price)+"\n\n")
                bill.insert(INSERT,"\t\tHOPE YOU ENJOYED OUR SERVICE!")   
                bill.place(x=600,y=0)
                                         
                #saving the bill in a notepad
                billcontent=bill.get(1.0,END)
                billfile=open(str(os.getcwd())+'/Restaurant bill folder'+"/"+str(bookingid.get())+".txt","w")
                billfile.write(billcontent)
                billfile.close()

                resetbutton.configure(state=ACTIVE)
                previousbutton.configure(state=ACTIVE)
#----------------------------------------------------------------------------------------------------------------------------------------------                                 
            else:
                costlabel.destroy()
                costlabel1.destroy()
                submitbutton.configure(state=ACTIVE)
                resetbutton.configure(state=ACTIVE)
                previousbutton.configure(state=ACTIVE)
        else:

            messagebox.showerror('Restaurant',"Enter proper credentials")

    def reset1():

        vegadultno.set(0)
        nonvegadultno.set(0)
        vegchildno.set(0)
        nonvegchildno.set(0)
        try:
            bill.destroy()
            bookingidlabel.destroy()
            bookingidentry.destroy()
            costlabel.destroy()
            costlabel1.destroy()
            Restaurant_screen.geometry('600x600')
            submitbutton.configure(state=ACTIVE)

        except:
            pass 

    def previous1():

        confirm_button.config(state=ACTIVE)
        mealdropdown.config(state=ACTIVE)

        vegadultlabel.destroy()
        vegadultoption.destroy()

        vegchildlabel.destroy()
        vegchildoption.destroy()

        nonvegadultlabel.destroy()
        nonvegadultoption.destroy()

        nonvegchildlabel.destroy()
        nonvegchildoption.destroy()

        submitbutton.destroy()
        resetbutton.destroy()
        previousbutton.destroy()
        try:
            bookingidlabel.destroy()
            bookingidentry.destroy()
            costlabel.destroy()
            costlabel1.destroy()
            bill.destroy()
            Restaurant_screen.geometry('600x600')
        except:
            pass  

    r=StringVar()

    def Restaurantguest():
        global vegadultno
        global vegchildno
        global nonvegadultno
        global nonvegchildno

        global vegadultlabel
        global vegchildlabel
        global nonvegadultlabel
        global nonvegchildlabel


        global vegadultoption
        global vegchildoption
        global nonvegadultoption
        global nonvegchildoption

        global previousbutton
        global resetbutton
        global submitbutton
        vegadultno=IntVar()

        vegchildno=IntVar()

        nonvegadultno=IntVar()

        nonvegchildno=IntVar()

        confirm_button.config(state=DISABLED)
        mealdropdown.config(state=DISABLED)

        vegadultlabel=Label(Restaurant_screen,text="VEG(Adults)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        vegadultlabel.place(x=110,y=250)

        vegadultoption=OptionMenu(Restaurant_screen,vegadultno,*[i for i in range(0,21)])
        vegadultoption.place(x=400,y=250)


        vegchildlabel=Label(Restaurant_screen,text="VEG(Kids)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        vegchildlabel.place(x=110,y=300)

        vegchildoption=OptionMenu(Restaurant_screen,vegchildno,*[i for i in range(0,21)])
        vegchildoption.place(x=400,y=300)
        

        nonvegadultlabel=Label(Restaurant_screen,text="NONVEG(Adults)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        nonvegadultlabel.place(x=110,y=350)

        nonvegadultoption=OptionMenu(Restaurant_screen,nonvegadultno,*[i for i in range(0,21)])
        nonvegadultoption.place(x=400,y=350)

        nonvegchildlabel=Label(Restaurant_screen,text="NONVEG(Kids)",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        nonvegchildlabel.place(x=110,y=400)

        nonvegchildoption=OptionMenu(Restaurant_screen,nonvegchildno,*[i for i in range(0,21)])
        nonvegchildoption.place(x=400,y=400)

        #submit button
        submitbutton=Button(Restaurant_screen,text='SUBMIT',fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',padx=20,command=submit1)
        submitbutton.place(x=100,y=460)

        #reset button
        resetbutton=Button(Restaurant_screen,text="RESET",fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',padx=20,command=reset1)
        resetbutton.place(x=220,y=460)    

        #previous page

        previousbutton=Button(Restaurant_screen,text="PREVIOUS",fg='darkgoldenrod1',bg='firebrick2',font='bahnschrift 15 bold',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',padx=20,command=previous1)
        previousbutton.place(x=340,y=460)

    #main screen
    meal=StringVar()
    meal.set("Breakfast")
    meallist=["Breakfast","Lunch","Dinner"]
    a=time.localtime()
    if a[3] not in[7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24]:
        messagebox.showerror("Restaurant","Restaurant service currently not available\nBREAKFAST:(8 AM-12 AM)\n\nLUNCH:(12 PM-5 PM)\n\nDINNER:(7 PM-12 PM)")
                                                    
    else:   

        Restaurant_screen=Toplevel()
        Restaurant_screen.geometry("600x600")
        Restaurant_screen.config(bg='firebrick2')
        Restaurant_screen.title('Restaurant')
        Restaurant_screen.iconbitmap(str(os.getcwd())+'/icons/'+'buffet.ico')
        
        # Restaurant label
        restaurant_label=Label(Restaurant_screen,text='Restaurant',fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 25 bold',padx=20)
        restaurant_label.place(x=210,y=10)
        cust=Label(Restaurant_screen,text="Customer Type",fg='darkgoldenrod1',bg='firebrick2',font = 'bahnschrift 15 bold',padx=20)
        cust.place(x=40,y=110) 
        Radiobutton(Restaurant_screen,text="Hotel Guest",font = 'bahnschrift 13 bold',variable=r,value="Hotel Guest",bg='firebrick2',fg='gold2',activeforeground='black',activebackground='red2').place(x=270,y=110)
        Radiobutton(Restaurant_screen,text="Restaurant Guest",font = 'bahnschrift 13 bold',variable=r,value="Restaurant Guest",bg='firebrick2',fg='gold2',activeforeground='black',activebackground='red2').place(x=400,y=110)
        menubutton=Button(Restaurant_screen,text="MENU",fg='gold2',bg='firebrick2',font='bahnschrift 15 bold',padx=20,command=menu)
        menubutton.place(x=480,y=40)
        confirm_button=Button(Restaurant_screen,text='Confirm',fg='darkgoldenrod1',bg='firebrick2',activebackground= 'firebrick2',activeforeground='darkgoldenrod1',font = 'bahnschrift 12 bold',command=findcustomertype)   
        confirm_button.place(x=370,y=170) 
        mealdropdown=OptionMenu(Restaurant_screen,meal,*meallist)
        mealdropdown.place(x=130,y=170)
        mealdropdown.config(bg="firebrick2",font="bahnschrift 13 bold",fg='gold2',activebackground= 'firebrick2',activeforeground='darkgoldenrod1')
        



    

    








