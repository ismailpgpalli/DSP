#Program to perform append operation
import numpy as np
a=input('Enter the array 1:')
b=input('Enter the array 2:')
for i in range(0,len(b)):
	a.append(b[i])
print a
