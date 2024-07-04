from tkinter import *
from tkinter import messagebox
import mysql.connector
import Checkin
import laundry
import Checkout
import Restaurant
import parking
import employees
import roomservice
main_screen = Tk()
main_screen.config(bg = '#12232E')
main_screen.geometry('600x700')
main_screen.title('Hotel')
main_screen.iconbitmap('hotel.ico')
connector = mysql.connector.connect(host = 'localhost', password = 'akhash', user = 'root',
database = 'project')
cursor = connector.cursor()
date_selected = StringVar()
month_selected = StringVar()
year_selected = StringVar()
18 | P a g e
Label(text = 'HOTEL MAJESTIC', padx = 20, font = ("bahnschrift", 20, "bold"), bg = '#12232E',
fg = 'white').grid(row = 0, column = 0, columnspan = 2)
def check_pwd(pwd_entered, password, pwd):
 if pwd_entered == password:
 for i in [x for x in range(26)]:
 statement = 'update customers set NAME = NULL ,OCCUPANTS = NULL ,CHECK_IN
= NULL,CUSTOMER_ID = NULL,PH_NUMBER = NULL, ROOM_TYPE = NULL,
STATUS = "FREE" where ROOM_NO = ' + str(i+100)
 cursor.execute(statement)
 connector.commit()
 statement = 'update laundry set SHIRTS = 0, PANTS = 0, OTHERS = 0, TOTAL = 0
where ROOM_NO = ' + str(i+100)
 cursor.execute(statement)
 connector.commit()
 statement = 'delete from restaurant'
 cursor.execute(statement)
 connector.commit()
 statement = 'delete from customer_history'
 cursor.execute(statement)
 connector.commit()
 statement = 'update parking set CAR_TYPE = NULL, L_PLATE = NULL, P_SLOT =
NULL, STATUS = NULL WHERE ROOM_NO = ' + str(i+100)
 cursor.execute(statement)
 connector.commit()
 statement = 'delete from laundry_history'
 cursor.execute(statement)
 connector.commit()
 pwd.destroy()
19 | P a g e
 Checkin.list_of_ids = []
 messagebox.showinfo('', 'Table Resetted')
 else:
 messagebox.showwarning('', 'Wrong Password')
def clear_data():
 password = 'rt'
 pwd = Toplevel()
 pwd.config(bg = '#12232E')
 pwd_label = Label(pwd, text = 'Enter the password', padx = 20, font = ("Times", 13, "bold"),
bg = '#12232E', fg = 'white')
 pwd_label.pack()
 pwd_entered = Entry(pwd, show = '*')
 pwd_entered.pack()
 pwd_button = Button(pwd, text = 'Enter', command = lambda: check_pwd(pwd_entered.get(),
password, pwd))
 pwd_button.pack()
#--------------------------------------------------------Buttons--------------------------------------------------
---------
Button_checkin = Button(main_screen, text='Check-In', font = ("times", 13, "italic"), relief =
RIDGE, padx = 20, pady = 15, bg = '#12232E', fg = 'white', activebackground = 'cornflower
blue', activeforeground = 'white', command = lambda: Checkin.checkin(date_selected,
month_selected, year_selected))
Button_checkout = Button(main_screen, text='Check-Out', font = ("times", 13, "italic"), relief =
RIDGE, padx = 17, pady = 15, bg = '#12232E', fg = 'white', activebackground = 'cornflower
blue', activeforeground = 'white', command = Checkout.Checkout)
Button_laundry = Button(main_screen, text='Laundry', font = ("times", 13, "italic"), relief =
RIDGE, padx = 24, pady = 15, bg = '#12232E', fg = 'white', activebackground = 'cornflower
blue', activeforeground = 'white', command = laundry.laundry)
20 | P a g e
Button_parking = Button(main_screen, text='Parking', font = ("times", 13, "italic"), relief =
RIDGE, padx = 24, pady = 15, bg = '#12232E', fg = 'white', activebackground = 'cornflower
blue', activeforeground = 'white', command = parking.parking)
Button_employees = Button(main_screen, text='Employees', font = ("times", 13, "italic"), relief
= RIDGE, padx = 17, pady = 15, bg = '#12232E', fg = 'white', activebackground = 'cornflower
blue', activeforeground = 'white', command = employees.employees)
Button_restaurant = Button(main_screen, text='Restaurant', font = ("times", 13, "italic"), relief =
RIDGE, padx = 17, pady = 15, bg = '#12232E', fg = 'white', activebackground = 'cornflower
blue', activeforeground = 'white', command = Restaurant.restaurant)
reset_button = Button(main_screen, text = 'Reset Data', font = ("times", 13, "italic"), relief =
RIDGE, bg = '#12232E', fg = 'white', padx = 17, pady = 15, command = clear_data)
room_service_button = Button(main_screen, text = 'Room Service', font = ("times", 13, "italic"),
relief = RIDGE, bg = '#12232E', fg = 'white', padx = 17, pady = 15, command =
roomservice.roomservice)
#-------------------------------------------Placing Buttons-----------------------------------------------------
------------
Button_checkin.grid(row = 1, column = 0, padx = 90, pady = (90,35))
Button_checkout.grid(row = 1, column = 1, padx = 90, pady = (90,35))
Button_laundry.grid(row = 2, column = 0, padx = 90, pady = 35)
Button_parking.grid(row = 2, column = 1, padx = 90, pady = 35)
room_service_button.grid(row = 3, column = 0, padx = 90, pady = 35)
Button_restaurant.grid(row = 3, column = 1, padx = 90, pady = 35)
Button_employees.grid(row = 4, column = 0, padx = 90, pady = 35)
reset_button.grid(row = 4, column = 1, padx = 90, pady = 35)
main_screen.mainloop()