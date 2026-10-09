"""
#[] => empty list
#list()=> empty list
fruits=['apple','orange','mango','lemon']
print(fruits)
phone=['xiaomi',2022,True,0.23]
print(phone)

list_from_string=list('Hello')
print(list_from_string)

#0-10
list_from_range=list(range(0,11))
print(list_from_range)

l=[1,2,3,4,5]
print(l)
l.append(10)
print(l)
l.insert(1,100)
print(l)
l.extend([11,12,13,14,15])
print(l)

l+=[111,222,333,2,3,4,5]
print(l)

l.remove(13) #0bj
print(l)

deleted_value=l.pop()#last =>return deleted value
print(deleted_value)

del_by_index_value=l.pop(4)
print(del_by_index_value)

del l[1]
print(l)

del l[4:8]
print(l)

sorted_list=sorted(l)
print(sorted_list)

l.reverse()
print(l)

print("-"*30)

# 1-100
nums=[ i for i in range(1,101)]
print(nums)

# 1 , 100
nums=[ i for i in range(2,101,2)]
print(nums)


# 1-20
# 1 ,3, 5=>'1>odd'
nums=[f'{i} > even'  if i%2==0  else f'{i} > odd' for i in range(1,21)]
print(nums)
"""

l1=[1,2,3];l2=[1,2,3]
print(l1==l2)
print(l1>l2)
print(l1 is l2)
print(min(l1),max(l1))

total=0
for num in l1:
    total+=num
    print(num)
print(total)

print(sum(l1))

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][2])
print(matrix[1])

a,b,c=[1,2,3]
print('A',a,b,c)

a,*rest,last=[1,2,3,4,5,6]
print(a,rest,last)

l=[11,12,13,14,15]
l[0]=110
print(l)

# insertion order maintain
# duplicate value
# FIFO

#tuple => list
# const
t1=()
t2=tuple()
print(t1,t2,type(t1),type(t2))

t=1,2,3,4,5
print(t, type(t))

t=(11,12,13,14,15)
print(t,type(t))

d={}
print(d,type(d))
d=dict()
print(d,type(d))
person={
    "name":"Hla Hla",
    "age":20,
    "city":"Yangon",
}
print(person)
print(person['name'])
print(person.get('age'))
print(person.get("country",'Myanmar'))
person['email']='h@email.com'
print(person)
person['age']=22
print(person)

print('name'  in person)

keys=person.keys()
print(keys)

values=person.values()
print(values)

print(person)

items=person.items()
print(items)

for k in    person.keys():
    print(k)

for v in person.values():
    print(v)
for k,v in person.items():
    print(k,' - ',v)

for item in person.items():
    print(item)
    print(item[0],item[1])


employees={
    "emp1":{'name':'MaungMaung','age':30,'dept':"IT"},
    "emp2":{'name':'HlaHla','age':28,'dept':"HR"},  
}
print(employees['emp1']['name'])
print(employees['emp2']['dept'])
#{1:1,2:4,...}
square={i:i*i for i in range(1,101)}
print(square)

d={'one':1,'two':2,'three':3}
sw={ v:k   for k,v in d.items()}
print(sw)

ks=['computer','phone','fruit']
vs=['Dell','Xiaomi','Apple']
combined={ k:v for k,v in zip(ks,vs)}
print(combined)

p=combined.pop('phone')
print(p)
print(combined)

p=combined.popitem()
print(p)
print(combined)


# list,set,tuple,dict
es=set()
print(es,type(es))

s={1,2,3,'hello',True,0.3}
print(s)


mixed={1,(4,5)}
print(mixed)

for i in d:
    print(i)

mixed.update({1,2,3,4,5})
print(mixed)

a={1,2,3,4,5};b={4,5,6,7,8}
a.update(b)
print(a)

a.remove(4)
print(a)

a.discard(7)
print(a)

p=a.pop()
print(p)
print(a)

# a.remove(100)
# print(a)

a.discard(100)
print(a)

u1={1,2,3,4,5};u2={3,4,5,6,7,9}
print(u1|u2) #union
c1={'a','b','c','d','e'};c2={'e','f','g'}
print(c1.union(c2))

print(c1.intersection(c2))
print(c1&c2)
