import csv 
from datetime import datetime

list_data=[]
def addtocsv(data):
    with open("Bills.csv", 'a',newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def readfromcsv():
    with open('Bills.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row:
                list_data.append(row)

def addItem():
   item=input("Enter Item Name")
   quantity=eval(input("Enter Quantity of Item"))
   price=eval(input("Enter Price of Item"))
   data=list()
   data.append(item)
   data.append(quantity)
   data.append(price)
   today=datetime.today().strftime('%Y-%m-%d')
   data.append(today)
   list_data.append(data)
   print(list_data)
   addtocsv(data)



def printitems():
    print("Item\t","Quantity\t","Price\t","Date\t","Total\n")
    for item in list_data:
        t=int(item[1])*int(item[2])
        print(item[0],"\t",item[1],"\t",item[2],"\t",item[3],"\t",t)
 
def reset():
      list_data.clear()
      filename = "Bills.csv"
      f = open(filename, "w+")
      f.close()