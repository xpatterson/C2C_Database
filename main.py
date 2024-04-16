import mysql.connector
import unittest

connection = mysql.connector.connect(user = 'root', database = 'sample', password = 'Xp021308!!')
# cursor = connection.cursor()

 

# testQuery = ("SELECT * FROM store")

 

# cursor.execute(testQuery)

 

# for item in cursor:

#     print(item)

 

# cursor.close()
# connection.close()

def access_existing_account():
    username = str(input("What is your username?"))
    password = str(input("What is your password?"))

    connection = mysql.connector.connect(user = 'root', database = 'sample', password = 'Xp021308!!')
    cursor = connection.cursor()

    testQuery = (f"SELECT COUNT(*) FROM `accounts_info` WHERE `username` = '{username}' AND `password` = '{password}';")

    cursor.execute(testQuery)

    data = cursor.fetchone()

    if data == (1,):
        print('Your account has been accessed.')
        #TODO: allow user to do stuff in their account
    else:
        print('No account was found with that username and password.')

   
    # cursor.close()
    #TODO: Make a function to access an account
    pass
def create_new_account():
#function that allows the user to create an account
    cursor = connection.cursor()
    username = input('What would you like your username to be?')
    print('Please retype your username to confirm.')
    proceed = False
    while proceed == False:
        uname_confirm = input()
        if uname_confirm == username:
            proceed = True
        else:
            print('You have not typed the same username. Try again.')

    password = input('What would you like your password to be?')
    print('Please retype your password to confirm.')
    proceed_2 = False
    while proceed_2 == False:
        pword_confirm = input()
        if pword_confirm == password:
            proceed_2 = True
        else:
            print('You have not typed the same password. Try again.')
    #allows user to set username and password
    
    addData = (f'INSERT INTO accounts_info (username, password, balance) VALUES("{username}","{password}", 0.00)')

    cursor.execute(addData)
    print('Your account has been created.')

    connection.commit()
    #adds user's username and password to the table

def access_account():
    #function that starts the program and allows the user to access or create an account
    valid_input_one = False
    while valid_input_one == False:
        welcome_message = print("Welcome!\nWould you like to access an account, create an account, or exit the program?\n(Type 1 for access, 2 for create, and 3 for exit.)")

        account_username = input()
        if account_username == "1":
            # valid_input_one = True
            access_existing_account() #Finish creating function
        elif account_username == "2":
            # valid_input_one = True
            create_new_account()
        elif account_username == "3":
            print(f"Thank you for using our program!")
            valid_input_one = True
        else:
            print("Invalid input. Try again.")

access_account()

connection.close()