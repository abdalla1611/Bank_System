from Account import *


class SingletonMeta(type):

    """
    The Singleton class can be implemented in different ways in Python. We will use the
    metaclass .
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BankSystem(metaclass=SingletonMeta):
    """
        A class to represent a bank system.

        ...

        Attributes
        ----------
        clientsData : (key : (str , str) , value : Account)
            dictionary that save the data of the clients
        Methods
        -------
        validate_details(username ,account):
            check if the system has an account with the giving username and password
        deposit(account):
            deposit from the account after asking the user from where and how much he wants to deposit

        signUp():
            adding a user to the system after asking for a password and a username
        createAccount():
            making a survey with the user to find out what type of account he can have and make it then adding it to the
            system.
        createSavingsAccount(account):
            creates a saving account.
        show_account(account):
            shows the account details.
        deleteAccount(account):
            deletes the account from the system.
        withdraw(account):
            withdraw money from the account after asking the user how much he wants.

    """
    clientsData = {}

    def validate_details(self, username, password):
        """
        Parameters
        ----------
        username : str
            The choosing user name
        password : str
            The choosing password

        Returns
        -------
            the account
            else -1 .
        """
        if (username,password) in self.clientsData.keys():
            return self.clientsData.get((username,password))
        return -1

    def deposit(self, account):
        """
        Parameters
        ----------
        account : Account
            The account we want to deposit from

        Returns
        -------
        """
        if account:
            depo = int(input('Enter your deposit sum: '))
            choice = input('What account do you want to deposit to? Savings(s)/Main(m), (q) to quit: ')
            while choice != 'q':
                if choice == 's':
                    if account.savingsAcc:
                        if account.deposit_to_savings(depo):
                            print("The amount "+str(depo)+" has been deposited to your savings account!")
                            return
                        else:
                            print("No enough balance in the main account to continue this transaction.")
                            return
                    else:
                        print("You have no savings account, Please create one first.")
                        return
                elif choice == 'm':
                    print("The amount " + str(depo) + " has been deposited to your main account!")
                    account.deposit(depo)
                    return
                else:
                    choice = input("Please choose a valid character(s/m) or press (q) to quit.")

    def signUp(self):
        found = True
        while found:
            username = input('Please choose a username: ')
            found = False
            for details in self.clientsData.keys():
                if username == details[0]:
                    print("This username is already in use.")
                    found = True
                    break

        password = input('Please choose a password: ')
        self.clientsData[(username,password)] = None
        print("You have signed up successfully!")

    def createAccount(self):
        """
        asking for the username and password  then make a survey to know witch type of account fit the user
        the most
        """
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        acc = self.validate_details(username, password)
        if not acc:
            choice = input("Are you a business owner (y/n)?")
            while True:
                if choice == 'y':
                    while True:
                        try:
                            salary = int(input('Please enter your salary: '))
                            if 0 < salary < 25000:
                                print("You deserve a private account!")
                                self.clientsData[(username, password)] = PrivateAccount()
                            elif 25000 <= salary < 100000:
                                print("You deserve a business account!")
                                self.clientsData[(username, password)] = BusinessAccount()
                            elif salary >= 100000:
                                print("You deserve a premium account!")
                                self.clientsData[(username, password)] = PremiumAccount()
                            else:
                                print("Please insert a positive number.")
                                continue
                            print("Your account was created successfully!")
                            return
                        except:
                            print("Please insert a valid number!")
                            continue

                elif choice == 'n':
                    print("You deserve a private account!")
                    self.clientsData[(username,password)] = PrivateAccount()
                    print("Your account was created successfully!")
                    return

                else:
                    choice = input("Please choose a valid answer (y/n)")
        elif acc == -1:
            print("There is no such username or password in the database, PLease sign up first.")
        else:
            print("You already have an account!")

    def createSavingsAccount(self, account):
        """
        Parameters
        ----------
        account : Account
            the account that we want to create a saving account in it .
        """

        if not account:
            return
        else:
            account.createSavingsAcc()

    def show_account(self, account):
        """
        Parameters
        ----------
        account : Account
            the account we want to show his details
        """

        if not account:
            return
        else:
            account.show()

    def deleteAccount(self, account):
        """
        Parameters
        ----------
        account : Account
            the account we want to delete
        """
        if not account:
            return
        else:
            account.deleteSavingsAcc()
            account.withdrawAll()
            for d in self.clientsData.keys():
                if self.clientsData.get(d) == account:
                    self.clientsData[d] = None
                    return

    def withdraw(self, account):
        """
        Parameters
        ----------
        account : Account
            the account we want to withdraw from .
        """
        if not account:
            return
        else:
            amount = int(input("Please enter amount to withdraw:"))
            if account.withdraw(amount):
                print("An amount of "+str(amount)+" has been withdrawn successfully!")
            else:
                print("You don't have enough balance to complete this transaction")


