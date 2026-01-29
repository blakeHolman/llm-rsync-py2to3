# 05-17.py
#  Purpose:    Example: how to use a loop within a loop
#              a nested for loop

#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 27th June 2007, 9:45 PT


print "This is the start of the program"

for i in range (1,6):
    for j in range (1,6):
        print "i: " + str(i) + " j: " + str(j) 
    print        
'''
Notice that with a loop repeating 5 times,
***within*** a loop that repeats 5 times
means that you can control 25 processes.
'''
