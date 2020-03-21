# Program:    Lesson 9 Girl Scout Cookie Program
# Programmer: Jonathan Rux
# Date:       February 10, 2020
# Purpose:    Program for user to order Girl Scout Cookies and calculate totals.

#Imports
import locale
locale.setlocale(locale.LC_ALL, '') #Set Locale

#Declare Variables
order_list = [] #List
cookie_list = ("Savannah", "Thin Mint", "Tag-a-Long", "Peanut Butter", "Sandwich") #Tuple

#******************
#*
#*  Welcome Banner
#*
#******************
print('''\033[33m
========================================================
   Welcome to Girl Scount Cookie Order Program Z1000!
========================================================
\033[0m''')

#Define Functions

#******************
#*
#*  Display Menu
#*
#******************
def disp_menu(): #Ask for the Cookie they want.
    print('''
        Choose an Option:
        ========================
    [\033[33ma\033[0m] Add Cookies
    [\033[33md\033[0m] Delete Cookies
    [\033[33mm\033[0m] Display Current Order
    [\033[33mq\033[0m] Quit
    ''')
    options = ["a", "d", "m", "q"]
    while True:
        choice = input("\033[33m======> \033[0m")
        if choice.lower() in options:
            return choice.lower()
        else:
            print("\033[31m\n\tError: Invalid Option \"{}\"\n\033[0m".format(choice))


#******************
#*
#*  Display Items
#*
#******************
def disp_items():
    print("\n\tChoose a Cookie Flavor:\n\t{}".format('='*24))
    for c in range(len(cookie_list)):
        print("    [\033[33m{}\033[0m]\t{} Cookies".format(c+1, cookie_list[c]))


#******************
#*
#*  Add Process
#*
#******************
def add_process():
    sel = 0
    sel = add_item(sel)
    qty = qty_item(sel)

    item_tot = calc_tot(qty)
    fmt_total = locale.currency(item_tot)
    valid = False
    while not valid:
        try:
            print("\nAdd \033[33m{}\033[0m boxes of {} Cookies with a cost of \033[33m\033[33m{}\033[0m to your order? (\033[32my\033[0m/\033[31mn\033[0m)".format(qty, cookie_list[sel], fmt_total))
            incl = input("\033[33m======> \033[0m")
        except Exception as detail:
            print("\033[31m\n\tError: \"{}\".\033[0m".format(detail))
        else:
            if incl.lower().startswith('y'):
                valid = True
                detail_list = [cookie_list[sel], qty]
                order_list.append(detail_list)
                print("\n\tThe {} Cookies were added to your order.".format(cookie_list[sel]))
            elif incl.lower().startswith('n'):
                # valid = True
                print("\n\tThe {} Cookies were not added to your order.".format(cookie_list[sel]))
                break
            else:
                print("\033[31m\n\tError: Invalid Option \"{}\"\n\033[0m".format(incl))


#******************
#*
#*  Add Item
#*
#******************
def add_item(sel):
    while True: #Ask for Cookie Flavor
        disp_items()
        try:
            sel = int(input("\n\033[33m======> \033[0m"))-1
            if sel in range(0, len(cookie_list)):
                return sel
            else:
                print("\033[31m\n\tError: Invalid Option \"{}\"\n\033[0m".format(sel+1))
        except Exception as detail:
            print("\033[31m\n\tError: \"{}\".\033[0m".format(detail))


#******************
#*
#*  Quantity
#*
#******************
def qty_item(sel):
    while True: #Ask for Quantity
        try:
            print("\nHow many boxes of {} Cookies would you like to order? (\033[33m1-10\033[0m)".format(cookie_list[sel]))
            c = int(input("\033[33m======> \033[0m"))
        except Exception as detail:
            print("\033[31m\n\tError: \"{}\".\033[0m".format(detail))
            pass
        else:
            if c in range(1, 11):
                return c
            else:
                print("\033[31m\n\tError: Invalid Option \"{}\"\n\033[0m".format(c))


#******************
#*
#*  Delete Process
#*
#******************
def del_item():
    if len(order_list) > 0:
        disp_order()
        print("Please choose an item from the list to delete. (1-{})".format(len(order_list)))
        valid = False
        while not valid:
            try:
                sel = int(input("\n\033[33m======> \033[0m"))-1
                if sel in range(0, len(order_list)):
                    print("\nRemoved {} boxes of {} for {} from your order.\n".format(order_list[sel][1], order_list[sel][0], locale.currency(order_list[sel][1] * 3.50)))
                    del order_list[sel]
                    valid = True
                else:
                    print("\033[31m\n\tError: Invalid Option \"{}\"\n\033[0m".format(sel+1))
            except Exception as detail:
                print("\033[31m\n\tError: \"{}\".\033[0m".format(detail))


#******************
#*
#*  Calculate Items
#*
#******************
def calc_tot(qty):
    return qty * 3.50

#******************
#*
#*  Print Order
#*
#******************
def disp_order():
    order_tot = 0
    item_cnt = 0
    if len(order_list) < 1:
        print("\n\tYour order has no items.\n")
    else:
        print("\033[33m\n\t\tName\t\t#\tPrice\n\t{}".format('='*40))
        for o in range(len(order_list)):
            order_tot += order_list[o][1] * 3.50
            item_cnt += order_list[o][1]
            print("\t{}.\t{}\t{}\t{}".format(o+1, order_list[o][0], order_list[o][1], locale.currency(order_list[o][1] * 3.50)))
        print("\033[0m" + "\n\tYour order has \033[33m{}\033[0m boxes for a total of \033[33m{}\033[0m.".format(item_cnt, locale.currency(order_tot)))
        print('\n' + '='*56)


#******************
#*
#*  Main Program
#*
#******************
while True:
    choice = disp_menu()
    if choice == "a":
        add_process()
    elif choice == "d":
        del_item()
    elif choice == "q":
        break
    disp_order()
disp_order()
print("\nThank you for using our Ordering Program!")
