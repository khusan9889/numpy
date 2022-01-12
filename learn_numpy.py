#Write a NumPy program to test element-wise for positive or negative infinity.
import numpy as np

a = np.array([3.0 , 4, True, np.inf])
print("Original array")
print(a)

print("Test element-wise for positive or negative infinity:")
print(np.isinf(a))


#Array of all the even integers from 30 to 70
import numpy as np

array = np.arange(30,71,2)
print("Array of all the even integers from 30 to 70")
print(array) 


#REVERSE array
import numpy as np

a = np.arange(1,11)
print("array in 1-20 arange")
print(a)
reverse = a[::-1]
print(reverse)

