#import Section Begins
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from bills import *
#Import Section Ends
readfromcsv()

#Window Section Starts
window = Tk()
window.title("Billing App by Abhay")
window.geometry('900x200')
#Window Section Ends


#Entry Section Starts
#1
lbl1 = Label(window, text="Item Name")
lbl1.grid(column=1, row=0)
name = Entry(window,width=10)
name.grid(column=2, row=0)

#2
lbl2 = Label(window, text="Quantity")
lbl2.grid(column=3, row=0)
var =IntVar()
var.set(1)
quantity = Spinbox(window, from_=1, to=10, width=5,textvariable=var) #Entry(window,width=10)
quantity.grid(column=4, row=0)

#3
lbl3 = Label(window, text=" Price")
lbl3.grid(column=5, row=0)
price = Entry(window,width=10)
price.grid(column=6, row=0)
#Entry Section Ends



#Function Sections Starts
def clicked():
    item=name.get()
    q=quantity.get()
    p=price.get()
    if (not p.isdigit() or not q.isdigit()):
        messagebox.showinfo('Entry Details','Enter Valid Data')
        return 0
    data=list()
    data.append(item)
    data.append(q)
    data.append(p)
    today=datetime.today().strftime('%Y-%m-%d')
    data.append(today)
    list_data.append(data)
    #print(list_data)
    addtocsv(data)
    click()
    #messagebox.showinfo('Entry Details',type(n))

#Items
items = scrolledtext.ScrolledText(window,width=55,height=10)
items.grid(column=0,row=0)

def click():
    total=0
    items.delete(1.0,END)
    items.insert(INSERT,'Item Name   Quantity   Price      Date     Total\n')
    items.insert(INSERT,'-------------------------------------------------\n')
    for data in list_data:
        t=int(data[1])*int(data[2])
        items.insert(INSERT,data[0]+"\t\t"+data[1]+"\t"+data[2]+"\t"+data[3]+"\t"+str(t)+"\n")
        total=total+t
    items.insert(INSERT,'-------------------------------------------------')
    items.insert(INSERT,'\n\nSum Total= '+str(total))    

def clear():
    reset()
    click()
#Function Section Ends


#Button Section Starts
but = Button(window, text="View", command=click)
but.grid(column=0, row=1)
btn = Button(window, text="Add", command=clicked)
btn.grid(column=3, row=1)
but = Button(window, text="Reset Memory", command=clear)
but.grid(column=6, row=1)
#Button Section Ends
click()

window.mainloop()