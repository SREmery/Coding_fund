# Task 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(8, 15)
print(rect.area())
print(rect.perimeter())

# Task 2

class BankAccount:
    def __init__(self, account_num, balance=0):
        self.account_num = account_num
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("error - invalid funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


bal = BankAccount("3344")
print(bal.get_balance()) 
bal.deposit(300)
print(bal.get_balance()) 
bal.withdraw(50)
print(bal.get_balance()) 



