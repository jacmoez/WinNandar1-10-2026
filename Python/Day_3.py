# build-in/predefined function 
# user-defined function 

def greet():
    print('Hello')

greet()

g=lambda :print('Hello')
g()

def findSquare(num):
    print(f'Square of {num}= {num*num}')

fSquare=lambda  num:print(f'Square of {num}= {num*num}')
findSquare(3)
fSquare(3)

print('-'*30)
def findTotal(num1,num2):
    r=num1+num2
    return  f'Total = {r}'
    
value=findTotal(2,3)
print(value)

fT=lambda   num1,num2:  f'Total = {num1+num2}'
v=fT(2,3)
print(v)
print('-'*30)

def showUserInfo(name,age,city):
    print(f'Name = {name}, Age = {age}, City = {city}')

sUI=lambda  name,age,city: print(f'Name = {name}, Age = {age}, City = {city}')

def productInfo(name,price=200,count=0):
    print(f'Product Name : {name}\nPrice : {price}\nCount : {count}')
productInfo("Phone",300)
productInfo("Laptop")
productInfo("Mouse")
productInfo(count=20,name="Keyboard",price=100)

pIF= lambda name,price=200,count=0:print(f'Product Name : {name}\nPrice : {price}\nCount : {count}')
print('-'*30)
#string - function [build-in]
string="Hello python Programming"
print(string[0])
print(len(string))
for i in range(len(string)):
    print(string[i])

print('-'*30)
for c in string:
    print(c)
print('-'*30)
print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())
print(string.swapcase())
print(string.casefold())

st=string.startswith('H')
print(st)

stt=string.upper().startswith('h'.upper())
print(stt)

print('-'*30)
s='Hello Python'
print(s.find('Python'))
print(s.index('H'))

print(s.find('a'))
#rindex(),rfind()
# print(s.index('a'))#error
print(s.index('o'))
print(s.rfind('o'))

# Cs1@ => 8
# 
ph="09345345" # 0-9
print(ph.isdigit())
st="hello"
print(st.isalpha())
st="rfsd3231"
print(st.isalnum())#isupper()??

s="  hello   "
st=s.strip()
print(f'***{s}***')
print(f'***{st}***')
print(f'***{s.lstrip()}***')
print(f'***{s.rstrip()}***')

s="----------python--------"
print(f'***{s}***')
print(f'***{s.strip('-')}***')

s="a,b,c,d,e"
l=s.split(",")
print(l)
l=s.split(",",2)
print(l)


s="hello programming"
print(s.replace('hello','hi'))
print(s)

print("-".join(('python','java','php')))#list,set,tuple,

text="Hello Python"
print(text[0])
print(text[:3])
print(text[2:])
print(text[-1])
print(text[::-1])

print("-"*30)
#number
a=abs(-3)
b=abs(3)
print(a,b)
print(pow(3,2))#3^2
print(round(3.1425342))
print(round(3.5425342))
print(round(3.1425342,3))

print("-"*30)
#math
import math
print(math.ceil(23.1))
print(math.floor(3.9))

print(math.sqrt(9))

# random
import random
print(random.random())
print(random.randint(1,100))

p=random.randrange(0,21,5)
print(p)

l=['hla hla','ma ma','su su','tun tun','thura']
print(random.choice(l))
print(random.choices(l,k=3))
print(random.sample(l,k=3))
print(random.shuffle(l))
print(l)
