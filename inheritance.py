# -*- coding: utf-8 -*-
"""inheritance.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mkeZhhqcLZq9Bk9K5lFDcXrRGS0HL4_C

Write a program to create a class Employee . Display the personal information and salary details of 5 employees using single inheritance
"""

lst = [3, 2, 1, 5, 6]
x = list(map(lambda x: x**3, lst))
print(x)

4*5**2

class Employee:
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=salary
  def display(self):
    print("the name of the employee is",self.name)
    print("The age of the employee is",self.age)
    print("salary",self.salary)
class details(Employee):
  pass
em1=details("sunaina",23,45677)
em2=details("naina",23,30000)
em3=details("saina",23,43000)
em4=details("getakshi",23,39000)
em5=details("rehana",23,67630)
em1.display()
print(" ")
em2.display()
print(" ")
em3.display()
print(" ")
em4.display()
print(" ")
em5.display()

2/2

"""Wap that extends the class Employee.Derive 2 classes Manager and Team Leader from Employee class.Display all the details of the employee working under the class leader and employee"""

class Employee:
  def personinfo(self):
    self.name=input("name of the employee: ")
    self.age=int(input("age of the employee is: "))
    self.salary=int(input(" salary: "))
class Manager(Employee):
  def __init__(self):
    print("The employees working under manager")

class Team_leader(Employee):
  def __init__(self):
    print("The employees working under team leader")
em1=Manager()
em1.personinfo()
print(" ")
em2=Team_leader()
em2.personinfo()