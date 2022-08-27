import array
from re import L

'''
l =[1,2,3,4,5,6,7,8,9,10]
a = array.array('i',l)
c = ("i"+ str(l))
print("Initial reading :")
for i in range(1,len(l)):
    print(i, end=" ")
    Sliced_array = l[3:8]
    print("n Slicing elements in a range 3-8 : ")
    print(Sliced_array)
    Sliced_array = a[5:]
    print("\n Elements sliced from 5th")
    print(Sliced_array)
    Sliced_array = c[:]
    print("\n printing all elements using slice operation")
    print(Sliced_array)
    # swapcase
def swap_case(s):
    k = list(s)
    for i in range(len(s)):
       if k[i].isupper():
        k[i]=k[i].lower()
       else:
        if k[i].islower():
         k[i] = k[i].upper()
    s=""       
    for i in k:
        s+=i
    return s
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)'''
    