#Write a NumPy program to test element-wise for positive or negative infinity.
import numpy as np

a = np.array([3.0 , 4, True, np.inf])
print("\n\tOriginal array")
print(a)

print("Test element-wise for positive or negative infinity:")
print(np.isinf(a))


#Array of all the even integers from 30 to 70
import numpy as np

array = np.arange(30,71,2)
print("\n\tArray of all the even integers from 30 to 70")
print(array) 


#REVERSE array
import numpy as np

a1 = np.arange(1,11)
print("\n\tarray in 1-20 arange")
print(a1)
reverse = a1[::-1]
print(reverse)


#Program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np

x = np.array([3,5])
y = np.array([2,5])
print("\n\tOriginal arrays: ")
print(x)
print(y)
#The Python Numpy greater_equal function checks whether the elements in a given array (first argument) is greater than or equal to a specified number(second argument). If True, True returned otherwise, False.
print("\n\tComparison-greater: ")
print(np.greater(x,y))
print("Greater or equal: ")
print(np.greater_equal(x,y))
print("Less: ")
print(np.less(x,y))
print("Less or equal: ")
print(np.less_equal(x,y))


#Find common values between two arrays.
import numpy as np
from numpy.lib.arraysetops import intersect1d

array1 = np.array([20,30,40,50,60])
print("\n\tArray1- " , array1)
array2 = np.array([30,50,70,10,20])
print("Arry2-" , array2)

print(intersect1d(array1,array2))


#compute the condition number of a given matrix.
import numpy as np
from numpy import datetime64, linalg as LA
array_to_compute = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
print("\n\tOriginal matrix:")
print(array_to_compute)
print("\nCompute the condition:")
compute = LA.cond(array_to_compute)
print(compute)

#Shuffle numbers between 0 and 10 (inclusive)
'''shuffle(x) can permute the elements in x randomly along the first axis. numpy. random. permutation(x) actually returns a new variable and the original data is not changed.'''
import numpy

frst_arr = np.arange(10)
np.random.shuffle(frst_arr)
print("\n\tUsing shuffle()\nWhich changes the original data in random order\n" , frst_arr)
print("\tUsing permutation which copies and changes in random but for another variable\n", np.random.permutation(frst_arr))


#Sort a given array of shape 2 along the first axis, last axis and on flattened array.
import numpy as np

arr_1 = np.array([[10,40], [30,20]])
print("\n\tOriginal array: ")
print(arr_1)
print("Sort along first axis")
print(np.sort(arr_1, axis=0))
print("Sort by last axis")
print(np.sort(arr_1))
print("Flattened sort")
print(np.sort(arr_1, axis=None))


#Add, subtract, multiply, divide arguments element-wise.
import numpy as np

print("\n\tAdd:")
print(np.add(2,3))
print("Substract: ")
print(np.subtract(2,3))
print("Multiply:")
print(np.multiply(2,3))
print("Divide")
print(np.divide(2,3))


#Find max or min value
import numpy as np

flattened_arr = np.array([[0,1], [2,3]])
print("\n\tOriginal array:\n" , flattened_arr)
print("Maximum value: ",np.amax(flattened_arr))
print("Minimum value: ", np.amin(flattened_arr))


#Convert numpy datetime64 to Timestamp.
import numpy as np
from datetime import datetime


dt = datetime.utcnow()
print("\n\tCurrent date:")
print(dt)

dt64 = np.datetime64(dt)
ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
print("Timestamp:\n",ts)

utc = datetime.utcfromtimestamp(ts)
print("UTC from Timestamp:\n" , utc)


#Concatenate element-wise two arrays of string.
import numpy as np

first_string = np.array(['Python', 'PHP'], dtype=np.str)
second_string = np.array([' Java', ' C++'], dtype=np.str)
print("\tArray1:\n ",first_string)
print("Array2:\n ",second_string)
print("New array:\n ",np.char.add(first_string,second_string))



