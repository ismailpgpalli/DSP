#Program to perform linear-algebraic operations
import numpy as np
a=np.array(input('Enter first 2*2 matrix:'))
b=np.array(input('Enter second 2*2 matrix:'))
u=np.add(a,b)
print 'Addition of two matirces:\n',u
v=np.subtract(a,b)
print 'Subtraction of two matrices:\n',v
e=np.multiply(a,b)
print 'Element by element multiplication of two matrices:\n',e
f=np.dot(a,b)
print 'Multiplication of two matrices:\n',f
k=np.divide(a,b)
print 'Element by element division of two matrices:\n',k
y=np.linalg.inv(a)
print 'Inverse of\n',a,'\n is\n',y
z=np.linalg.eig(a)
print 'Eigen vectors of\n',a,'\n is\n',z
w=np.linalg.matrix_rank(a)
print 'Rank of a matrix of\n',a,'\n is\n',w
x=np.linalg.det(a)
print 'Determinant of\n',a,'\n is\n',x
s=np.linalg.eigvals(a)
print 'Eigen values of\n',a,'\n is\n',s
t=np.linalg.qr(a)
print 'qr decomposition of\n',a,'\n is\n',s
g=np.linalg.matrix_power(a,3)
print 'Matrix power of\n',a,'\n is\n',g
