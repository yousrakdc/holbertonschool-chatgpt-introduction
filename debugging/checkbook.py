class Checkbook:
    """
    A simple class to manage a checkbook with basic operations like deposit, withdraw, and check balance.
    """
    def __init__(self):
        """
        Initialize a Checkbook object with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the checkbook.

        Parameters:
        -----------
        amount : float
            The amount to deposit into the checkbook.

        Returns:
        --------
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw funds from the checkbook.

        Parameters:
        -----------
        amount : float
            The amount to withdraw from the checkbook.

        Returns:
        --------
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance of the checkbook.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()