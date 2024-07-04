from tkinter import *
from tkinter import messagebox
import mysql.connector
connector = mysql.connector.connect(host = 'localhost', password = 'akhash', user = 'root', database = 'project')
cursor = connector.cursor()
class labels:
    def __init__(self, screen, t, x, y):
        self = Label(screen, text = t, bg = 'light slate grey', fg = 'black', font = 'bahnschrift 18 bold')
        self.place(x = x, y = y)
def check_none(x):
    for i in x:
        if i == None:
            return True
    return False
def rooms_slots():
    statement = 'SELECT ROOM_NO FROM PARKING WHERE STATUS = "OCCUPIED"'
    cursor.execute(statement)
    rooms = [i[0] for i in cursor]
    statement = 'SELECT P_SLOT FROM PARKING WHERE P_SLOT IS NOT NULL'
    cursor.execute(statement)
    slots = [i[0] for i in cursor]
    if check_none(slots):
        slots = []

    slots2 = [j for j in range(1,26)]

    for x in slots:
        if x in slots2:
            slots2.remove(x)

    return slots2, rooms   
def parking():
    parking_screen = Toplevel()
    parking_screen.configure(bg = 'light slate grey')
    parking_screen.title("Parking")
    parking_screen.geometry('600x600')

    room_selected = IntVar()
    type_selected = StringVar()
    slot_selected = IntVar()

    def submit():
        if type_selected.get() == None or plateNo_entry.get == None or slot_selected.get() == None:
            messagebox.showerror('', 'Enter proper credentials')
            parking_screen.destroy()
            parking()
        statement = 'UPDATE PARKING SET CAR_TYPE = "' + str(type_selected.get()) + '", L_PLATE = "' + str(plateNo_entry.get()) + '", P_SLOT = ' + str(slot_selected.get()) + ' WHERE ROOM_NO = ' + str(room_selected.get())
        cursor.execute(statement)
        connector.commit()
        parking_screen.destroy()
        messagebox.showinfo('', 'Updated')

    car_types = ['SUV', 'SEDAN', 'HATCHBACK', 'CONVERTIBLE', 'SPORT']

    Label(parking_screen, text = 'Parking', font = 'bahnschrift 25 bold', bg = 'light slate grey').place(x = 235, y = 5)
    labels(parking_screen, 'Room Number', 50, 150)
    labels(parking_screen, 'Car Type', 50, 240)
    labels(parking_screen, 'Licence Plate Number', 50, 330)
    labels(parking_screen, 'Parking Slot', 50, 420)

    slots, rooms = rooms_slots()

    if rooms == []:
        parking_screen.destroy()
        messagebox.showerror('','No customers available')
        return

    room_menu = OptionMenu(parking_screen, room_selected, *rooms)
    room_menu.place(x = 470, y = 150)
    type_menu = OptionMenu(parking_screen, type_selected, *car_types)
    type_menu.place(x = 470, y = 240)
    plateNo_entry = Entry(parking_screen, font = 'bahnschrift 13 bold', width = 13)
    plateNo_entry.place(x = 470, y = 330)
    slots_menu = OptionMenu(parking_screen, slot_selected, *slots)
    slots_menu.place(x = 470, y = 420)
    submit_button = Button(parking_screen, text = 'Submit', font = 'bahnschrift 18 bold', bg = 'light slate grey', activebackground = 'light slate grey', command = submit)
    submit_button.place(x = 250, y = 520)
