# 10-02.py
#  Purpose:    Example: sequential search of a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 19th November 2008, 11:37 PT

mylist = [10,11,3,4,55,12,23,14,16]
n = len(mylist)
print(n)
for i in range(n):
    print(mylist[i], end=' ')

search = int(input("\nPlease enter a number to search for: "))
    
print(search)

found = False
for i in range(n):
    if mylist[i] == search:
        found = True
        index = i
print()

if found == True:
    print(str(search) + " found at index " + str(index))
else:
    print(str(search) + " not found")

        










#  File:       bubblesort.py 
#  Purpose:    Example: a program which demonstrates a bubble sort on
#              a list of 10 random integers
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Sunday 14th November 2004, 9:17 PT

import random

# define the bubble sort function
def sort(values):
   length = len(values)
   for time in range(0, length-1):
      for position in range(0, (length-time-1)):
         if values[position] > values[position+1]:
            temp = values[position]
            values[position] = values[position+1]
            values[position+1] = temp

# generate a list of ten random numbers
numbers = []
number = 0
while number < 10:
   value = random.randint(1,100)
   if not(value in numbers):
      numbers.append(value)
      number = number + 1

# show unsorted list, sort the list, and show sorted list
print("Before:", numbers)
sort(numbers)
print("After :", numbers)
