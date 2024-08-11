from tkinter import *
from tkinter import messagebox
from datetime import datetime
import csv
import pandas as pd

root = Tk()
root.geometry("1280x720")
root.title("BILL SYSTEM")
mainlabel=Label(text=" CAFE GOOD FIRE ",font="Helvetica 25 bold",bd=10,relief=RIDGE)
mainlabel.pack(fill=X)

def fn_valid():
        first=n.get()
        if len(first)==0:
            msg.config(text="first name is must")
        else:
            try:
                if any(ch.isdigit() for ch in first):
                    msg.config(text="it cannot contain digit!")
                elif len(first)<=2:
                    msg.config(text="lenght is too small!")
                elif len(first)>15:
                    msg.config(text="Huge name!")
                else:
                    msg.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True

def ph_valid():
        first=ph.get()
        if len(first)==0:
            msg3.config(text="phone number is must")
        else:
            try:
                if any(ch.isalpha() for ch in first):
                    msg3.config(text="it cannot contain alphabet!")
                elif len(first)<10:
                    msg3.config(text="must be of 10 numbers!")
                elif len(first)>10:
                    msg3.config(text="invalid number!")
                else:
                    msg3.config(text="")
            except Exception as ep:
                messagebox.showerror("error",ep)
        return True

def increase_quantity():
    current_value = int(bu1["text"])
    bu1["text"] = str(current_value + 1)
def decrease_quantity():
    current_value = int(bu1["text"])
    if current_value > 0:
        bu1["text"] = str(current_value - 1)

def increase_quantity1():
    current_value = int(bu2["text"])
    bu2["text"] = str(current_value + 1)
def decrease_quantity1():
    current_value = int(bu2["text"])
    if current_value > 0:
        bu2["text"] = str(current_value - 1)

def increase_quantity2():
    current_value = int(bu3["text"])
    bu3["text"] = str(current_value + 1)
def decrease_quantity2():
    current_value = int(bu3["text"])
    if current_value > 0:
        bu3["text"] = str(current_value - 1)

def increase_quantity3():
    current_value = int(bu4["text"])
    bu4["text"] = str(current_value + 1)
def decrease_quantity3():
    current_value = int(bu4["text"])
    if current_value > 0:
        bu4["text"] = str(current_value - 1)

def increase_quantity4():
    current_value = int(gb1["text"])
    gb1["text"] = str(current_value + 1)
def decrease_quantity4():
    current_value = int(gb1["text"])
    if current_value > 0:
        gb1["text"] = str(current_value - 1)

def increase_quantity5():
    current_value = int(gb2["text"])
    gb2["text"] = str(current_value + 1)
def decrease_quantity5():
    current_value = int(gb2["text"])
    if current_value > 0:
        gb2["text"] = str(current_value - 1)

def increase_quantity6():
    current_value = int(ta1["text"])
    ta1["text"] = str(current_value + 1)
def decrease_quantity6():
    current_value = int(ta1["text"])
    if current_value > 0:
        ta1["text"] = str(current_value - 1)

def increase_quantity7():
    current_value = int(ta2["text"])
    ta2["text"] = str(current_value + 1)
def decrease_quantity7():
    current_value = int(ta2["text"])
    if current_value > 0:
        ta2["text"] = str(current_value - 1)

def increase_quantity8():
    current_value = int(pas1["text"])
    pas1["text"] = str(current_value + 1)
def decrease_quantity8():
    current_value = int(pas1["text"])
    if current_value > 0:
        pas1["text"] = str(current_value - 1)

def increase_quantity9():
    current_value = int(pas2["text"])
    pas2["text"] = str(current_value + 1)
def decrease_quantity9():
    current_value = int(pas2["text"])
    if current_value > 0:
        pas2["text"] = str(current_value - 1)

def increase_quantity10():
    current_value = int(fr1["text"])
    fr1["text"] = str(current_value + 1)
def decrease_quantity10():
    current_value = int(fr1["text"])
    if current_value > 0:
        fr1["text"] = str(current_value - 1)

def increase_quantity11():
    current_value = int(fr2["text"])
    fr2["text"] = str(current_value + 1)
def decrease_quantity11():
    current_value = int(fr2["text"])
    if current_value > 0:
        fr2["text"] = str(current_value - 1)

def increase_quantity12():
    current_value = int(be1["text"])
    be1["text"] = str(current_value + 1)
def decrease_quantity12():
    current_value = int(be1["text"])
    if current_value > 0:
        be1["text"] = str(current_value - 1)

def increase_quantity13():
    current_value = int(be2["text"])
    be2["text"] = str(current_value + 1)
def decrease_quantity13():
    current_value = int(be2["text"])
    if current_value > 0:
        be2["text"] = str(current_value - 1)

def increase_quantity14():
    current_value = int(be3["text"])
    be3["text"] = str(current_value + 1)
def decrease_quantity14():
    current_value = int(be3["text"])
    if current_value > 0:
        be3["text"] = str(current_value - 1)

def increase_quantity15():
    current_value = int(be4["text"])
    be4["text"] = str(current_value + 1)
def decrease_quantity15():
    current_value = int(be4["text"])
    if current_value > 0:
        be4["text"] = str(current_value - 1)

def increase_quantity16():
    current_value = int(bu5["text"])
    bu5["text"] = str(current_value + 1)
def decrease_quantity16():
    current_value = int(bu5["text"])
    if current_value > 0:
        bu5["text"] = str(current_value - 1)

def increase_quantity17():
    current_value = int(fr3["text"])
    fr3["text"] = str(current_value + 1)
def decrease_quantity17():
    current_value = int(fr3["text"])
    if current_value > 0:
        fr3["text"] = str(current_value - 1)

def increase_quantity18():
    current_value = int(cc1["text"])
    cc1["text"] = str(current_value + 1)
def decrease_quantity18():
    current_value = int(cc1["text"])
    if current_value > 0:
        cc1["text"] = str(current_value - 1)

def increase_quantity19():
    current_value = int(cc2["text"])
    cc2["text"] = str(current_value + 1)
def decrease_quantity19():
    current_value = int(cc2["text"])
    if current_value > 0:
        cc2["text"] = str(current_value - 1)

menuframe=Frame(root,bd=10,relief=SUNKEN)
menuframe.pack(fill=X,side=TOP)

name =Label(menuframe,text="Name*:-",font="bold")
Phone =Label(menuframe,text="Contact number*:-",font="bold")
discount =Label(menuframe,text="Discount:-",font="bold")
bill_load =Label(menuframe,text="Load this bill:-",font="bold")

name.grid(row=0,column=0,ipadx=5,ipady=2)
Phone.grid(row=0,column=3,ipadx=5,ipady=2)
discount.grid(row=0,column=7,ipadx=5,ipady=2)
bill_load.grid(row=1,column=0,ipadx=5,ipady=2)

n=StringVar()
ph=StringVar()
d=StringVar()
bl=StringVar()

fn_entry= Entry(menuframe,textvariable=n,validate="focusout",validatecommand=fn_valid)
msg=Label(menuframe,text="",fg="red")
ln_entry= Entry(menuframe,textvariable=ph,validate="focusout",validatecommand=ph_valid)
msg3=Label(menuframe,text="",fg="red")
d_entry= Entry(menuframe,textvariable=d)
bill_entry= Entry(menuframe,textvariable=bl)
search_but=Button(menuframe,text="Load",bg="lightgrey",height=1,width=10,font="serif 10 bold")
search_but.grid(row=1,column=2)

fn_entry.grid(row=0,column=1)
msg.grid(row=0,column=2)
ln_entry.grid(row=0,column=4)
msg3.grid(row=0,column=5)
d_entry.grid(row=0,column=8)
bill_entry.grid(row=1,column=1)

button_frame=Frame(root,bd=10,relief=SUNKEN)
button_frame.pack(anchor="nw",side="top",fill=X)


#Bill display area initialisation
display_frame=Frame(button_frame,height=300,width=500,bd=5,relief=RIDGE)
display_frame.place(x=650,y=10)
ttl=Label(display_frame,text="Bill area",font="arial 13 bold",bd=5,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(display_frame,orient=VERTICAL)
display_text=Text(display_frame,yscrollcommand=scrol_y.set,height=26,width=60)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=display_text.yview)
display_text.pack()

#Burgers to select 
Burgers =Label(button_frame,text="BURGERS",font="timesnewroman 14 bold").grid(row=0,column=0)

B1 =Label(button_frame,text="1)Veggie Burger",font="bold 13").grid(row=1,column=0)
bur1=StringVar()
global bu1
bu1 =Label(button_frame, text="0",font="bold 11")
bu1.grid(column=6,row=1)
increase_button = Button(button_frame, text="+", command=increase_quantity)
increase_button.grid(column=7,row=1)
decrease_button = Button(button_frame, text="-", command=decrease_quantity)
decrease_button.grid(column=5,row=1)

B2 =Label(button_frame,text="2)Paneer Burger",font="bold 13").grid(row=2,column=0)
bur2=StringVar()
bu2 =Label(button_frame, text="0",font="bold 11")
bu2.grid(column=6,row=2)
increase_button = Button(button_frame, text="+", command=increase_quantity1)
increase_button.grid(column=7,row=2)
decrease_button = Button(button_frame, text="-", command=decrease_quantity1)
decrease_button.grid(column=5,row=2)

B3 =Label(button_frame,text="3)Grilled Panner Burger",font="bold 13").grid(row=3,column=0)
bur3=StringVar()
bu3 =Label(button_frame, text="0",font="bold 11")
bu3.grid(column=6,row=3)
increase_button = Button(button_frame, text="+", command=increase_quantity2)
increase_button.grid(column=7,row=3)
decrease_button = Button(button_frame, text="-", command=decrease_quantity2)
decrease_button.grid(column=5,row=3)

B4 =Label(button_frame,text="4)Chicken Burger",font="bold 13").grid(row=4,column=0)
bur4=StringVar()
bu4 =Label(button_frame, text="0",font="bold 11")
bu4.grid(column=6,row=4)
increase_button = Button(button_frame, text="+", command=increase_quantity3)
increase_button.grid(column=7,row=4)
decrease_button = Button(button_frame, text="-", command=decrease_quantity3)
decrease_button.grid(column=5,row=4)

B5 =Label(button_frame,text="5)Grilled Chicken Burger",font="bold 13").grid(row=5,column=0)
bur5=StringVar()
bu5 =Label(button_frame, text="0",font="bold 11")
bu5.grid(column=6,row=5)
increase_button = Button(button_frame, text="+", command=increase_quantity16)
increase_button.grid(column=7,row=5)
decrease_button = Button(button_frame, text="-", command=decrease_quantity16)
decrease_button.grid(column=5,row=5)

#Garlic bread to select
Garlic_bread =Label(button_frame,text="GARLIC BREAD",font="timesnewroman 14 bold").grid(row=6,column=0)

g1 =Label(button_frame,text="1)Cheese Garlic Bread",font="bold 13").grid(row=7,column=0)
g_b1=StringVar()
gb1 =Label(button_frame, text="0",font="bold 11")
gb1.grid(column=6,row=7)
increase_button = Button(button_frame, text="+", command=increase_quantity4)
increase_button.grid(column=7,row=7)
decrease_button = Button(button_frame, text="-", command=decrease_quantity4)
decrease_button.grid(column=5,row=7)

g2 =Label(button_frame,text="2)Paneer Cheese Garlic Bread",font="bold 13").grid(row=8,column=0)
g_b2=StringVar()
gb2 =Label(button_frame, text="0",font="bold 11")
gb2.grid(column=6,row=8)
increase_button = Button(button_frame, text="+", command=increase_quantity5)
increase_button.grid(column=7,row=8)
decrease_button = Button(button_frame, text="-", command=decrease_quantity5)
decrease_button.grid(column=5,row=8)

#Tacos
tacos =Label(button_frame,text="TACOS",font="timesnewroman 14 bold").grid(row=6,column=9)

t1 =Label(button_frame,text="1)Veggie Tacos",font="bold 13").grid(row=7,column=9)
tac1=StringVar()
ta1 =Label(button_frame, text="0",font="bold 11")
ta1.grid(column=11,row=7)
increase_button = Button(button_frame, text="+", command=increase_quantity6)
increase_button.grid(column=12,row=7)
decrease_button = Button(button_frame, text="-", command=decrease_quantity6)
decrease_button.grid(column=10,row=7)

t2 =Label(button_frame,text="2)Chicken Tacos",font="bold 13").grid(row=8,column=9)
tac2=StringVar()
ta2 =Label(button_frame, text="0",font="bold 11")
ta2.grid(column=11,row=8)
increase_button = Button(button_frame, text="+", command=increase_quantity7)
increase_button.grid(column=12,row=8)
decrease_button = Button(button_frame, text="-", command=decrease_quantity7)
decrease_button.grid(column=10,row=8)

#Pastas to select
Pasta =Label(button_frame,text="PASTAS",font="timesnewroman 14 bold").grid(row=15,column=9)

pa1 =Label(button_frame,text="1)Peri-peri Sauce",font="bold 13").grid(row=16,column=9)
past1=StringVar()
pas1 =Label(button_frame, text="0",font="bold 11")
pas1.grid(column=11,row=16)
increase_button = Button(button_frame, text="+", command=increase_quantity8)
increase_button.grid(column=12,row=16)
decrease_button = Button(button_frame, text="-", command=decrease_quantity8)
decrease_button.grid(column=10,row=16)

pa2 =Label(button_frame,text="2)White Sauce",font="bold 13").grid(row=17,column=9)
past2=StringVar()
pas2 =Label(button_frame, text="0",font="bold 11")
pas2.grid(column=11,row=17)
increase_button = Button(button_frame, text="+", command=increase_quantity9)
increase_button.grid(column=12,row=17)
decrease_button = Button(button_frame, text="-", command=decrease_quantity9)
decrease_button.grid(column=10,row=17)

#FRIES to select
fries =Label(button_frame,text="FRIES",font="timesnewroman 14 bold").grid(row=15,column=0)

f1 =Label(button_frame,text="1)Regular Fries",font="bold 13").grid(row=16,column=0)
fri1=StringVar()
fr1 =Label(button_frame, text="0",font="bold 11")
fr1.grid(column=6,row=16)
increase_button = Button(button_frame, text="+", command=increase_quantity10)
increase_button.grid(column=7,row=16)
decrease_button = Button(button_frame, text="-", command=decrease_quantity10)
decrease_button.grid(column=5,row=16)

f2 =Label(button_frame,text="2)Peri-peri Fries",font="bold 13").grid(row=17,column=0)
fri2=StringVar()
fr2 =Label(button_frame, text="0",font="bold 11")
fr2.grid(column=6,row=17)
increase_button = Button(button_frame, text="+", command=increase_quantity11)
increase_button.grid(column=7,row=17)
decrease_button = Button(button_frame, text="-", command=decrease_quantity11)
decrease_button.grid(column=5,row=17)

f3 =Label(button_frame,text="3)Veggie Fries",font="bold 13").grid(row=18,column=0)
fri3=StringVar()
fr3 =Label(button_frame, text="0",font="bold 11")
fr3.grid(column=6,row=18)
increase_button = Button(button_frame, text="+", command=increase_quantity17)
increase_button.grid(column=7,row=18)
decrease_button = Button(button_frame, text="-", command=decrease_quantity17)
decrease_button.grid(column=5,row=18)

#Shakes to select
Beverages =Label(button_frame,text="FREAK SHAKES",font="timesnewroman 14 bold").grid(row=19,column=0)

b1 =Label(button_frame,text="1)Banana Cracker",font="bold 13").grid(row=20,column=0)
bev1=StringVar()
be1 =Label(button_frame, text="0",font="bold 11")
be1.grid(column=6,row=20)
increase_button = Button(button_frame, text="+", command=increase_quantity12)
increase_button.grid(column=7,row=20)
decrease_button = Button(button_frame, text="-", command=decrease_quantity12)
decrease_button.grid(column=5,row=20)

b2 =Label(button_frame,text="2)Milk Shake and cookies",font="bold 13").grid(row=21,column=0)
bev2=StringVar()
be2 =Label(button_frame, text="0",font="bold 11")
be2.grid(column=6,row=21)
increase_button = Button(button_frame, text="+", command=increase_quantity13)
increase_button.grid(column=7,row=21)
decrease_button = Button(button_frame, text="-", command=decrease_quantity13)
decrease_button.grid(column=5,row=21)

b3 =Label(button_frame,text="3)Kit-Kat Choco Pie",font="bold 13").grid(row=22,column=0)
bev3=StringVar()
be3 =Label(button_frame, text="0",font="bold 11")
be3.grid(column=6,row=22)
increase_button = Button(button_frame, text="+", command=increase_quantity14)
increase_button.grid(column=7,row=22)
decrease_button = Button(button_frame, text="-", command=decrease_quantity14)
decrease_button.grid(column=5,row=22)

b4 =Label(button_frame,text="4)Death by Chocolate",font="bold 13").grid(row=23,column=0)
bev4=StringVar()
be4 =Label(button_frame, text="0",font="bold 11")
be4.grid(column=6,row=23)
increase_button = Button(button_frame, text="+", command=increase_quantity15)
increase_button.grid(column=7,row=23)
decrease_button = Button(button_frame, text="-", command=decrease_quantity15)
decrease_button.grid(column=5,row=23)

#Cold coffee to select
coffee =Label(button_frame,text="COLD COFFEE",font="timesnewroman 14 bold").grid(row=19,column=9)

c1 =Label(button_frame,text="1)Cold Coffee",font="bold 13").grid(row=20,column=9)
coc1=StringVar()
cc1 =Label(button_frame, text="0",font="bold 11")
cc1.grid(column=11,row=20)
increase_button = Button(button_frame, text="+", command=increase_quantity18)
increase_button.grid(column=12,row=20)
decrease_button = Button(button_frame, text="-", command=decrease_quantity18)
decrease_button.grid(column=10,row=20)

c2 =Label(button_frame,text="2)Frappuccino",font="bold 13").grid(row=21,column=9)
coc2=StringVar()
cc2 =Label(button_frame, text="0",font="bold 11")
cc2.grid(column=11,row=21)
increase_button = Button(button_frame, text="+", command=increase_quantity19)
increase_button.grid(column=12,row=21)
decrease_button = Button(button_frame, text="-", command=decrease_quantity19)
decrease_button.grid(column=10,row=21)

button_frame2=Frame(root,bd=10,relief=SUNKEN)
button_frame2.pack(anchor="nw",side="top")

def reset_bill():
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    d_entry.delete(0,END)
    #burger
    current_value = int(bu1["text"])
    bu1["text"] = str(current_value - current_value)
    current_value1 = int(bu2["text"])
    bu2["text"] = str(current_value1 - current_value1)
    current_value2 = int(bu3["text"])
    bu3["text"] = str(current_value2 - current_value2)
    current_value3 = int(bu4["text"])
    bu4["text"] = str(current_value3 - current_value3)
    current_value16 = int(bu5["text"])
    bu5["text"] = str(current_value16 - current_value16)
    #garlic bread
    current_value4 = int(gb1["text"])
    gb1["text"] = str(current_value4 - current_value4)
    current_value5 = int(gb2["text"])
    gb2["text"] = str(current_value5 - current_value5)
    #tacos
    current_value6 = int(ta1["text"])
    ta1["text"] = str(current_value6 - current_value6)
    current_value7 = int(ta2["text"])
    ta2["text"] = str(current_value7 - current_value7)
    #pasta
    current_value8 = int(pas1["text"])
    pas1["text"] = str(current_value8 - current_value8)
    current_value9 = int(pas2["text"])
    pas2["text"] = str(current_value9 - current_value9)
    #fries
    current_value10 = int(fr1["text"])
    fr1["text"] = str(current_value10 - current_value10)
    current_value11 = int(fr2["text"])
    fr2["text"] = str(current_value11 - current_value11)
    current_value17 = int(fr3["text"])
    fr3["text"] = str(current_value17 - current_value17)
    #beverages
    current_value12 = int(be1["text"])
    be1["text"] = str(current_value12 - current_value12)
    current_value13 = int(be2["text"])
    be2["text"] = str(current_value13 - current_value13)
    current_value14 = int(be3["text"])
    be3["text"] = str(current_value14 - current_value14)
    current_value15 = int(be4["text"])
    be4["text"] = str(current_value15 - current_value15)
    #cold coffee
    current_value18 = int(cc1["text"])
    cc1["text"] = str(current_value18 - current_value18)
    current_value19 = int(cc2["text"])
    cc2["text"] = str(current_value19 - current_value19)

    #bill display reset
    display_text.delete("1.0","end")
    tt.set("0000.00")

now = datetime.now()
date_today= now.strftime("%d/%m/%Y")
time_today= now.strftime("%H:%M")

def display_bill():
    if display_text:
        display_text.delete("1.0","end")

    csv_file="cafe_datails.csv"
    col_name="Bill number"
    df=pd.read_csv(csv_file)
    global bill_value
    bill_value=df[col_name].iloc[-1]

    display_text.insert(END,f"			CAFE GOOD FIRE\n")
    display_text.insert(END,f"\n")
    display_text.insert(END,f"15 Empire building,waghodia road,\n")
    display_text.insert(END,f"Vadodara - 390013\n")
    display_text.insert(END,f"\n")
    display_text.insert(END,f"GST number:12683964839\n")
    display_text.insert(END,f"Customer name:\t{n.get()}\n")
    display_text.insert(END,f"Customer Phone number:\t{ph.get()}\n")
    display_text.insert(END,f"Date and time:\t{date_today}\t{time_today}\n")
    display_text.insert(END,f"Bill number:\t{bill_value+1}\n")
    display_text.insert(END,f"============================================================\n")
    display_text.insert(END,f"Dish                        Quantity              Price\n")
    display_text.insert(END,f"============================================================\n")

    #burger display in bill
    if int(bu1["text"]) > 0:
        global a1
        a1=int(bu1["text"])
        global a1_price
        a1_price=a1*129
        display_text.insert(END,f" Veggie Burger               {a1}                     {a1_price}\n")
    else:
        a1_price=0

    if int(bu2["text"]) > 0:
        global a2
        a2=int(bu2["text"])
        global a2_price
        a2_price=a2*159
        display_text.insert(END,f" Paneer Burger               {a2}                     {a2_price}\n")
    else:
        a2_price=0

    if int(bu3["text"]) > 0:
        global a3
        a3=int(bu3["text"])
        global a3_price
        a3_price=a3*179
        display_text.insert(END,f" Grilled Paneer Burger       {a3}                     {a3_price}\n")
    else:
        a3_price=0

    if int(bu4["text"]) > 0:
        global a4
        a4=int(bu4["text"])
        global a4_price
        a4_price=a4*199
        display_text.insert(END,f" Chicken Burger              {a4}                     {a4_price}\n")
    else:
        a4_price=0

    if int(bu5["text"]) > 0:
        global a17
        a17=int(bu5["text"])
        global a17_price
        a17_price=a17*219
        display_text.insert(END,f" Grilled Chicken Burger      {a17}                     {a17_price}\n")
    else:
        a17_price=0

    #garlic bread display in bill
    if int(gb1["text"]) > 0:
        global a5
        a5=int(gb1["text"])
        global a5_price
        a5_price=a5*129
        display_text.insert(END,f" Cheese Garlic Bread         {a5}                     {a5_price}\n")
    else:
        a5_price=0

    if int(gb2["text"]) > 0:
        global a6
        a6=int(gb2["text"])
        global a6_price
        a6_price=a6*149
        display_text.insert(END,f" Paneer-Cheese Garlic Bread  {a6}                     {a6_price}\n")
    else:
        a6_price=0

    #tacos display in bill
    if int(ta1["text"]) > 0:
        global a7
        a7=int(ta1["text"])
        global a7_price
        a7_price=a7*149
        display_text.insert(END,f" Veggie Tacos                {a7}                     {a7_price}\n")
    else:
        a7_price=0

    if int(ta2["text"]) > 0:
        global a8
        a8=int(ta2["text"])
        global a8_price
        a8_price=a8*169
        display_text.insert(END,f" Chicken Tacos               {a8}                     {a8_price}\n")
    else:
        a8_price=0

    #Pasta display in bill
    if int(pas1["text"]) > 0:
        global a9
        a9=int(pas1["text"])
        global a9_price
        a9_price=a9*139
        display_text.insert(END,f" Peri-Peri Sauce             {a9}                     {a9_price}\n")
    else:
        a9_price=0

    if int(pas2["text"]) > 0:
        global a10
        a10=int(pas2["text"])
        global a10_price
        a10_price=a10*159
        display_text.insert(END,f" White Sauce                 {a10}                     {a10_price}\n")
    else:
        a10_price=0

    #fries display in bill
    if int(fr1["text"]) > 0:
        global a11
        a11=int(fr1["text"])
        global a11_price
        a11_price=a11*79
        display_text.insert(END,f" Regular Fries               {a11}                     {a11_price}\n")
    else:
        a11_price=0

    if int(fr2["text"]) > 0:
        global a12
        a12=int(fr2["text"])
        global a12_price
        a12_price=a12*109
        display_text.insert(END,f" Peri-Peri Fries             {a12}                     {a12_price}\n")
    else:
        a12_price=0

    if int(fr3["text"]) > 0:
        global a18
        a18=int(fr3["text"])
        global a18_price
        a18_price=a18*129
        display_text.insert(END,f" Veggie Fries                {a18}                     {a18_price}\n")
    else:
        a18_price=0

    #Beverages display in bill
    if int(be1["text"]) > 0:
        global a13
        a13=int(be1["text"])
        global a13_price
        a13_price=a13*199
        display_text.insert(END,f" Banana Cracker              {a13}                     {a13_price}\n")
    else:
        a13_price=0

    if int(be2["text"]) > 0:
        global a14
        a14=int(be2["text"])
        global a14_price
        a14_price=a14*199
        display_text.insert(END,f" Milk-shake and cookies      {a14}                     {a14_price}\n")
    else:
        a14_price=0

    if int(be3["text"]) > 0:
        global a15
        a15=int(be3["text"])
        global a15_price
        a15_price=a15*229
        display_text.insert(END,f" Kit-Kat Choco pie           {a15}                     {a15_price}\n")
    else:
        a15_price=0

    if int(be4["text"]) > 0:
        global a16
        a16=int(be4["text"])
        global a16_price
        a16_price=a16*249
        display_text.insert(END,f" Death by Chocolate          {a16}                     {a16_price}\n")
    else:
        a16_price=0

    #Cold coffee display in bill
    if int(cc1["text"]) > 0:
        global a19
        a19=int(cc1["text"])
        global a19_price
        a19_price=a19*129
        display_text.insert(END,f" Cold Coffee                 {a19}                     {a19_price}\n")
    else:
        a19_price=0

    if int(cc2["text"]) > 0:
        global a20
        a20=int(cc2["text"])
        global a20_price
        a20_price=a20*139
        display_text.insert(END,f" Frappuccino                 {a20}                     {a20_price}\n")
    else:
        a20_price=0

    #sub-total
    global sub_t
    sub_t=a1_price+a2_price+a3_price+a4_price+a5_price+a6_price+a7_price+a8_price+a9_price+a10_price+a11_price+a12_price+a13_price+a14_price+a15_price+a16_price+a17_price+a18_price+a19_price+a20_price

    #sgst
    global sgst_price
    sgst_price=(2.5*sub_t)/100

    #cgst
    global cgst_price
    cgst_price=(2.5*sub_t)/100

    display_text.insert(END,f"============================================================\n")
    display_text.insert(END,f"                                      Sub total :- {sub_t}\n")
    display_text.insert(END,f"============================================================\n")
    display_text.insert(END,f"SGST  2.5%                                        \t{sgst_price}\n")
    display_text.insert(END,f"CGST  2.5%                                        \t{cgst_price}\n")
    global disc
    disc=d.get()
    if disc=="":
        disc=0
    if int(disc)>0:
        global discount_ovr
        discount_ovr=round((int(disc)*sub_t+sgst_price+cgst_price)/100,3)
        display_text.insert(END,f"Discount  {d.get()}%                                     \t{discount_ovr}\n")
    else:
        discount_ovr=0

    display_text.insert(END,f"============================================================\n")
    display_text.insert(END,f"                                  GRAND TOTAL :-	{round(sub_t+sgst_price+cgst_price-discount_ovr,2)}    \n")
    display_text.insert(END,f"============================================================\n")
    display_text.insert(END,f"Contact us:9785236145\n")
    display_text.insert(END,f"	   abc@gmail.com\n")
    display_text.insert(END,f"\n")
    display_text.insert(END,f"			   THANK YOU\n")
    display_text.insert(END,f"			Visit us Again\n")

#Total bill rupees in black screen
t =Label(button_frame2,text="TOTAL",font="bold")
t.grid(row=0,column=4)
tt=StringVar()
tt.set("0000.00")
tt_1= Entry(button_frame2,textvariable=tt,validate="focusout",bg="black",fg="green",font="20")
tt_1.grid(row=0,column=9)

def grand_total():
    g_total=sub_t+cgst_price+sgst_price-discount_ovr
    tt.set(round(g_total,2))


#Calculate button
cal_but=Button(button_frame2,text="Calculate",height=2,width=20,font="serif 10 bold",bg="yellow",command=lambda:[display_bill(),grand_total()])
cal_but.grid(row=0,column=0)

#Reset button
reset_but=Button(button_frame2,text="RESET",height=2,width=20,font="serif 10 bold",bg="red",command=reset_bill)
reset_but.grid(row=0,column=2)

def upload_to_csv():
    #simply upload some main data in csv file

    with open("cafe_datails.csv","a",newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([n.get(),ph.get(),date_today,time_today,bill_value+1,sub_t,cgst_price,sgst_price,sub_t+cgst_price+sgst_price])


#Print button
print_but=Button(button_frame2,text="Print",height=2,width=20,font="serif 10 bold",bg="darkgreen",command=lambda:[upload_to_csv(),create_save_pdf(),reset_bill()])
print_but.grid(row=0,column=3)

def create_save_pdf():
    name_cust=n.get()
    ph_number=ph.get()
    with open(f"{bill_value+1}.txt","w") as f:
        f.writelines("			CAFE GOOD FIRE\n")
        f.writelines("\n")
        f.writelines("15 Empire building,waghodia road,\n")
        f.writelines("Vadodara - 390013\n")
        f.writelines("\n")
        f.writelines("GST number:12683964839\n")
        f.writelines(f"Customer name:\t{name_cust}\n")
        f.writelines(f"Date and time:\t{date_today}\t{time_today}\n")
        f.writelines(f"Bill number:\t{bill_value+1}\n")
        f.writelines("============================================================\n")
        f.writelines("Dish                        Quantity              Price\n")
        f.writelines("============================================================\n")

        #burger display in bill
        if int(bu1["text"])>0:
            f.writelines(f" Veggie Burger               {a1}                     {a1_price}\n")
        else:
            pass

        if int(bu2["text"]) > 0:
            f.writelines(f" Paneer Burger               {a2}                     {a2_price}\n")
        else:
            pass

        if int(bu3["text"]) > 0:
            f.writelines(f" Grilled Paneer Burger       {a3}                     {a3_price}\n")
        else:
            pass

        if int(bu4["text"]) > 0:
            f.writelines(f" Chicken Burger              {a4}                     {a4_price}\n")
        else:
            pass

        if int(bu5["text"]) > 0:
            f.writelines(f" Grilled Chicken Burger      {a17}                     {a17_price}\n")
        else:
            pass

        #garlic bread display in bill
        if int(gb1["text"]) > 0:
            f.writelines(f" Cheese Garlic Bread         {a5}                     {a5_price}\n")
        else:
            pass

        if int(gb2["text"]) > 0:
            f.writelines(f" Paneer-Cheese Garlic Bread  {a6}                     {a6_price}\n")
        else:
            pass

        #tacos display in bill
        if int(ta1["text"]) > 0:
            f.writelines(f" Veggie Tacos                {a7}                     {a7_price}\n")
        else:
            pass

        if int(ta2["text"]) > 0:
            f.writelines(f" Chicken Tacos               {a8}                     {a8_price}\n")
        else:
            pass

        #Pasta display in bill
        if int(pas1["text"]) > 0:
            f.writelines(f" Peri-Peri Sauce             {a9}                     {a9_price}\n")
        else:
            pass

        if int(pas2["text"]) > 0:
            f.writelines(f" White Sauce                 {a10}                     {a10_price}\n")
        else:
            pass

        #fries display in bill
        if int(fr1["text"]) > 0:
            f.writelines(f" Regular Fries               {a11}                     {a11_price}\n")
        else:
            pass

        if int(fr2["text"]) > 0:
            f.writelines(f" Peri-Peri Fries             {a12}                     {a12_price}\n")
        else:
            pass

        if int(fr3["text"]) > 0:
            f.writelines(f" Veggie Fries                {a18}                     {a18_price}\n")
        else:
            pass

        #Beverages display in bill
        if int(be1["text"]) > 0:
            f.writelines(f" Banana Cracker              {a13}                     {a13_price}\n")
        else:
            pass

        if int(be2["text"]) > 0:
            f.writelines(f" Milk-shake and cookies      {a14}                     {a14_price}\n")
        else:
            pass

        if int(be3["text"]) > 0:
            f.writelines(f" Kit-Kat Choco pie           {a15}                     {a15_price}\n")
        else:
            pass

        if int(be4["text"]) > 0:
            f.writelines(f" Death by Chocolate          {a16}                     {a16_price}\n")
        else:
            pass

        #Cold coffee display in bill
        if int(cc1["text"]) > 0:
            f.writelines(f" Cold Coffee                 {a19}                     {a19_price}\n")
        else:
            pass

        if int(cc2["text"]) > 0:
            f.writelines(f" Frappuccino                 {a20}                     {a20_price}\n")
        else:
            pass

        f.writelines(f"============================================================\n")
        f.writelines(f"                                      Sub total :- {sub_t}\n")
        f.writelines(f"============================================================\n")
        f.writelines(f"SGST  2.5%                                        \t{sgst_price}\n")
        f.writelines(f"CGST  2.5%                                        \t{cgst_price}\n")
        
        if disc=="":
            pass
        
        if int(disc)>0:
            f.writelines(f"Discount  {d.get()}%                                     \t{discount_ovr}\n")
        else:
            pass

        f.writelines(f"============================================================\n")
        f.writelines(f"                                  GRAND TOTAL :-	{round(sub_t+sgst_price+cgst_price-discount_ovr,2)}    \n")
        f.writelines(f"============================================================\n")
        f.writelines(f"Contact us:9785236145\n")
        f.writelines(f"	   abc@gmail.com\n")
        f.writelines(f"\n")
        f.writelines(f"			   THANK YOU\n")
        f.writelines(f"			Visit us Again\n")

root.mainloop()