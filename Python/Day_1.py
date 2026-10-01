"""
Rules
Must not start with numbers
Must not contain space
Must not keywords - class,if
Must not contains specaial chars
"""
"""
Convention
snake_case,camelCase
"""
#predefined , bulid-in
#userdefined
print('Hi',1,2,3,True) #sep=" "
print('Hi',1,2,3,True,sep="*") #sep="*"
print("Line1",end=". ")#end
print("Line2",end=". ")
print("Line3")

f=open('a.txt','a')
text='\nLorem ipsum dolor sit amet consectetur adipisicing elit. Debitis, repudiandae doloremque laudantium sapiente, sit sint quis deleniti similique suscipit magni corporis omnis consequatur atque eaque aspernatur, beatae nulla esse officia?'

print(text,file=f)

num1=10;num2=20
#Num1 is 10 and num2 is 20
print("Num1 is "+str(num1)," and  ","Num2 is "+str(num2))

print(f'Num1 is {num1} and num2 is {num2}')
print('Num1 is {1} and num2 is {0}'.format(num2,num1))

#Operators
#Arithmetic operator
#+,-,*,%(remainder),/,// (quotient)
print(3/2)
print(3//2)

#Assignment operator
#=,+=,-=,..
num1=10
num1+=2 # num1=num1+2=10+2=12

#Comparison or Relational 
#==,!=,>,<,>=,<=

#Logical Operator
#and , or , not
# and => all True =>True
# or => one True => True
con=3<5 and 3==4 and 2==0 and True
print(con)
# not 
a=True
b=not a #False
c=not b #True #Toggle case

#membership operator
#in , not in

string='ap' not in 'apple'
print(string)

#identity operator
#is , is not
num1=2;num2=2
print(num1 is num2)
l1=list();l2=list()
print(l1 is l2)

#range
for i in range(10):#0-9 #end
    print(i)

for i in range(1,11):#start,end
    print(i)

for i in range(1,11,2):#start,end,step
    print(i)

#10-1
print("---------------------")
for i in range(10,0,-1):
    print(i)

"""
* * * * *
* * * * *
* * * * *

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""
# row=outer loop 
# col=inner loop
for i in range(3):
    for j in range(5):
        print('* ',end="")
    print()
print("----------")

for i in range(3):
    print("* "*5)

print("----------")
for i in range(1,4):
    print(f'{i} '*5)


#row-5 , col-5
for i in range(1,6):
    for j in range(1,6):
        print(f'{j} ',end="")
    print()

print("--------------")
for i in range(1,6):
    print("1 2 3 4 5")

string='PythonProgramming'
#in , in range
for s in string:
    print(s)
print("="*30)

for i in range(len(string)):#Hello => 5 => 0-4 , 0-5
    print(string[i])

# flow control / control flow
# loop , if-else,break,continue
for i in range(20):
    if i==12:
        break
    print("i value ",i)
print('-'*30)
for i in range(30):
    if i==16:
        continue
    print('value ',i)

if 3>2 :
    print('If Statement')
else:
    print('Else Statement')

num1=20
if num1<30:
    print(1)
elif num1==50:
    print(2)
elif num1<10:
    print(3)
elif num1>5:
    print(4)
else:
    print('Else')
# for ,while

v=1
while v<10:
    print('V',v)
    v+=1

# while True:
#     name=input("Enter Name >> ")
#     password=input("Enter Password >> ")
#     if name=='khine' and password=='123':
#         print('Login Success')
#         break
#github => mail 

# list
l=list() # empty list
l1=[]
print(l1,l2)
print(type(l),type(l1))
#insertion order , duplicate
l=[1,2,3,11,12,0,11,12,'Hello',5.6]#FIFO , LIFO
print(l)#stack,queue
print(len(l))
print(l[0])
for num in l:
    print(num)
print("----------")
for i in range(len(l)):
    print(l[i])
print(l[:3])#0-2
print(l[1:6])#1-5
print(l[3:])
