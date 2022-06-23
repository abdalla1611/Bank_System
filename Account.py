from SavingsAccount import *


class Account:
    """
        A class to represent an account.
        ...
        Attributes
        ----------
        balance : float
            how much money in the account
        num_of_actions : int
            how many actions did this account
        savingsAcc : SavingsAccount or None
            a SavingAccount object if the user wants a saving account else None
        Methods
        -------
        deposit(amount):
            updates the saving account balance.
        getBalance():
            returns the balance in this account
        check_interest():
            pass the implementation to the subclasses
        withdrawAll():
            withdraw all the money in the account.
        deposit_to_savings(amount):
            deposit the giving amount to the saving account
        createSavingsAcc():
            creates a Savings Account for this account
        show():
            shows the details of the account.
        deleteSavingsAcc():
            deletes the saving account .
    """

    def __init__(self):
        """
             Constructs all the necessary attributes for the Account object.
        """
        self.balance = 0.0
        self.num_of_actions = 1
        self.savingsAcc = None

    def check_interest(self):
        """
        abstractmethod that the Account subclasses provides the implementation .

        """
        pass

    def deposit(self, amount):
        self.balance += amount
        self.check_interest()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.check_interest()
            return True
        return False

    def withdrawAll(self):
        print("Your " + type(self).__name__ + " has been deleted, an amount of " + str(
            self.balance) + " has been withdrawn!")

    def deposit_to_savings(self, amount):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            self.savingsAcc.updateBalance(amount)
            self.check_interest()
            return True

    def createSavingsAcc(self):
        self.check_interest()
        if self.savingsAcc:
            print("You already have a savings account!")
        else:
            self.savingsAcc = SavingsAccount()
            print("A new savings account has been created successfully!")

    def show(self):
        self.check_interest()
        print(self)
        if self.savingsAcc:
            print(self.savingsAcc)
        else:
            print("no savings account to show")

    def deleteSavingsAcc(self):
        if not self.savingsAcc:
            print("No savings account to be deleted")
        else:
            print("Your savings account has been deleted, an amount of " + str(
                self.savingsAcc.getBalance()) + " has been withdrawn!")
            del self.savingsAcc
            self.savingsAcc = None

    def __repr__(self):

        return type(self).__name__ + ":-\n" + "Balance: " + str(self.balance) + ", Number of actions: " + str(
            self.num_of_actions) + '\n'


class BusinessAccount(Account):
    """
        BusinessAccount , children of Account

        this type of account has an interest of 5% for each 10 actions

    """

    def __init__(self):
        super().__init__()

    def check_interest(self):
        """
        increment the actions by 1 and then checks if it equal to 10 , if yes then take an interst of 5% from the
        balance .
        """
        self.num_of_actions += 1
        if self.num_of_actions == 10:
            self.balance = 0.95 * self.balance
            self.num_of_actions = 0


class PrivateAccount(Account):
    """
        privateAccount , children of Account

        this type of account has an interest of 5% for each 5 actions
    """

    def __init__(self):
        super().__init__()

    def check_interest(self):
        """
        increment the actions by 1 and then checks if it equal to 5 , if yes then take an interst of 5% from the
        balance .
        """
        self.num_of_actions += 1
        if self.num_of_actions == 5:
            self.balance = 0.95 * self.balance
            self.num_of_actions = 0


class PremiumAccount(Account):
    """
         privateAccount , children of Account
         this type of account has an interest of 2.5% for each 10 actions

     """

    def __init__(self):
        super().__init__()

    def check_interest(self):
        """
        increment the actions by 1 and then checks if it equal to 10 , if yes then take an interst of 2.5% from the
        balance .
        """
        self.num_of_actions += 1
        if self.num_of_actions == 10:
            self.balance = 0.975 * self.balance
            self.num_of_actions = 0
