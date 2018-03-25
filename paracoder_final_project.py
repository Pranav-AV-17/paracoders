import tkinter
from tkinter import Label, Entry, Tk , Toplevel, Button, OptionMenu, StringVar
from tkinter import *
master = Tk()
master.geometry('800x500')
master.title("Agri-Mitron")
master.configure(background="#1D2745")
email_dataset = ["1","aditya@paracoder.com","amogh@paracoder.com","pranav@paracoder.com","rasmita@paracoder.com"]
password_dataset = ["1","151060042","151060044","151060018","151061037"]
def sign_in():
   email_id = Email_entry.get()
   password = Password_entry.get()
   if (email_id in email_dataset):
       email_index = email_dataset.index(email_id)
       if password_dataset[email_index] == password:
           exist(master)
       else:
           win = Toplevel()
           message = "Please check your Password."
           Label(win, text=message, bg="#1D2745", fg="white", font=32).pack()
           Button(win, text='OK', command=win.destroy).pack()
   else:
       win = Toplevel()
       message = "Please check your Email ID."
       Label(win, text=message).pack()
       Button(win, text='OK', command=win.destroy).pack()
def sign_up():
    win = Toplevel()
    win.geometry('800x600')
    win.configure(background="#1D2745")
    Application_label = Label(win, text="Agri-Mitron", bg="#1D2745", fg="white", font=32)
    Application_label.place(x=375, y=150)
    name_label = Label(win, text="Name : ", bg="#1D2745", fg="white", font=32)
    name_label.place(x=250, y=200)
    name_entry = Entry(win)
    name_entry.place(x=350, y=200)
    email_id_label = Label(win, text="Email ID : ", bg="#1D2745", fg="white", font=32)
    email_id_label.place(x=250, y=250)
    email_id_entry = Entry(win)
    email_id_entry.place(x=350, y=250)
    password_label = Label(win, text="Password : ", bg="#1D2745", fg="white", font=32)
    password_label.place(x=250, y=300)
    password_entry = Entry(win)
    password_entry.place(x=350, y=300)
    Sign_up_button = tkinter.Button(win, text ="Sign Up", bg="#1D2745", fg="black", font=32, command = lambda:[email_dataset.append(email_id_entry.get()),password_dataset.append(password_entry.get()),exist(win)])
    Sign_up_button.place(x=375, y=350) 
def exist(self):
    self.destroy()
Application_label = Label(master, text="Agri-Mitron", bg="#1D2745", fg="white", font=32)
Application_label.place(x=375, y=150)
Email_label = Label(master, text="Email ID : ", bg="#1D2745", fg="white", font=32)
Email_label.place(x=250, y=200)
Email_entry = Entry(master)
Email_entry.place(x=350, y=200)
Password_label = Label(master, text="Password : ", bg="#1D2745", fg="white", font=32)
Password_label.place(x=250, y=250)
Password_entry = Entry(master)
Password_entry.place(x=350, y=250)
Sign_in_button = tkinter.Button(master, text ="Sign In", bg="#1D2745", fg="black", font=32, command = sign_in)
Sign_in_button.place(x=375, y=300)
Sign_up_button = tkinter.Button(master, text ="Sign Up", bg="#1D2745", fg="black", font=32, command = sign_up)
Sign_up_button.place(x=450, y=300)
master.mainloop()
from datetime import datetime
month = datetime.now().month
input_parameter = []
input_parameter_animal = []
if month < 5 or month >10:
    season = "Rabi"
else:
    season = "Kharif"
rainfall =100
import tkinter
root = Tk()
root.title("Agri-Mitron")
root.configure(background="#1D2745")
root.geometry('1000x1000')
app_label = Label(root, text="Agri-Mitron", bg="#1D2745", fg="white", font=32).place(x=490, y=150)
agri_label = Label(root, text="Agriculture", bg="#1D2745", fg="white", font=32).place(x=250, y=250)
husb_label = Label(root, text="Animal Husbandary", bg="#1D2745", fg="white", font=32).place(x=750, y=250)
choices0 = { 'Wheat','Rice','Cotton','Tea','Coffee','Maize','Sugarcane'}
tkvar0 = StringVar(root)
tkvar0.set('Select')
popupMenu0 = OptionMenu(root, tkvar0, *choices0)
crops_label = Label(root, text="Choose Your Crop", bg="#1D2745", fg="white", font=32).place(x=150, y=300)
popupMenu0.place(x=350, y=300)
land_label = Label(root, text="Enter Your Land Size(in Acres)", bg="#1D2745", fg="white", font=32).place(x=150, y=350)
Land_1 = Entry(root)
Land_1.place(x=350, y=350)
choices3 = { 'Coastal','Mountains','Plateau'}
tkvar3 = StringVar(root)
tkvar3.set('Select')
popupMenu3 = OptionMenu(root, tkvar3, *choices3)
crops_label = Label(root, text="Choose Your Region", bg="#1D2745", fg="white", font=32).place(x=150, y=400)
popupMenu3.place(x=350, y=400)
choices1 = {'Clay soil','Red soil','Black soil','Alluvial soil','Laterite soil'}
tkvar1 = StringVar(root)
tkvar1.set('Select')
popupMenu1 = OptionMenu(root, tkvar1, *choices1)
soil_label = Label(root, text="Choose Your Soil type", bg="#1D2745", fg="white", font=32).place(x=150, y=450)
popupMenu1.place(x=350, y=450)
choices2 = { 'Drip','Surface','Sprinkle'}
tkvar2 = StringVar(root)
tkvar2.set('Select')
popupMenu2 = OptionMenu(root, tkvar2, *choices2)
irrigation_label = Label(root, text="Choose Type of Irrigation", bg="#1D2745", fg="white", font=32).place(x=150, y=500)
popupMenu2.place(x=350, y=500)
investment_label = Label(root, text="Enter Your Budget", bg="#1D2745", fg="white", font=32).place(x=150, y=550)
Investment_1 = Entry(root)
Investment_1.place(x=350, y=550)
cow_label = Label(root, text="Cows", bg='#1D2745', fg="white", font=32).place(x=650, y=300)
Cow_1 = Entry(root, font=32)
Cow_1.place(x=750, y=300)
buff_label = Label(root, text="Buffalo", bg='#1D2745', fg="white", font=32).place(x=650, y=350)
Buff_1 = Entry(root, font=32)
Buff_1.place(x=750, y=350)
bull_label = Label(root, text="Bullocks", bg='#1D2745', fg="white", font=32).place(x=650, y=400)
Bull_1 = Entry(root, font=32)
Bull_1.place(x=750, y=400)
goat_label = Label(root, text="Goats", bg='#1D2745', fg="white", font=32).place(x=650, y=450)
Goat_1 = Entry(root, font=32)
Goat_1.place(x=750, y=450)
hens_label = Label(root, text="Hens", bg='#1D2745', fg='white', font=32).place(x=650, y=500)
Hens_1 = Entry(root, font=32)
Hens_1.place(x=750, y=500)
bee_label = Label(root, text="Bee Boxes", bg="#1D2745", fg="white", font=32).place(x=650, y=550)
Bee_1 = Entry(root, font=32, )
Bee_1.place(x=750, y=550)
B = Button(root, text = "Submit", bg="#1D2745", fg="black", font=32, command = lambda : [input_parameter.append(tkvar0.get()),input_parameter.append(season),input_parameter.append(tkvar3.get()),input_parameter.append(Land_1.get()),input_parameter.append(tkvar1.get()),input_parameter.append(tkvar2.get()),input_parameter.append(Investment_1.get()),input_parameter_animal.append(Cow_1.get()),input_parameter_animal.append(Buff_1.get()),input_parameter_animal.append(Bull_1.get()),input_parameter_animal.append(Goat_1.get()),input_parameter_animal.append(Hens_1.get()),input_parameter_animal.append(Bee_1.get()),exist(root)])
B.place(x=500, y=700)
root.mainloop()
win = Tk()
win.geometry('1400x900')
win.configure(background="#1D2745")
import rm, rm_ah
recommendations = rm.recommendation_agriculture(input_parameter)
print(input_parameter_animal)
crops = recommendations[0]
irrigation = recommendations[1]
npk = recommendations[2]
cost = recommendations[3]
recommendations_animal = rm_ah.recommendation_husbandary(input_parameter_animal[0:6],float(input_parameter[3])*0.409,crops)
total_N = recommendations_animal[0]
total_P = recommendations_animal[1]
total_K = recommendations_animal[2]
savings = recommendations_animal[3]
investment = recommendations_animal[4]
income = recommendations_animal[5]
print(investment)
rowspan = 0
for i in range(len(crops)):
    Label(win,text="Recommended Crops", bg='#1D2745', fg="white", font=32).place(x=150, y=150 + (50*i))
    Label(win,text=crops[i]).place(x=200, y=200+ (50*i))
    Label(win,text="Recommended Irrigation", bg='#1D2745', fg="white", font=32).place(x=350, y=150+ (50*i))
    Label(win,text=irrigation).place(x=400, y=200+ (50*i))
    k=round(float(npk[i][0]),2)
    Label(win,text="Recommended N in Kg", bg='#1D2745', fg="white", font=32).place(x=550, y=150+ (50*i))
    Label(win,text=str(k)).place(x=600, y=200+ (50*i))
    k=round(float(npk[i][1]),2)
    Label(win,text="Recommended P in Kg", bg='#1D2745', fg="white", font=32).place(x=750, y=150+ (50*i))
    Label(win,text=str(k)).place(x=800, y=200+ (50*i))
    k=round(float(npk[i][2]),2)
    Label(win,text="Recommended k in Kg", bg='#1D2745', fg="white", font=32).place(x=950, y=150+ (50*i))
    Label(win,text=str(k)).place(x=1000, y=200+ (50*i))
    k=round(float(cost[i]),2)
    Label(win,text="Expected Cost", bg='#1D2745', fg="white", font=32).place(x=1150, y=150+ (50*i))
    Label(win,text=str(k)).place(x=1200, y=200+ (50*i))
    rowspan = 200 + (50*i)
rowspan += 100
k=round(float(total_N),2)
Label(win,text="Total N in Kg", bg='#1D2745', fg="white", font=32).place(x=150, y=rowspan)
Label(win,text=str(k)).place(x=200, y=rowspan + 50)
k=round(float(total_P),2)
Label(win,text="Total P in Kg", bg='#1D2745', fg="white", font=32).place(x=350, y=rowspan)
Label(win,text=str(k)).place(x=400, y=rowspan + 50)
k=round(float(total_K),2)
Label(win,text="Total K in Kg", bg='#1D2745', fg="white", font=32).place(x=550, y=rowspan)
Label(win,text=str(k)).place(x=600, y=rowspan + 50)
k=round(float(savings),2)
Label(win,text="Total Fertilizer Savings", bg='#1D2745', fg="white", font=32).place(x=750, y=rowspan)
Label(win,text=str(k)).place(x=800, y=rowspan + 50)
k=round(float(income),2)
Label(win,text="Total income from animal husbandary", bg='#1D2745', fg="white", font=32).place(x=950, y=rowspan)
Label(win,text=str(k)).place(x=1000, y=rowspan + 50)
rowspan += 150
for i in range(len(crops)):
    Label(win,text="Recommended Crops", bg='#1D2745', fg="white", font=32).place(x=150, y=rowspan+ (50*i))
    Label(win,text=crops[i],fg='#1D2745', bg="white", font=32).place(x=200, y=rowspan+ (50*i)+50)
    Label(win,text="Investment needed for Apiculture and Pisciculture", bg='#1D2745', fg="white", font=32).place(x=350, y=rowspan+ (50*i))
    Label(win,text=investment[i], fg='#1D2745', bg="white", font=32).place(x=450, y=rowspan+ (50*i)+50)
    rowspan = rowspan + (50*i)
rowspan += 150
ok_button = tkinter.Button(win, text ="   Ok   ", fg='#1D2745', bg="white", font=64 ,command = win.destroy)
ok_button.place(x=650, y=rowspan) 
win.mainloop()