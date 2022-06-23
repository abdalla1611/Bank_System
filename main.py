from BankSystem import *

System = BankSystem()

menu_options = {
    1: 'Sign Up',
    2: 'Create Account',
    3: 'Delete Account',
    4: 'Create Savings Account',
    5: 'Deposit',
    6: 'Withdraw',
    7: 'Show Account',
    8: 'Exit',
}


def get_values():
    """
    asking for the username and the password then check if it in the system and if he has already an account or not
    :return:
        the account if the user already has one
        else return None
    """
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    acc = System.validate_details(username, password)
    if not acc:
        print("Please create an account first.")
        return None
    elif acc == -1:
        print("There is no such username or password in the database, PLease sign up first.")
        return None
    else:
        return acc


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


def sign_up():
    System.signUp()


def create_acc():
    System.createAccount()


def delete_acc():
    System.deleteAccount(get_values())


def create_saving_acc():
    System.createSavingsAccount(get_values())


def deposit():
    System.deposit(get_values())


def withdraw():
     System.withdraw(get_values())


def show_acc():
    System.show_account(get_values())


if __name__=='__main__':
    """
    implementing the CLI by asking the user what action he want by entering a number between 1-8 .
    then calling for the corresponding method that take care of what the user ask if the user enters an invalid input 
    then the system will print a message and let him try again with a valid input .  
    """
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
            continue
        if option == 1:
            sign_up()
        elif option == 2:
            create_acc()
        elif option == 3:
            delete_acc()
        elif option == 4:
            create_saving_acc()
        elif option == 5:
            deposit()
        elif option == 6:
            withdraw()
        elif option == 7:
            show_acc()
        elif option == 8:
            print("Bye Bye!")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 8.')
