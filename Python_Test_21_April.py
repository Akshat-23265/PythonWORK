# Q1
class Student:
    school_name="UPES"
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Akshat" , 19)
s2=Student("Sparsh" , 18)
print(f"School : {s1.school_name}")
print(f"School : {s2.school_name}")
print(f"Student 1 : {s1.name} {s1.age}")
print(f"Student 2 : {s2.name} {s2.age}")

# Q3
class MathHelper:
    @staticmethod
    def is_even(num):
        return num%2==0
print(MathHelper.is_even(8))
print(MathHelper.is_even(11))

# Q4
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self ,amount):
        self.__balance+=amount
        print(f"Deposit{amount} new Balance: {self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdraw {amount}, Remaining{self.__balance}")
        else:
            print("Not Enough Balance")
    def show_balance(self):
        print(f"Account Holder : {self.name} , Balance: {self.__balance}")
acc=BankAccount("Akshat", 10000)
acc.show_balance()
acc.deposit(5000)
acc.withdraw(6000)
acc.withdraw(90000)
acc.show_balance

# Q5
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
print(Student.__name__)
print(Student.__doc__)
print(Student.__module__)
print(Student.__dict__)

# Q6
class product:
    def __init__(self,name,price):
        self.name =name
        self.price=price
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"
    def __add__(self, other):
        return self.price + other.price
    def __eq__(self, other):
        return self.price == other.price
p1=product("Laptop" , 70000)
p2=product("Keyboard" , 15000)
p3=product("Mouce" , 3000)
print(p1)
print(p1 +p2)
print(p1==p3)
print(p1==p2)