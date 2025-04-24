from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, acc_num, balance=0):
        self.__acc_num = acc_num
        self.__balance = balance

    @property
    def account_number(self):
        return self.__acc_num

    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount >= -5000:
            self._set_balance(self.balance - amount)

    def display_account_type(self):
        return "Current Account"


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self._set_balance(self.balance - amount)

    def display_account_type(self):
        return "Savings Account"


def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {int(account.balance)}")
    print(f"Type: {account.display_account_type()}")
    print("-" * 50)


if __name__ == "__main__":
    
    sa1 = SavingsAccount("SA123", 1000)
    sa2 = SavingsAccount("SA456", 1500)

    sa1.deposit(500)     # 1000 + 500 = 1500
    sa1.withdraw(300)    # 1500 - 300 = 1200
    sa2.withdraw(1600)   # Denied silently

    
    ca1 = CurrentAccount("CA789", 0)
    ca2 = CurrentAccount("CA012", 1000)

    ca1.withdraw(200)    # 0 - 200 = -200
    ca2.withdraw(6000)   # Denied silently

    
    for acc in [sa1, sa2, ca1, ca2]:
        print_account_details(acc)