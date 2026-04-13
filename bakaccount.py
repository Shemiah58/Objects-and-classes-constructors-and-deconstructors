class BankAccount:
    def __init__(self, acc_num, holder, initial_balance):
        self.__account_number = acc_num
        self.__account_holder = holder
        self.__balance = 0
        # Validate initial balance
        if initial_balance >= 0:
            self.__balance = initial_balance
        else:
            print("Initial balance cannot be negative")
    @property
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")

    def display_account_info(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ${self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self, acc_num, holder, initial_balance, interest_rate=0.05):
        super().__init__(acc_num, holder, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")

class CurrentAccount(BankAccount):
    def __init__(self, acc_num, holder, initial_balance, overdraft_limit=500):
        super().__init__(acc_num, holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
        
            new_balance = self.balance - amount
            self.balance = new_balance
            print(f"Withdrawn: ${amount}")
