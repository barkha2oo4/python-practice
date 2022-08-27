# for loop
import argparse
from calendar import leapdays
import math
import os


n = 6
sum = 0
for i in range(0,n+1):
    sum+= i*i
    print(sum)

# given an integer n perform following conditional actions
import os
import math
import random
import sys
if__name__='__main__'
n = int(input().split())
if(n%2!=0):
    print("weird")
else:
   if(n>=2 and n<=5):
    print("Not weird")
   elif(n>=6 and n<=20):
    print("weird")
   elif(n>20):
    print("Not weird")

a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a!=b)
print(a=b)
print(a>=b)
print(a&b)
# largest of 3 numbers
a = int(input())
b = int(input())
c = int(input())
if(a>c):
    if(c>b):
        print(a)
    else:
        print(b)  
if(b>c):
    if(c>a):
        print(b)  
    else:
        print(a) 
else:
    print(c)              

for x in "banana":
   print(x , end=" ")

sum = 0
i = 0
n = int(input())
while(i<n):
    sum +=i
    i+= 1
    print(sum)
# sum of square of no.
    sum= 0
    i = 0
    while(i<=5):
        sum+=i*i
        print(sum)

for i in range(1,10):
    if i==5 or i==7:
        continue
    print(i)
    i = 0
while(i<10):
    i+=1
    if i==5 or i==7:
        print(i)
        # cube of a number
        sum = 0
        for i in range(1,6):
            cube = i**3
            sum += cube
            print(cube)
            print(sum)

            # NESTED STATEMENTS
            for i in range(1,5):
                for j in range(1,5):
                    print(i+j , end =" ")
                    print("/n")
                    # for finding if the mentioned year is leap year or not
def is_leap(year):

    if(year%400==0):
        leap= True
    elif(year%100==0) and (year%4!=0):
        leap = False
    elif(year%100!=0) and (year%4==0):
        leap = True
    else:
        leap = False
    return leap

    # LISTS
    list = ["physics","chemistry",1972,2020]
    print(ls[2], ls[-2])
    list1 = [1,2,3,4,5,67,78,687,90,89,24]
    print(list1[3:7])
    print(list1[4:])
    print(list1[:7])
    print(list1[:])
    print(max(list1))
    print(len(list1))
    print(min(list1))
    
    print(d)
    #CONSIDER A LIST (LIST=[]). YOU CAN PERFORM FOLLOWING COMMANDS
    N = int(input())
    k =[]
    for i in range(N):
        p = input().split()
        if (p[0] == "insert"):
            k.insert(int(p[1]),int(p[2]))
        if (p[0] == "print"):
            print(k)
        if (p[0] == "remove"):
            k.remove(int(p[1]))
        if (p[0] == "append"):
            k.append(int(p[1]))
        if (p[0] == "sort"):
            k.sort()
        if (p[0] == "pop"):
            k.pop()
        if (p[0] == "reverse"):
            k.reverse()
import array
# array 
l =[1,2,3,4,5,6,7,8,9,10]
a = array.array('i',l)
print("Initial reading :")
for i in (a):
    print(i, end=" ")
    Sliced_array = a[3:8]
    print("\n Slicing elements in a range 3-8 : ")
    print(Sliced_array)
    Sliced_array = a[5:]
    print("\n Elements sliced from 5th")
    print(Sliced_array)
    Sliced_array = a[:]
    print("\n printing all elements using slice operation")
print(Sliced_array)



def miniMaxSum(ar):
    argparse.sort()
miniSum = 0
maxSum = 0
for i in range(4):
    miniSum += argparse[i]
    print(miniSum , end =" ")
for i in range(4,0,-1):
    miniSum += argparse[i]
    print(miniSum , end =" ")

    if__name__=='__main__' 
    arr = list(map(int,input().rstrip().split()))
     
miniMaxSum(argparse)

# BIRTHDAY CAKE
for i in range(4,0,-1):
 print(i)

#  FUNCTIONS---
def minimum(num):
    mini = 10000
    for i in num:
     if(i<mini):
        mini = i
ls =[1,32,56,344,87,90]   
print(minimum(ls))
print(min(ls))
sums = 0
for i in ls:
    sums+=i
    print(sums)
    print(sum(ls))
    print(len(ls))

    def power(value1,value2):
        return value1**value2
    print(power(2,10))