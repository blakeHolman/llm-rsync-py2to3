# 06-05.py
#  Purpose:    Example: importing programmer-defined functions
#              from its own module file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:56 PT

#  IMPORTANT:  myFunctions.py should be in the same folder as this file

import myFunctions

print("1 to 5 cubed")
for x in range(1,6):
    print(myFunctions.cube(x), end=' ')
print()
print()

print("1 to 5 doubled")    
for x in range(1,6):    
    print(myFunctions.doubleIt(x), end=' ')
