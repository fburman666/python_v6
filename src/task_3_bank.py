class Bank:
    def __init__(self, balance=0, interest=0):
        self.__balance = balance
        self.__interest = interest
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def checkbalance(self):
        print(f"Du har: {self.__balance} kr på kontot")
        return self.__balance
    def apply_interest(self):
        sum = self.__balance * self.__interest * 0.01
        print(f"Din ränta blir: {sum} kr")
        return sum
    def afford_to_pay_bill(self, cost):
            if cost >= self.__balance:
                return False
            else:
                return True

