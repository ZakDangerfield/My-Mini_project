# Week 2 finished.
# 26/01 added a corriers sub menu and will implement a view/add/edit and remove (Complete)
# 26/01 add a sub menu for Products
import sys
import os
#Windows

def clear():
	os.system( 'cls' )

#DON'T TOUCH PRODUCT MENU! (WORKING)
def product_menu():
    action = 0
    while action not in range(1,6):
        try:
            action = int(input(("""
Welcome to the Product menu.
Please pick from the following options:

[1]: Shows our Drinks and Snacks menu.   
[2]: Creates a new drinks/snacks entry.
[3]: Edit products. 
[4]: Removes products.
[5]: Exits to the main menu.
Your option: """)))
            if action not in range(1,6):
                clear()
                print("Action not recognised")
            elif action == 1:
                clear()
                d_or_s = input("would you like to see the Drinks menu[1] or our snacks menu[2]? ")
                if d_or_s == "1":
                    print ("Here is the Drinks list: ")
                    with open('drinks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
                elif d_or_s == "2":
                    print ("Here is the snacks list: " "\n")
                    with open('snacks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                print ("\n" "Press any key for main menu")
                result1 = (input())
                if result1 == "0":
                    clear()
                    product_menu()
                else:
                    clear()
                    product_menu()
            elif action == 2:
                clear()
                print("What entry would you like to add to? Drinks[1] or Snacks[2]")
                d_or_s = input()
                if d_or_s == "1":
                    new_drinks_entry = open("drinks.txt", "a")
                    new_drink = input("Please enter the name of a new Drink? ")          
                    new_drinks_entry.write("\n")
                    new_drinks_entry.write(new_drink)
                    new_drinks_entry.close()
                    print (f"Here is the ammended list: \n")
                    with open('drinks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
                elif d_or_s == "2":
                    new_snacks_entry = open("snacks.txt", "a")
                    new_snack = input("Please enter the name of a new snack? ")          
                    new_snacks_entry.write("\n")
                    new_snacks_entry.write(new_snack)
                    new_snacks_entry.close()
                    print (f"Here is the ammended snacks list: \n")
                    with open('snacks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
            elif action == 3:
                clear()
                print ("What directory would you like to edit? drinks[1] or snacks?[2] ")
                d_or_s = input()
                if d_or_s == "1":
                    with open('drinks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    change = int(input("What drink number would you like to edit? "))
                    change_to = input("Please give this number a new name: ")
                    # Edit codes:
                    drinks_edit = open("drinks.txt")
                    edit_drinks_list = drinks_edit.readlines()
                    edit_drinks_list[change] = (f"{change_to} \n") # this replaces the index with the edit 
                    drinks_edit.close()
                    drinks_edit = open("drinks.txt", "w")
                    new_drinkfile_contents = "".join(edit_drinks_list)
                    drinks_edit.write(new_drinkfile_contents)
                    drinks_edit.close()
                    clear()
                    print ("Here is the drinks list: " "\n")
                    with open('drinks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
                #Edit snack entry
                
                elif d_or_s == "2":
                    with open('snacks.txt') as g:
                        for i, line in enumerate(g):
                            print ("{0}: {1}".format(i+0,line))
                    change_s = int(input("What Snack number would you like to edit? "))
                    change_to_s = input("Please give this number a new name: ")
                    # Edit codes:
                    snacks_edit = open("snacks.txt")
                    edit_snacks_list = snacks_edit.readlines()
                    edit_snacks_list[change_s] = (f"{change_to_s} \n") # this replaces the index with the edit 
                    snacks_edit.close()
                    snacks_edit = open("snacks.txt", "w")
                    new_snacksfile_contents = "".join(edit_snacks_list)
                    snacks_edit.write(new_snacksfile_contents)
                    snacks_edit.close()
                    clear()
                    print ("Here is the snacks list: " "\n")
                    with open('snacks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        product_menu()
                    else:
                        clear()
                        product_menu()
            elif action == 4:
                clear()
                print(" What products list do you want to remove from? Drink[1] Snacks[2]")
                remove_item = input()
                if remove_item == "1":
                    print ("Here is the Drinks list: ")
                    with open('drinks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("What drink number would you like to remove? ")
                    removal = int(input())
                    print (f"are you sure you want to remove this product? [y/n]")
                    are_you_sure = input()
                    if are_you_sure == "y":
                        a_file = open("drinks.txt", "r")
                        lines = a_file.readlines()
                        a_file.close()
                        del lines[removal]
                        new_drinks_file = open("drinks.txt", "w+")
                        for line in lines:
                            new_drinks_file.write(line)
                        new_drinks_file.close()
                        print("\n" "press any key for menu")
                        result = input()
                        if result == "0":
                            clear()
                            product_menu()
                        else:
                            clear()
                            product_menu()
                    else:
                        print("Removal was aborted")
                        print("\n" "press any key for menu")
                        resulttt = input()
                        if resulttt == "0":
                            clear()
                            product_menu()
                        else:
                            clear()
                            product_menu()
                elif remove_item == "2":
                    print ("Here is the Snacks list: ")
                    with open('snacks.txt') as f:
                        for i, line in enumerate(f):
                            print ("{0}: {1}".format(i+0,line))
                    print ("What Snack number would you like to remove? ")
                    removal = int(input())
                    print (f"Warning: Are you sure you want to remove this product? [y/n]")
                    are_you_sure = input()
                    if are_you_sure == "y":
                        a_file = open("snacks.txt", "r")
                        lines = a_file.readlines()
                        a_file.close()
                        del lines[removal]
                        new_snacks_file = open("snacks.txt", "w+")
                        for line in lines:
                            new_snacks_file.write(line)
                        new_snacks_file.close()
                        print("\n" "press any key for menu")
                        result = input()
                        if result == "0":
                            clear()
                            product_menu()
                        else:
                            clear()
                            product_menu()
                    else:
                        print("Removal was aborted")
                        print("\n" "press any key for menu")
                        resulttt = input()
                        if resulttt == "0":
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

def couriers_menu():
    action = 0
    while action not in range(1,6):
        try:
            action = int(input("""Welcome to the Couriers menu. Please select from the following options;
s
Option [1] View my couriers.
Option [2] Add a courier.
Option [3] Edit a courier.
Option [4] Remove a courier.
Option [5] Back to Main menu 
Your Option: """))
            
            # View Couriers.
            if action == 1:
                clear()
                print ("Here is the Couriers list: ")
                with open('couriers.txt') as f:
                    for i, line in enumerate(f):
                        print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        couriers_menu()
                    else:
                        clear()
                        couriers_menu()
            # Add Courier
            elif action == 2:
                clear()
                new_couriers_entry = open("couriers.txt", "a")
                new_couriers = input("Please enter the name of the new couriers? ")          
                new_couriers_entry.write("\n")
                new_couriers_entry.write(new_couriers)
                new_couriers_entry.close()
                print (f"Here is the ammended list: \n")
                with open('couriers.txt') as f:
                    for i, line in enumerate(f):
                        print ("{0}: {1}".format(i+0,line))
                print ("\n" "Press any key for main menu")
                result1 = (input())
                if result1 == "0":
                    clear()
                    couriers_menu()
                else:
                    clear()
                    couriers_menu()           
            elif action == 3:
                clear()
                with open('couriers.txt') as f:
                    for i, line in enumerate(f):
                        print ("{0}: {1}".format(i+0,line))
                    change = int(input("What Courier number would you like to edit? "))
                    change_to = input("Please Enter a new name to this number: ")
                    # Edit codes:
                    couriers_edit = open("couriers.txt")
                    edit_couriers_list = couriers_edit.readlines()
                    edit_couriers_list[change] = (f"{change_to} \n") # this replaces the index with the edit 
                    couriers_edit.close()
                    couriers_edit = open("couriers.txt", "w")
                    new_couriersfile_contents = "".join(edit_couriers_list)
                    couriers_edit.write(new_couriersfile_contents)
                    couriers_edit.close()
                    #readable file code
                    print ("Here is the couriers list: " "\n")
                with open('couriers.txt') as f:
                    for i, line in enumerate(f):
                        print ("{0}: {1}".format(i+0,line))
                    print ("\n" "Press any key for main menu")
                    result1 = (input())
                    if result1 == "0":
                        clear()
                        couriers_menu()
                    else:
                        clear()
                        couriers_menu()            
            elif action == 4:
                clear()
                print ("Here is the couriers list: ")
                with open('couriers.txt') as f:
                    for i, line in enumerate(f):
                        print ("{0}: {1}".format(i+0,line))
                print ("What courier number would you like to remove? ")
                removal = int(input())
                print (f"are you sure you want to remove this courier? [y/n]")
                are_you_sure = input()
                if are_you_sure == "y":
                    couriers_file = open("couriers.txt", "r")
                    lines = couriers_file.readlines()
                    couriers_file.close()
                    del lines[removal]
                    new_couriers_file = open("couriers.txt", "w+")
                    for line in lines:
                        new_couriers_file.write(line)
                    new_couriers_file.close()
                    print("\n" "press any key for menu")
                    result = input()
                    if result == "0":
                        clear()
                        menu()
                    else:
                        clear()
                        menu()            
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

def menu():
    action = 0
    while action not in range(1,4):
        try:
            action = int(input("""Welcome to the main menu please select from the following options;

Option [1] Exits the app
Option [2] Enter the products menu.
Option [3] Enter the couriers menu.
"""))
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
                
            elif action not in range(1,4):
                clear()
                print ("Action not recognised.")
        except ValueError:
            clear()
            print("Please enter an integer.")
            menu()
    return action




clear()
menu()
