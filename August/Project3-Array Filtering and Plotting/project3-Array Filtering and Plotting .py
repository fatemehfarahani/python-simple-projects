import numpy as np
import matplotlib.pyplot as plt

mylist=list(range(1,101))
array=np.array(mylist)
print("main array:\n")
print(array)


array2= array[(array % 3 == 0) | (array % 5 == 0)]

print("filtered array:")
print(array2)

print('arry after add number 10 to each element:')
print(array2 +10)
print()

x=list(range(len(array2)))
y=array2

plt.plot(x, y, '*--r')
plt.title('Plot of array' , color='red')
plt.xlabel('Index' , color='red')
plt.ylabel('Value', color='red')
plt.show()
