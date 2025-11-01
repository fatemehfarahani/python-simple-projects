#part1

import matplotlib.pyplot as plt
import pandas as pd

students_names=['Herin','Kai','Soobin','lia','hiyeh','teahyun']
scores=[19,20,18,15,14,16]

compiled_list=list(zip(students_names, scores))

print('Main name and score students list :\n')
print(compiled_list ,'\n')


new_list=list( filter( lambda x : x[1] > 15 , compiled_list) )

print('names and scores list after filter:\n')
print(new_list ,'\n')

#or we can use this :

my_dictionary = {name : score for name ,score in compiled_list}


print(f'Main names and scores list : \n\n {my_dictionary} \n')

my_dictionary2 = {name : score for name ,score in compiled_list if score > 15 } 

print(f'names and scores list after filter: \n\n {my_dictionary2}\n')


#part2 - The  first way

x=list(my_dictionary.keys())
y=list(my_dictionary.values())

plt.bar(x,y ,color='hotpink')
plt.title("Analyzing studen's scores")
plt.show()


#The  second way

df=pd.DataFrame(list(my_dictionary.items()),columns=['Name','Score'])
plt.bar(df['Name'], df['Score'] , color='skyblue')
plt.title("Analyzing studen's scores")
plt.show()

df.to_csv("Analyzing studen's scores.csv" , index=False)