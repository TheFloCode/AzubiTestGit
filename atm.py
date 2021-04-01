#!/usr/bin/python3.6
import getpass
import string
import os


users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0

while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:

        print('INVALID USERNAME')

        # comparing pin

        pin = str(getpass.getpass(input('\nPLEASE ENTER PIN: ')))

    if pin.isdigit():
        if user == 'user':
            if pin == pins[0]:

                break
            elif pin != pins[0]:
                str(getpass.getpass(input('\nINVALID PIN. TRY AGAIN: ')))

    if user == 'user2':
        if pin == pins[1]:
            break
        else:

            print('INVALID PIN')

    if user == 'user3':
        if pin == pins[2]:
            break
        else:

            print('INVALID PIN')

    else:
        print('------------------------')
        print('************************')
        print('INVALID PIN FORMAT')
        print('************************')
        print('------------------------')
        exit()

        print('LOGIN SUCCESSFUL, CONTINUE')
        print('----------ATM SYSTEM-----------')

        # Main menu
while True:
    # os.system('clear')
    print('-------------------------------')
    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) '
                     '\nDeposit__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('*******************************')
    print('-------------------------------')
    valid_responses = ['s', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 's':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(user[n]), 'YOU HAVE ', amounts[n], 'DOLLARS ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')

    elif response == 'w':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 DOLLARS NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'DOLLARS')
            print('***********************************')
            print('-----------------------------------')

    elif response == 'd':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 DOLLAR NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'DOLLARS')
            print('****************************************')
            print('----------------------------------------')
    elif response == 'p':
        print('-----------------------------')
        print('*****************************')
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        print('*****************************')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_pin = str(getpass.getpass('CONFIRM NEW PIN: '))
            print('*******************')
            print('-------------------')
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
