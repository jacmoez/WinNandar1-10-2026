class Phone:
    model="2026"

p=Phone()
print(p.model)

class Computer:
    def __init__(self):#constructor
        print('=== Init function ===')

c=Computer()

class Car:
    def __init__(self,name,price): # self => this
        self.name=name
        self.price=price

car=Car("Toyota",3000)
print(car.name,car.price)

car1=Car("Swift",4000)
print(car1.name,car1.price)

print("="*30)

class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
        self.transactions=[]

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transactions.append(f'Deposit : ${amount}')
            return  f'Deposited ${amount} . New Balance {self.balance}'
        return  'Depoist amount must be > 0'
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            self.transactions.append(f'Withdraw : -${amount}')
            return  f'Withdraw ${amount} . New Balance {self.balance}'
        return "Insufficient funds"

    def get_balance(self):
        return f'Balance : ${self.balance}'

    def get_statement(self):
        return "\n".join(self.transactions)

account=BankAccount('Maung Maung',5000)
print(account.get_balance())
print("Statements : \n",account.get_statement())
print("-"*30)
print("=== After Deposit ===")
account.deposit(300)
print(account.get_balance())
print("Statements : \n",account.get_statement())
print("=== After Withdraw ===")
account.deposit(100)
print(account.get_balance())
print("Statements : \n",account.get_statement())

print("="*30)


class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        self.current_page=0
    def __str__(self):
            return f'Book :\nTitle : {self.title}, Author : {self.author}, Price : {self.pages}'
b=Book('Title 1',"author 1",300)
print(b)
# print(f'Book :\nTitle : {b.title}, Author : {b.author}, Price : {b.pages}')
b=Book('Title 2',"author 1",500)
print(b)
# print(f'Book :\nTitle : {b.title}, Author : {b.author}, Price : {b.pages}')

print("="*30)

class Temperature:
    def __init__(self,celsius=0):# private
        self.__celsius=celsius

    def getCel(self):
        return  self.__celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self,value):
        self.__celsius=value

t=Temperature(20)
print(t.getCel())
t.celsius=30
print(t.celsius)

# try -> except 
num1=input("Enter Number One : ")
# num2=input("Enter Number Two : ")
try:
    n1=int(num1)
    a=20
    print(a)
    print(5/10)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
    print('Number must be 0-9')
except Exception as e:
    print(e)

print("="*30)
def validateAge(age):
    if not 18<=age<=65:
        raise   Exception("Error Age between 18 and 65")
try:
    validateAge(15)
except Exception as e:
    print(e)
