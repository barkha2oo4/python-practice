# -*- coding: utf-8 -*-
"""Apr 23 DS Python Dictionary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mWdSidqFm4VTZuoSaXhVxDoEISxC-1l9
"""

d1 = {'Name': 'Ben', 'Age':35}
d1 ['Name']

print (type (d1))

person = {'First_Name': 'John', 'Last_Name': 'Sam','Salary' : 5000}
person

person['Salary']

person = {'first_name':['John','Sam','Jim','Kim'],'Last_name': 'Len'}
person

person['first_name'][1]

person['first_name'].append ('Borker')
person

person['first_name'][1] = 'Judy'
person

person = {'first_name':['John','Sam','Jim','Kim'],'Last_name': 'Len'}
del (person)
person

person = {'first_name':['John','Sam','Jim','Kim'],'Last_name': 'Len'}
del (person['first_name'])
person

person = {'first_name':['John','Sam','Jim','Kim'],'Last_name': 'Len'}
person.clear()
person

person = {'first_name':['John','Sam','Jim','Kim'],'Last_name': 'Len'}
person

person.keys()

print (person.values ())

print (person.items())

print (person.get ('first_name'))

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1

dict1.items()

for (k,v) in dict1.items():
    print ('k',k)

for (k,v) in dict1.items():
    print ('k',k, '-v',v)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k:v**2 for (k,v) in dict1.items()}
print(double_dict1)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict['Color'] = 'Red'
thisdict

p1 = thisdict.pop("model")
p1

thisdict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict1 = thisdict
print(mydict1)

mydict1

mydict1['model'] = 'AAAABBB'
mydict1

thisdict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict['model']= 'AAAABB'
mydict

thisdict

family = {}

family = {'Father':{'Name': 'Bob', 'Age':2}}
family

family = {'Father':{'Name': 'Bob', 'Age':52},
          'Mother': {'Name': 'Judy', 'Age': 45}}
family

myfamily = {'Father': {'Name':'Tom', 'Age':60},
             'Mother':{'Name':'Ann', 'Age':55},
            "Children": {
                'Child1': {'Name':'Eric', 'Age':22},
                'Child2': {'Name':'Jen', 'Age':18}
            }
              }

myfamily.keys()

myfamily['Children']

myfamily['Children']['Child1']['Name']

customer_name = ['John','Sam','Rick','Jim', 'Ken']
order_id = ['AA123','AAA110','BBB111','BBB123','CCC100']

'''
Hello John  Your order id is AA123
Hello Sam  Your order id is AAA110
Hello Rick  Your order id is BBB111
Hello Jim  Your order id is BBB123
Hello Ken  Your order id is CCC100

'''
for (c,o) in zip (customer_name,order_id ):
    print ('Hello',c,' Your order id is',o)











