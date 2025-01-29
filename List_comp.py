from IPython import get_ipython
from IPython.display import display
import numpy as np

# List comprehensions and functional programming examples
l = [1, 2, 3]
m = list(map(lambda x: x**2, l))
print(m)

l = [1, 2, 3, 8, 9, 66, 2]
m = list(filter(lambda x: x % 2 == 0, l))
print(m)

print([(x, y, z) for x in range(100) for y in range(x, 100) for z in range(y, 100) if x * x + y * y == z * z])

l = [1, 2, 3]
print([i * 2 for i in l])

l = ['hi', 'hello']
print([x.upper() for x in l])
print([x + " welcome" for x in l])

ar = np.array([[1, 2, 3], [4, 5, 6]])
print([a**2 for a in ar])

num = [1, 2, 3, 4, 5]
print([x * 5 for x in num])

num = [1, 2, 3, 4, 5]
print([x * 5 for x in num if x > 2])

dict_list = [{'name': 'abcd'}, {'name': 'efgh'}]
print([x['name'] for x in dict_list])

num = [1, 2, 3, 4, 5]
print([i * 5 if i == 3 else i for i in num])

num = [1, 2, 3, 4, 5]
# print(map(lambda i: i))  # This line doesn't produce any meaningful output

num = [1, 2, 3, 4, 5]
print([i if i >= 1 and i < 3 else i * 5 for i in num])

num = [1, 2, 3, 4, 5]
print([i * 5 if i == 3 else i for i in num if i > 1])
# print([lambda i: i * 5 if i == 3 else i, filter(i > 1, l)])  # This line has errors

n1 = [1, 2, 3, 4]
n2 = ['a', 'b', 'c', 'd']
print([(i, j) for i in n1 for j in n2])

num = [1, 2, 3, 4, 5]
f = ["apples", "pears", "mango"]
print([(f, i) for f, i in enumerate(f, start=1)])

print([i for i in range(100) if '3' in str(i)])

num = [1, 2, 3, 4, 5]
n2 = [6, 3, 8, 9, 2]
print([i for i in num if i in n2])

num = [1, 2, 3, 4, 5]
n2 = [6, 3, 8, 9, 2]
print([(i, i) for i in num if i in n2])
