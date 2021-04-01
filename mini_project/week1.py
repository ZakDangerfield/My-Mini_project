#week 1 complete 
import sys
import os
#Windows
def clear():
	os.system( 'cls' )

def myfunc():
    global drinks
    drinks = ['Coke', 'Pepsi', 'Coca-Cola','Sprite','Fanta','Schweppes','Appletiser','Fresca','Barqs']
myfunc()
def myfunc_2():
    global snacks
    snacks = [ "Nachos", "Popcorn", "Crackers", "Pretzels", "Granola Bars", "Peanuts", "Dried Fruit"]
myfunc_2()
def myfunc_3():
	global couriers
	couriers = []
myfunc_3()

def menu():
    print ("""Welcome to the main menu.
Please pick from the following options.

Option 1: Shows our drinks and snacks.

Option 2: Creates a new product entry.

Option 3: Edit products.

option 4: Removes products
Option 20: exits the app. 
Your option: """)

    choice = int(input())
    
    # Drinks
    if choice == 1:
        clear()
        print (f"Here is the drinks list {drinks}")
        print (f"Here is the snacks list {snacks}")
        print ("Press any key for main menu")
        result1 = (input())
        if result1 == "0":
            clear()
            menu()
        else:
            clear()
            menu()
            
    #add a drink or snack to their respective library
    elif choice == 2:
        clear()
        print("What entry would you like to add to? Drinks[1] or Snacks[2]")
        d_or_s = input()
        if d_or_s == "1":
            print (drinks)
            add = input("what would you like to add to our drinks menu?\n ")
            drinks.append(add)
            print (f'The updated drinks list: {drinks}')
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()
        elif d_or_s == "2":
            print (snacks)
            add = input("what would you like to add to our snacks menu?\n ")
            snacks.append(add)
            print (f'The updated drinks list: {snacks}')
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()
        else:
            print("Incorrect command, Please press any key to return to the main menu")
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()

    # edit a drink or snack index
    elif choice == 3:
        clear()
        print ("What directory would you like to edit? drinks[1] or snacks?[2] ")
        dri_or_sna = input()
        if dri_or_sna == "1":
            print (drinks)
            print ("What drink number starting from 0 would you like to edit? ")
            change = int(input())
            print ("Please enter a new name for this product: ")
            changeto = input()
            drinks[change] = changeto
            print (f"here is the new improved drinks list {drinks}")
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()
            
        elif dri_or_sna == "2":
            print (snacks)
            print ("What snack number starting from 0, would you like to edit? ")
            change = int(input())
            print ("Please enter a new name for this product: ")
            changeto = input()
            snacks[change] = changeto
            print (f"here is the new improved snacks list {snacks}")
            print("press any key for menu")
            result = input()
            if result == "0":
                clear()
                menu()
            else:
                clear()
                menu()
        
    # Remove a drinks option
    elif choice == 4:
        clear()
        print (drinks)
        print ("What drink number would you like to remove? (first_entry[0])")
        removal = int(input())
        print (f"are you sure you want to remove this product? [Y/N]")
        are_you_sure = input()
        if are_you_sure == "Y" or "y":
            drinks.pop(removal)
        print (f"Selected object has been removed: {drinks}")
        print("press any keyfor menu")
        result = input()
        if result == "0":
            clear()
            menu()
        else:
            clear()
            menu()
        print("Returned to menu")
    #Leave app
    elif choice == 20:
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
    

menu()
