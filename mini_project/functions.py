import sys
import os
import csv
import random
import tempfile
import pandas as pd
from csv import DictWriter
def clear():
    	os.system( 'cls' )


mycursor = mydb.cursor()

sql = "INSERT INTO Couriers (courier, courier_phone) VALUES (%s, %s)"
val = ("Sab", "01010101")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")







def finnish():
    finnish = input("Your order has been updated. Press any key to return to the orders edit menu.")
    if finnish == "0":
        clear()
        update_order()
    else:
        clear()
        update_order()

def view_order():
    with open('order.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(" ")
                line_count += 1
            print(f'Order number: {row["Order number"]} \nCustomer name: {row["Customer name"]} \nCustomer address: {row["Customer address"]} \nCustomer phone number: {row["Customer phone number"]}.')
            print(" ")
            line_count += 1
        print(f'Processed {line_count} lines.')

def add_order():
    order_details = ['Order number', 'Customer name', 'Customer address', 'Customer phone number', 'Order date'] 
    order_number = (random.randint(100000,999990))
    customer_name = input("Please enter the customer name: ")
    customer_address = input("Please enter the first line of the addrress and postcode: ")
    customer_phone_number = input("Please enter the customer phone number: ")
    order_date = input("Please enter date of purchase: ")
    order = [{'Order number': order_number, 'Customer name': customer_name, 'Customer address': customer_address, 'Customer phone number': customer_phone_number, 'Order date': order_date}]
    print (f"The order has been placed, \n Please review the order: \n {order}")
    with open('order.csv', 'a+', newline='') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = order_details) 
        writer.writerows(order)

def update_order():
    clear()
    # reading the csv file 
    full_order_list = pd.read_csv("order.csv") 
    print (full_order_list)
    print (" ")
    row_edit = int(input("Please enter the order number. \n The order number is located on the first collumn: "))
    Collumn_edit = 0
    while Collumn_edit not in range(1,6):
        try:
            Collumn_edit = int(input("""What would you like to change: 
Customer name [1]
Customer address [2]
Customer phone number [3]
Order date [4]
Exit back to the Orders menu [5]
"""))
            if Collumn_edit not in range(1,6):
                clear()
                print("Action not recognised")
            
            elif Collumn_edit == 1:
                clear()
                new_edit = input("Please update the name: ")
            # updating the column value/data 
                full_order_list.loc[row_edit, 'Customer name'] = new_edit
            # writing into the file
                full_order_list.to_csv("order.csv", index=False) 
                clear()
                finnish()

            elif Collumn_edit == 2:
                clear()
                new_edit = input("Please update the first line of address followed by the postcode:\n \n ")
                full_order_list.loc[row_edit, 'Customer address'] = new_edit
                full_order_list.to_csv("order.csv", index=False) 
                clear()
                finnish()
                
            elif Collumn_edit == 3:
                clear()
                new_edit = input("Updating phone number: ")
                full_order_list.loc[row_edit, 'Customer phone number'] = new_edit
                full_order_list.to_csv("order.csv", index=False)
                finnish()
                clear()
            elif Collumn_edit == 4:
                clear()
                new_edit = input("Update the date of the order. DD/MM/YYYY \n \n")
                full_order_list.loc[row_edit, 'Customer address'] = new_edit
                full_order_list.to_csv("order.csv", index=False)
                finnish()
                clear()
            elif Collumn_edit == 5:
                clear()
                order_menu()
        except ValueError:
                    clear()
                    print("Please enter an integer.")
                    order_menu()
    return Collumn_edit 


def remove_order():
        # reading the csv file 
    full_order_list = pd.read_csv("order.csv") 
    print (full_order_list)
    print (" ")
    print ("The order number is located on the first collumn: ")
    removal = input("Please enter the order number you would like to remove: ")
    # making data frame from csv file 
    data = pd.read_csv("order.csv", index_col = "Customer name" ) 
# dropping passed values 
    data.drop([removal,"courtney"], inplace = True) 
