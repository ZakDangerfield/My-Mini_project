import sys
import os
# import csv
# import pandas as pd 
# from csv import DictWriter

def clear():
	os.system( 'cls' )

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="password",
database="Zaks_mini_project"
)
# COURIER FUNCS
def couriers_menu_finnish():
    finnish = input("\nPress any key to return to the orders edit menu.")
    if finnish == "0":
        clear()
        couriers_menu()
    else:
        clear()
        couriers_menu()

# COURIER FUNCTIONS
def add_courier():
	mycursor = mydb.cursor()
	new_courier = input("Please enter the full name of a new courier:   ")
	new_courier_phone = input("Please enter the couriers phone number:   ")
	courier_sql = "INSERT INTO Couriers (Courier_name, Courier_phone_number) VALUES (%s, %s)"
	courier_val = (new_courier, new_courier_phone)
	mycursor.execute(courier_sql, courier_val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

def view_couriers():
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM Couriers")
	myresult = mycursor.fetchall()
	for row in myresult:
		print(f"Courier ID: {row[0]}")
		print(f"Courier Name: {row[1]}")
		print(f"Courier Phone number: {row[2]}")
		print (" ")
# UPDATING COURIER FUNCTIONS
def update_courier_name():
	mycursor = mydb.cursor()
	sql = "UPDATE Couriers SET Courier_name = %s WHERE Courier_ID = %s"
	replace_courier_name = int(input("Please enter the Courier ID of the courier you wish to update:  "))
	replace_courier_name_to = input("Please Update this entry with the Full name of a new courier:  ")
	val = (replace_courier_name_to, replace_courier_name)
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record(s) affected")

def update_courier_phone():
	mycursor = mydb.cursor()
	sql_phone = "UPDATE Couriers SET Courier_phone_number = %s WHERE Courier_ID = %s"
	replace_courier_phone = int(input("Please enter the Courier ID of the courier you wish to update: \n \n"))
	replace_courier_phone_to = input("Please enter the new phone number: ")
	val_phone = (replace_courier_phone_to, replace_courier_phone)
	mycursor.execute(sql_phone, val_phone)
	mydb.commit()
	print(mycursor.rowcount, "record(s) affected")

def remove_courier():
    mycursor = mydb.cursor()
    sql = "DELETE FROM Couriers WHERE Courier_ID = %s"
    val = int(input("Please enter the Courier ID of the Courier you wish to remove: \nCourier ID:  "))
    mycursor.execute(sql, (val,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
#______________________________
# PRODUCTS FUNCS
def view_products():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Products")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(f"Product ID: {row[0]}")
        print(f"Product Name: {row[1]}")
        print(f"Product Price: £{row[2]}")
        print (" ")

def add_product():
	mycursor = mydb.cursor()
	new_product = input("Please enter the name of your new product:   ")
	new_product_price = input("Please enter price of your new product:   ")
	x = float(new_product_price)
	products_sql = "INSERT INTO Products (Product_name, Price) VALUES (%s, %s)"
	products_val = (new_product, x)
	mycursor.execute(products_sql, products_val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

def update_product_name():
    mycursor = mydb.cursor()
    sql = "UPDATE Products SET Product_name = %s WHERE Product_ID = %s"
    replace_product_name = int(input("Please enter the Product ID of the Product you wish to update:  "))
    replace_product_name_to = input("Please Update this entry with a new product name:  ")
    val = (replace_product_name_to, replace_product_name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def update_product_price():
    mycursor = mydb.cursor()
    sql = "UPDATE Products SET Price = %s WHERE Product_ID = %s"
    replace_product_name = int(input("Please enter the Product ID of the Product you wish to update: "))
    replace_product_name_to = input("Please Update this entry with a new product price: ")
    val = (replace_product_name_to, replace_product_name)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def remove_product():
    mycursor = mydb.cursor()
    sql = "DELETE FROM Products WHERE Product_ID = %s"
    val = int(input("Please enter the Product ID of the product you wish to remove: \nProduct ID:  "))
    mycursor.execute(sql, (val,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
