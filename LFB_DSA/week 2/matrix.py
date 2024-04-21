import numpy as np

m1 = np.array([[1,2,3],
               [4,5,6],
               [4,7,6]])
m2 = np.array([[2,3,1],
               [5,6,9],
               [1,2,3]])

mul = np.dot(m1,m2)
print(mul)

diagonal = np.diag(m1)
print(diagonal)

np.fill_diagonal(m1,0)
print(m1)
