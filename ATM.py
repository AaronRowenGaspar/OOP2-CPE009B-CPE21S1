class ATM():
    serial_number = 0

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []

    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        self.transactions.append(f"Deposit of {amount} to account {account.account_number}")
        print("Deposit Complete")

    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        self.transactions.append(f"Withdrawal of {amount} from account {account.account_number}")
        print("Withdraw Complete")

    def check_currentbalance(self, account):
        print(account.current_balance)

    def view_transactionsummary(self):
        for transaction in self.transactions:
            print(transaction)