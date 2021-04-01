import os
import csv
from csv import DictWriter
from week5functions import *
from Ordrerfunctions import *

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="password",
database="Zaks_mini_project"
)


def clear():
	os.system( 'cls' )

def order_menu():
    action = 0
    while action not in range(1,6):
        try:
            action = int(input("""    
.-=~=-.                                                                 .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
(__  _)                                                                 (__  _)
( _ __)                  Welcome to the Orders menu!                    ( _ __)
(__  _)              -----------------------------------                (__  _)
( _ __)                                                                 ( _ __)
(_ ___)                     [1] View all orders.                        (_ ___)
(__  _)                   -------------------------                     (__  _)
( _ __)                [2] Add an order to the system.                  ( _ __)
(__  _)              -----------------------------------                (__  _)
(_ ___)                 [3] Update an existing order.                   (_ ___)
(__  _)               ---------------------------------                 (__  _)
(_ ___)               [4] Remove an order from Database.                (_ ___)
(__  _)              ------------------------------------               (__  _)
( _ __)                    [5] Return to Main menu.                     ( _ __)
(__  _)                   --------------------------                    (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
(__  _)                                                                 (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                                                                 `-._.-'
"""))
            if action not in range(1,6):
                clear()
                print("Action not recognised")
            elif action == 1:
                clear()
                view_orders()
                print ("\n" "Press any key for main menu")
                result1 = (input())
                if result1 == "0":
                    clear()
                    order_menu()
                else:
                    clear()
                    order_menu()
            elif action == 2:
                clear()
                make_order()
                print ("\n" "Press any key for main menu")
                result1 = (input())
                if result1 == "0":
                    clear()
                    order_menu()
                else:
                    clear()
                    order_menu()
            elif action == 3:
                clear()
                choice = input("""Please choose from the following options: \n
[1] Update the name of an order. \n
[2] Update the address of an order. \n
[3] Update the Contact number of an order. \n
[4] Update the Courier allocated to an order. \n
[5] Update the Status of an order. \n
[6] Return back to the Orders menu. \n
""")
                if choice == "1":
                    clear()
                    clear()
                    update_order_name()
                    view_orders()
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        order_menu()
                    else:
                        clear()
                        order_menu()
                elif choice == "2":
                    clear()
                    view_orders()
                    update_order_address()
                    view_orders()
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        order_menu()
                    else:
                        clear()
                        order_menu()
                elif choice == "3":
                    clear()
                    view_orders()
                    update_order_phone()
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        order_menu()
                    else:
                        clear()
                        order_menu()
                elif choice == "4":
                    clear()
                    update_order_courier()
                    view_orders()
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        order_menu()
                    else:
                        clear()
                        order_menu()
                elif choice == "5":
                    clear()
                    view_orders()
                    update_order_status()
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        order_menu()
                    else:
                        clear()
                        order_menu()
                elif choice == "6":
                    clear()    
                    order_menu()  
            elif action == 4:
                clear()
                view_orders()
                remove_order()
                print ("\n" "Press any key for main menu")
                result1 = (input())
                if result1 == "0":
                    clear()
                    order_menu()
                else:
                    clear()
                    order_menu()
            elif action == 5:
                clear()
                menu()
        except ValueError:
            clear()
            print("Please Choose a valid option.")
            order_menu()
    return action


#Product menu --------------------------------------------------------------
def product_menu():
    action = 0
    while action not in range(1,6):
        try:
            action = int(input("""
 ........................................................
 :   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
 : _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
 :(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
 :  / o \    / o \    / o \    / o \    / o \    / o \  :
 : (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
 :   ,-.   ....................................   ,-.   :
 : _(*_*)_ :                                  : _(*_*)_ :
 :(_  o  _):   Welcome to the Product menu.   :(_  o  _):
 :  / o \  :     Please select an option:     :  / o \  :
 : (_/ \_) :                                  : (_/ \_) :
 :   ,-.   :      View all products: [1]      :   ,-.   :
 : _(*_*)_ :  Create a new product entry: [2] : _(*_*)_ :
 :(_  o  _):   Edit a selected product: [3]   :(_  o  _):
 :  / o \  :   Remove a selected product [4]  :  / o \  :
 : (_/ \_) :                                  : (_/ \_) :
 :   ,-.   :    Exit back to main menu [5]    :   ,-.   :
 : _(*_*)_ :                                  : _(*_*)_ :
 :(_  o  _):  _______________________________ :(_  o  _):
 :  / o \  :                                  :  / o \  :
 : (_/ \_) :..................................: (_/ \_) :
 :   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
 : _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
 :(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
 :  / o \    / o \    / o \    / o \    / o \    / o \  :
 : (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
 :......................................................:
"""))
            if action not in range(1,6):
                clear()
                print("Action not recognised")
            elif action == 1:
                clear()
                view_products()
                finnish = input("\nPress any key to return to the orders edit menu.")
                if finnish == "0":
                    clear()
                    product_menu()
                else:
                    clear()
                    product_menu()
                
            elif action == 2:
                clear()
                view_products()
                add_product()
                view_products()
                finnish = input("\nPress any key to return to the orders edit menu.")
                if finnish == "0":
                    clear()
                    product_menu()
                else:
                    clear()
                    product_menu()

            elif action == 3:
                clear()
                name_or_price = input("""
                                           .---.
                                          /  .  \
                                         
                                         |   |  /|
  .--------------------------------------------' |
 /  .-.                                          |
|  /   \    What would you like to edit?         |
| |\_.  |                                        |
|\|  | /|       Product name  [1]                |
| `---' |       Product price [2]                |
|       |                                       /
|       |     Return to main menu [3]           |
|       |--------------------------------------'
\       |
 \     /
  `---'
""")
                if name_or_price == "1":
                    clear()
                    view_products()
                    update_product_name()
                    finnish = input("\nPress any key to return to the orders edit menu.")
                    if finnish == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
                elif name_or_price == "2":
                    clear()
                    view_products()
                    update_product_price()
                    finnish = input("\nPress any key to return to the orders edit menu.")
                    if finnish == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
                else:
                    clear()
                    product_menu()
            elif action == 4:
                clear()
                view_products()
                remove_product()
                finnish = input("\nPress any key to return to the orders edit menu.")
                if finnish == "0":
                    clear()
                    product_menu()
                else:
                    clear()
                    product_menu()
            elif action == 5:
                clear()
                menu()
        except ValueError:
            clear()
            print("Please enter an integer.")
            product_menu()
    return action

#Courier Menu ------------------------------------------------------
def couriers_menu():
    action = 0
    while action not in range(1,6):
        try:
            action = int(input("""Welcome to the Couriers menu. 
Please select from the following options;

Option [1] View my couriers.
Option [2] Add a courier.
Option [3] Edit a courier.
Option [4] Remove a courier.
Option [5] Back to Main menu 
Your Option: """))
            
            # View Couriers.
            if action == 1:
                clear()
                print ("\nHere is the Couriers list: \n")
                view_couriers()
                finnish = input("\nPress any key to return to the orders edit menu.")
                if finnish == "0":
                    clear()
                    couriers_menu()
                else:
                    clear()
                    couriers_menu()
            # Add Courier
            elif action == 2:
                clear()
                add_courier()
                print ("\nPress any key for main menu")
                result1 = (input())
                if result1 == "0":
                    clear()
                    couriers_menu()
                else:
                    clear()
                    couriers_menu()   
                    
            # Update existing couriers
            elif action == 3:
                clear()
                what_to_edit = input("""What item would you like to edit?
Courier name [1]
Courier Phone number [2] 
Press any other key to return back to couriers menu.   """)
                if what_to_edit == "1":
                    clear()
                    view_couriers()
                    update_courier_name()
                    result1 = input("\n Press any key to return to the couriers menu ")
                    if result1 == "0":
                        clear()
                        couriers_menu()
                    else:
                        clear()
                        couriers_menu() 
                elif what_to_edit == "2":
                    clear()
                    view_couriers()
                    update_courier_phone()
                    result1 = input("\n Press any key to return to the couriers menu ")
                    if result1 == "0":
                        clear()
                        couriers_menu()
                    else:
                        clear()
                        couriers_menu()
                else:
                    clear()
                    couriers_menu()
            elif action == 4:
                clear()
                view_couriers()
                remove_courier()
                print("\n" "press any key for menu")
                result = input()
                if result == "0":
                    clear()
                    couriers_menu()
                else:
                    clear()
                    couriers_menu()            
            elif action == 5:
                clear()
                menu()
            elif action not in range(1,6):
                clear()
                print ("Action not recognised.")
        except ValueError:
            clear()
            print("Please enter an integer.")
            couriers_menu()
    return action

#Main Menu ----------------------------------------------------------
def menu():
    action = 0
    while action not in range(1,4):
        try:
            action = int(input('''
                     ,---.           ,---.
                    / /"`.\.--"""--./,'"\ \

                     `./  / __   __ \  \,'
                      /    /_O)_(_O\    \

                   .--|       \_/       |--.
                 ,'    \   \   |   /   /    `.
                /       `.  `--^--'  ,'       \

.-----------/         \------------------/         \--------------.
| .---------\         /----------------- \         /------------. |
| |          `-`--`--'                    `--'--'-'             | |
| |Welcome to the main menu.                                    | |
| |Please select from the following options:                    | |
| |                                                             | |
| |Option [1] Exits the app.                                    | |
| |Option [2] Enter the products menu.                          | |
| |Option [3] Enter the couriers menu.                          | |
| |option [4] Enter the orders menu.                            | |
| |                                                             | |
| |_____________________________________________________________| |
|_________________________________________________________________|
                   )__________|__|__________(
                  |            ||            |
                  |____________||____________|
                    ),-----.(      ),-----.(
                  ,'   ==.   \    /  .==    `.
                 /            )  (            \
'''))
# exit app
            if action == 1:
                clear()
                print ("are you sure you want to leave? press 3 for yes or 0 no")
                result3 = int(input())
                if result3 == 3:
                    sys.exit(3)
                elif result3 == 0:
                    clear()
                    menu()
                else:
                    print ("incorrect command returned to menu")
                    clear()
                    menu()
            
            elif action == 2:
                clear()
                product_menu()
            
            elif action == 3:
                clear()
                couriers_menu()
                
            elif action == 4:
                clear()
                order_menu()
            
            elif action not in range(1,4):
                clear()
                print ("Please enter an option.")
        except ValueError:
            clear()
            print("Please enter an option.")
            menu()
    return action




clear()
menu()
