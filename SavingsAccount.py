class SavingsAccount:
    """
        A class to represent a saving  account.

        ...

        Attributes
        ----------
        balance : int
            how much money in the saving account
        Methods
        -------
        updateBalance(amount):
            updates the saving account balance.
        getBalance():
            returns the balance in this account
    """

    def __init__(self):
        """
            Constructs all the necessary attributes for the SavingAccount object.
        """
        self.balance = 0

    def updateBalance(self, amount):
        """
        Parameters
        ----------
        amount : int
            the amount of money we want to add to this account
        """
        self.balance += amount

    def getBalance(self):
        """
        :returns
            the balance in this account
        """
        return self.balance

    def __repr__(self):
        """
        :return:
             how we want to represent the saving account
        """
        return "Savings Account:- "+"Balance: " +str(self.balance)+'\n'