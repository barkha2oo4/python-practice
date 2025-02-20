# -*- coding: utf-8 -*-
"""numpy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QYhZoltA63mhP8adk3x9cgWvIPBnujvk

The numpy is a multi-dimensional array object consisting of two parts --The actual data ,some metadata describes the stored data.They are indexed just like sequences are in python, starting from 0
"""

import numpy as np

a=np.array([])
a

a=np.array([[10,20,30],[40,50,60]])
a

#list is a 1 dimensional
list1=[[10,20,30],[40,50,60]]
list1

#here we are passing the list to an array and an array is created it is 2-dimensional
a=np.array(list1)
print(a)

a=np.array([[10,20,30],[40,50]])
print(a)
#colon should be consistent

a=np.array([[10,20,30],[40,0,50]])
print(a)

a=np.array([[10,20,30],[40,np.nan,50]])
print(a)

a=np.array([[10,"Sun",30],[40,0,50]])
print(a)
# more than 1 datatype cannot exist in array as it did in list

#in tuple there is more than one form of datatype
Tuple1=(10,20,78,39,38,"x","y")
import numpy as np
#array converts all other forms of datatype into a string when there is more than 1 type of datatype
array1=np.array(Tuple1)
print(type(array1))
print(type(Tuple1))
print(Tuple1)
print(array1)

i

list1 = [[10,20,30],[50,60,70,80]]
print (list1)
a= np.array ([[10,20,30],[50,60,70,80]])
print (a)
print (type(a))

#Changes in the sub list won’t impact main list
list1 = [10,20,30,40,50,60,70,80]
list2 = list1 [:3]
print (list2)
list2[1]=500
print (list2)
print (list1)

#If we update sliced array , parent array also gets impacted
array1 = np.array (list1)
print (array1)
array2 = array1 [:3]
print (array2)
array2 [0] =500
print (array1)
print (array2)

#But in Copy parent array won’t impacted
print (array1)
array2 = (array1 [0:3]).copy()
print (array2)
array2[1]=200
print (array1)
print (array2)

import numpy as np
a=np.arange(10,20,3)
a

a=np.arange(9)
print(a)
a = np.arange(10,20)
print(a)
a = np.arange(10,30,3)
print(a)#array are represented in form of list

"""## difference between array and list
***array ***-- it is represented in the form of"[]" just like list
it cannot except elements of more than 1 data type thus in such conditions it converts al other elements to string if there is a string available in the array
If we update sliced array , parent array also gets impacted
but in Copy parent array won’t impacted bold text

---


**list**--It is represented in form of "[]"
it can accept more than 1 data type ,
if we update sliced list , parent list don't get impacted

"""

a=np.arange(30)
b=a.reshape(10,3)
b

a=np.arange(30)
a=a.reshape((3,10))
print(a)

a=np.arange(30)
b=a.reshape((2,5,3))
print(b)

b=np.zeros((5,5))
b

b=np.ones((5,5))
print(b*3)
print(b)

mat1=np.arange(0,30)
mat2=np.reshape(mat1,(6,5),"F")
print(mat1)#F for Columns , C for rows
print()
print(mat2)

mat1=np.arange(0,30)
mat2=np.reshape(mat1,(6,5),"c")
print(mat1)
print()
print(mat2)

print (mat2)

print (mat2.T)#here T represents transpose

a = np.arange (9)
b = a.reshape (3,3)
b

a = np.arange (2,11)
c = a.reshape (3,3)
c

b+c

b-c

b/c

b//c

c**b

b

c

b@c

mat2

vector=np.linspace(50,80,6)
print(vector)

a=[1002,4567,2435,2643]
b=[7854,567,2575,9863]
c=[8683,1893,2535]
Sales=np.array([a,b,c])
print(Sales)

Sales[1]

Sales[1][2]

r={"EU":0,"APAC":1,"US":2}
r

q={"Q1":0,"Q2":1,"Q3":2,"Q4":3}

r["APAC"]

Sales[1][2]

a=[1002,4567,2435,2643]
b=[7854,567,2575,9863]
c=[8683,1893,2535]
print(Sales[r['APAC']][q['Q3']])
print(Sales[r["APAC"]][2])
print(Sales[r["EU"]][2])
print(Sales[r['EU']][q['Q2']])

Sales[r["APAC"]][q["Q3"]]

import numpy as np
arr1=np.arange(100,200)
arr1

print(arr1[10:],"\n")

print(arr1[:20],"\n")

print(arr1[10:20],"\n")

print(arr1[10:50:5],"\n")

print(arr1[::10])

arr_slice=slice(1,10,2)
print(arr_slice)
print(arr1[arr_slice])

slice

arr1=np.arange(0,9)
print(arr1)
arr2=arr1.reshape(3,3)
print("\n")
print(arr2)

arr2[1:,1:]

arr1=np.arange(9)
print(arr1)
arr1=arr1.reshape(3,3)
print("\n")
print(arr1)
print("\n")
arr2=arr1[0:2,0:2]
print(arr2)

print(arr1)

print(arr1.shape)
print(arr1.ndim)#dimensional array

print(arr1.itemsize)#gives no. of elements
print(arr1.dtype)#it give the datatype

print(arr1.size)
print(arr1.min())
print(arr1.max())
print(arr1.sum())
print(np.sqrt(arr1))
print(np.std(arr1))#standard deviation

#In Python, the numpy. empty() function is used to return new array of a given shape and type. It has random values and uninitialized entries
arrs=np.empty([3,2], dtype=float)
print(arrs)

arrs=np.empty([3,2], dtype=int)
print(arrs)

arrs=np.empty([3,3], dtype=str)
print(arrs)

#Slicing

import numpy as np
arr1= np.arange (100)
print (arr1[10:],'\n')
print (arr1[:20],'\n')
print (arr1[10:20],'\n')
print (arr1[10:50:5])
print (arr1[::10])

import numpy as np
arr1 =  np.arange(20)
print (arr1)
arr_slice = slice (1,10,2)
print (arr_slice)
print (arr1[arr_slice])

"""**We use dir to get all the commands of the library **"""

import pandas
dir(pandas)

#sorting of 2 dimensional array
arr=np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))

arr=np.array([[3,2,4],[5,0,1]])
print(arr)
print()
print(np.sort(arr,axis=0))



import numpy
for name in dir(numpy):
  print(name,end= "\t")

arr=np.array(["banana","cherry","apple"])
print(np.sort(arr)[::-1])

import numpy as np
arr=np.arange(10,19)
print(arr)
arr=np.delete(arr,[2,5])
print(arr)

arr1=np.arange(10,22)
arr2=arr1.reshape(3,4)
arr2

a=np.delete(arr2,1,0)
a