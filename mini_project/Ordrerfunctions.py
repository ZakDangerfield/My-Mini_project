import sys
import os
import csv
import pandas as pd 
from csv import DictWriter
from week5functions import *


def clear():
	os.system( 'cls' )

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="password",
database="Zaks_mini_project"
)




def make_order():
    mycursor = mydb.cursor()
    customer_name = input("Please enter the name of the customer: ")
    clear()
    customer_address = input("Please enter a customer address:\n")
    clear()
    customer_phone = input("Please enter the customer contact number: ")
    clear()
    view_couriers()
    courier_ID = int(input("Please select a courier: "))
    clear()
    Status = "preparing"

    Items_list = []
    item = 1
    while item != 0:
        clear()
        view_products()
        print("Please select the products you wish to order, when finished pleas enter 0.\n ")
        item = int(input("Selection: "))
        Items_list.append(item)
    Items_list.remove(0)

    sql = "INSERT INTO Orders (Customer_name, Customer_address, Customer_phone, Courier_ID, Status_of, Products) VALUES (%s, %s, %s, %s, %s, %s) "
    mycursor.execute(sql, (customer_name, customer_address, customer_phone, courier_ID, Status, str(Items_list)))
    mydb.commit()

def update_order_name():
    mycursor = mydb.cursor()
    print("\n***Customer name Update***\n")
    replace_customer_name = int(input("Please provide the Order ID of the order you wish to update:  "))
    replace_customer_name_to = input("Please Update this entry with a new name:  ")
    sql = "UPDATE Orders SET Customer_name = %s WHERE order_id = %s"
    val = (replace_customer_name_to, replace_customer_name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def update_order_address():
    print("***Customer address Update***")
    mycursor = mydb.cursor()
    sql = "UPDATE Orders SET Customer_address = %s WHERE order_id = %s"
    replace_customer_address = int(input("Please provide the Order ID of the order you wish to update:  "))
    replace_customer_address_to = input("Please Update this entry with a new address:  ")
    val = (replace_customer_address_to, replace_customer_address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def update_order_phone():
    mycursor = mydb.cursor()
    print("***Phone number Update***")
    sql = "UPDATE Orders SET Customer_phone = %s WHERE order_id = %s"
    replace_customer_phone = int(input("Please provide the Order ID of the customers phone number you wish to update:  "))
    replace_customer_phone_to = input("Please Update this entry with a new phone number:  ")
    val = (replace_customer_phone_to, replace_customer_phone)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def update_order_courier():
    print("***Courier Update***")
    mycursor = mydb.cursor()
    sql = "UPDATE Orders SET Courier_ID = %s WHERE order_id = %s"
    replace_customer_courier = int(input("Please provide the Order ID you wish to update:  "))
    replace_customer_courier_to = int(input("Please Update this entry with a Courier ID number:  "))
    val = (replace_customer_courier_to, replace_customer_courier)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def view_orders():
    mycursor = mydb.cursor()
    
    sql = "SELECT \
    Orders.order_id, \
    Orders.Customer_name, \
    Orders.Customer_address, \
    Orders.Customer_phone, \
    Orders.Status_of, \
    Orders.products, \
    Couriers.Courier_name AS Courier_id \
    FROM Orders \
    INNER JOIN Couriers ON Orders.Courier_id = Couriers.Courier_id "

    mycursor.execute(sql)
    
    myresult = mycursor.fetchall()
    
    for row in myresult:
            print(f"Order ID: {row[0]}")
            print(f"Customer name: {row[1]}")
            print(f"Customer address: {row[2]}")
            print(f"Customer phone: {row[3]}")
            print(f"Order status: {row[4]}")
            print(f"Purchased product ID's: {row[5]}")
            print(f"Courier name: {row[6]}")
            print (" \n ")

def remove_order():
    mycursor = mydb.cursor()
    sql = "DELETE FROM Orders WHERE order_id = %s"
    val = int(input("Please enter the Order ID of the Order you wish to remove: \nOrder ID:  "))
    mycursor.execute(sql, (val,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
        

def update_order_status():
    mycursor = mydb.cursor()
    print("***Status Update***\n")
    sql = "UPDATE Orders SET Status_of = %s WHERE order_id = %s"
    replace_customer_status = int(input("Please select the order id you wish to update: "))
    replace_customer_status_to = input("Please Update the status of this order:  ")
    val = (replace_customer_status_to, replace_customer_status)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

