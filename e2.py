class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited:${amount}. New amount${self.__balance}")
        else:
            print("Deposited must be positive")
    
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance -=amount
            print(f"Withdraw:${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

account= BankAccount("Ishant", 1200)

print(f"Account holder: {account.account_holder}")

print(f"Balance: ${account.get_balance()}")

account.deposit(2000)
account.withdraw(400)


    