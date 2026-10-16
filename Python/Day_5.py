# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#         self.is_alive=True

#     def eat(self):
#         return f'{self.name} is eating'

#     def sleep(self):
#         return f'{self.name} is sleeping'

#     def make_sound(self):
#         return "Some generic sound"

# class Cat(Animal):
#     pass

# cat=Cat('Mi Mi','Cat')
# print(cat.make_sound())
# print(cat.eat())
# print(cat.sleep())

# class Bird(Animal):
#     pass


# b=Bird('Bird','Bird')
# print(b.make_sound())
# print(b.eat())
# print(b.sleep())

# print("="*30)

# # file read/write
# # w =>write [create new file or truncates existing]
# # a => append( create new file of append existing file)
# # x =>Exclusive creation(fails if exists)
# # r => Read
# f=open('a.txt','w')
# f.write('New Text')
# f.close()

# file=open('ab.txt','a')
# file.write('\nFrom Append Mode')
# file.close()

# # f=open('abc.txt','x')
# # f.write('X - mode')
# # f.close()

# with open('ab.txt','r') as f:
#     content=f.read()
#     print(content)

# print("-"*30) #csv file =>comma separated value

# import csv
# data=[
#     ['Name','Age','Department','Salary'],
#     ['Maung Maung',22,'IT',8500],
#     ['Hla Hla',23,'HR',5000]
# ]
# with open('employee.csv','w',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerows(data)

# with open('employee.csv','r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
employees=[
    {'name':'A','age':22,'position':'Developer'},
    {'name':'B','age':25,'position':'ADeveloper'},
    {'name':'c','age':27,'position':'BDeveloper'},
    {'name':'D','age':28,'position':'CDeveloper'},
    {'name':'E','age':29,'position':'DDeveloper'}
]
import csv
import time
with open('emp_dict.csv','w',newline='') as file:
    field_names=['name','age','position']
    writer=csv.DictWriter(file,fieldnames=field_names)
    writer.writeheader()
    time.sleep(3)
    writer.writerows(employees)

company={
    'name':'Cherry Co.Ltd',
    'founded':2022,
    'employee':500,
    'department':['Enginerring','Marketing','Sale','HR'],
    'location':{
        'city':'Yangon',
        'country':'Myanmar'
    },
    "public":True,
    'revenue':32432423
}
import json
with open('company.json','w') as file:
    json.dump(company,file,indent=4)

with open('company.json','r') as file:
    data=json.load(file)
    print(data)

print("-"*30) #11

import os
import platform
print(f'Operating System {os.name}')
print(f'Platform Name : {platform.system()}')

cwd=os.getcwd()
print(cwd)

os.makedirs('folder1')
os.makedirs('folder2/folder11/folder22')
time.sleep(5)
os.rmdir('folder1')
