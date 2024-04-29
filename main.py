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

def mod_account_info():
    current_uname = input(f'Please type in current username.')
    current_pword = input(f'Please type in current password.')
    mod_username = input('What would you like your new username to be?')
    print('Please retype your username to confirm.')
    proceed = False
    while proceed == False:
        uname_confirm = input()
        if uname_confirm == mod_username:
            proceed = True
        else:
            print('You have not typed the same username. Try again.')

    mod_password = input('What would you like your new password to be?')
    print('Please retype your password to confirm.')
    proceed_2 = False
    while proceed_2 == False:
        pword_confirm = input()
        if pword_confirm == mod_password:
            proceed_2 = True
        else:
            print('You have not typed the same password. Try again.')


    import mysql.connector

    connection = mysql.connector.connect(user = 'root', database = 'sample', password = 'Xp021308!!')

    cursor = connection.cursor()
    mod_data = (f'UPDATE accounts_info SET username = "{mod_username}", password = "{mod_password}" WHERE username = "{current_uname}" AND password = "{current_pword}";')

    cursor.execute(mod_data)


# def deposit_money():
    

          
    correct_input = False
    while correct_input == False:
        user_confirmation = input("Are you sure you would like to exit your account?(y/n)")
        if user_confirmation == "y":
            correct_input = True
        elif user_confirmation == "n":
            correct_input = True
        else:
            print('That is not a valid answer. Please type "y" or "n".')


def check_balance():
    username = input(f'You will have to retype your username to check balance.')

    import mysql.connector

    connection = mysql.connector.connect(user = 'root', database = 'sample', password = 'Xp021308!!')

    cursor = connection.cursor()
    testQuery = (f"SELECT balance FROM accounts_info WHERE username = '{username}'")

    cursor.execute(testQuery)

    print("\nYour account balance is the number inside the parenthesis and if nothing shows up, then no account was found with the usernamer you typed.\n")
    for item in cursor:
        print(f"\nYou account balance is {item}.\n")
        

def user_account_actions():
    #function for user to do certain actions once they have accessed their account
    
    user_correct_input = False
    while user_correct_input == False:
        user_in_account = True
        while user_in_account == True:
            user_action = input('What would you like to do?\n(Check balance = "1", Modify account information = "5", Exit account = "6")')
                
            if user_action == "1":
                #choice to check user balance
                user_correct_input = True
                check_balance()

            # Deposit money = "2", Withdraw money = "3", Delete account = "4"

            # elif user_action == "2":
            #     user_correct_input = True
            #     # deposit_money()

                
            #     pass

            # elif user_action == "3":
            #     user_correct_input = True
                
            #     pass

            # elif user_action == "4":
            #     user_correct_input = True
            #     mod_account_info()
                
            #     pass

            elif user_action == "5":
                user_correct_input = True
                mod_account_info()
                

            elif user_action == "6":
                #choice to exit account
                correct_input = False
                while correct_input == False:
                    user_confirmation = input("Are you sure you would like to exit your account?(y/n)")
                    if user_confirmation == "y":
                        correct_input = True
                        user_in_account = False
                    elif user_confirmation == "n":
                        correct_input = True
                    else:
                        print('That is not a valid answer. Please type "y" or "n".')
                user_correct_input = True
                

            else:
                print("What you typed was not an available choice. Please type one of the number choices given.")


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
        user_account_actions()
 
        
        #TODO: allow user to do stuff in their account
    else:
        print('No account was found with that username and password.')

   
    # cursor.close()
    
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
            access_existing_account()

            class TestAccessExistAccount():
                def test_account_uname(self):
                    self.assertTrue(account_uname = 1)
            if __name__ == '__main__':
                unittest.main()
            #unit test #1

        elif account_username == "2":
            # valid_input_one = True
            create_new_account()

            class TestCreateNewAccount():
                def test_new_account(self):
                    self.assertTrue(account_uname = 2)
            if __name__ == '__main__':
                unittest.main()
            #unit test #2

        elif account_username == "3":
            print(f"Thank you for using our program!")
            valid_input_one = True
        else:
            print("Invalid input. Try again.")

access_account()

connection.close()