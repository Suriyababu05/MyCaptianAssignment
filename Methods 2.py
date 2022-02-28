#Change Values
list=["Suriya","Dolly","San","Deepak"]
list[1]="Riya"
print(list)
['Suriya', 'Riya', 'San', 'Deepak']
dict={"Name":"Suriya","Age":"21","Branch":"CSE"}
dict
{'Name': 'Suriya', 'Age': '21', 'Branch': 'CSE'}
dict["Age"]=20
print(dict)
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE'}
#Methods of List

l1=["San",2,"Bangalore","Hello"]
l1
['San', 2, 'Bangalore', 'Hello']
print(l1[2]
      )
Bangalore
l1[1]
2

l1
['San', 2, 'Bangalore', 'Hello']
l1[1]=20
print(l1)
['San', 20, 'Bangalore', 'Hello']
l1[1:2]=["21","Coimbatore"]
print(l1)
['San', '21', 'Coimbatore', 'Bangalore', 'Hello']
l1
['San', '21', 'Coimbatore', 'Bangalore', 'Hello']
l1.append("World")
l1
['San', '21', 'Coimbatore', 'Bangalore', 'Hello', 'World']
l1.insert(2,"Chennai")
l1
['San', '21', 'Chennai', 'Coimbatore', 'Bangalore', 'Hello', 'World']
l1
['San', '21', 'Chennai', 'Coimbatore', 'Bangalore', 'Hello', 'World']
l1.remove("21")
l1
['San', 'Chennai', 'Coimbatore', 'Bangalore', 'Hello', 'World']
l1.pop()
'World'
l1.pop(0)
'San'
l1
['Chennai', 'Coimbatore', 'Bangalore', 'Hello']
l1.pop(3)
'Hello'
l1
['Chennai', 'Coimbatore', 'Bangalore']
l1
['Chennai', 'Coimbatore', 'Bangalore']
for x in l1:
    print(x)

    
Chennai
Coimbatore
Bangalore
for i in range(len(l1)):
    print(l1[i])

    
Chennai
Coimbatore
Bangalore
l1
['Chennai', 'Coimbatore', 'Bangalore']
l1.sort()
l1
['Bangalore', 'Chennai', 'Coimbatore']
l2=[50,22,65,23]
l2
[50, 22, 65, 23]
l2.sort()
l2
[22, 23, 50, 65]
l1.sort(reverse = True)
l1
['Coimbatore', 'Chennai', 'Bangalore']
l1
['Coimbatore', 'Chennai', 'Bangalore']
l2
[22, 23, 50, 65]
l2.sort(reverse = True)
l2
[65, 50, 23, 22]
l1
['Coimbatore', 'Chennai', 'Bangalore']
newlist=l1.copy()
print(newlist)
['Coimbatore', 'Chennai', 'Bangalore']
l1
['Coimbatore', 'Chennai', 'Bangalore']
l2
[65, 50, 23, 22]
l3=l1+l2
l3
['Coimbatore', 'Chennai', 'Bangalore', 65, 50, 23, 22]

#Methods of Dictonary

dict
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE'}
dict={"Name":"Suriya","Age":"21","Branch":"CSE"}
dict
{'Name': 'Suriya', 'Age': '21', 'Branch': 'CSE'}
x=dict["Age"]
x
'21'
dict["Place"]="Bangalore"
dict
{'Name': 'Suriya', 'Age': '21', 'Branch': 'CSE', 'Place': 'Bangalore'}
dict["Age"]=20
dict
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE', 'Place': 'Bangalore'}
dict
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE', 'Place': 'Bangalore'}
dict.pop("Place")
         
'Bangalore'
dict
         
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE'}
for x in dict:
         print(x)

         
Name
Age
Branch
for x in dict:
         print(dict[x])

         
Suriya
20
CSE
for x,y in dict.items():
         print(x,y)

         
Name Suriya
Age 20
Branch CSE
dict
         
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE'}
NewDict=dict.copy()
         
NewDict
         
{'Name': 'Suriya', 'Age': 20, 'Branch': 'CSE'}
#Methods of Strings
print("HI")
         
HI
print('HI')
         
HI
a="Hello World"
         
print(a)
         
Hello World
a="""Hello World
python"""
         
print(a)
         
Hello World
python
a="Hello,World,!"
         
a[1]
         
'e'
len(a)
         
13
a
         
'Hello,World,!'
print(a[2:6])
         
llo,
a[:6]
         
'Hello,'
a[0:]
         
'Hello,World,!'
a[:-2]
         
'Hello,World'
a[-5:-2]
         
'rld'
a.upper()
         
'HELLO,WORLD,!'
a.lower()
         
'hello,world,!'
a.strip()
         
'Hello,World,!'
a.replace(","," ")
         
'Hello World !'
a.replace("!"," ")
         
'Hello,World, '
a.replace(" ",".")
         
'Hello,World,!'
a.split(",")
         
['Hello', 'World', '!']
a="Hello"
         
b="World"
         
c=a+b
         
c
         
'HelloWorld'
c=a+" "+b

c
         
'Hello World'
name="Suriya"
         
txt="My Name is "+name
         
print(txt)
         
My Name is Suriya
