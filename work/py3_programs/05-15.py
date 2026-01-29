# 05-15.py
#  Purpose:    Example: how to use a loop within a loop
#              a nested while loop

#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 27th June 2007, 9:08 PT


print("This is the start of the program")

x = 1
while (x < 6):
    print() # prints a new line
    print("x = " + str(x), end=' ') # the , forces printing of the next item
                           # to be on the same line 
    x = x + 1
    y = 1
    while (y < 6):
        print("y = " + str(y), end=' ') # the , forces printing on the same line
        y = y + 1

'''
Notice that with a loop repeating 5 times,
***within*** a loop that repeats 5 times
means that you can control 25 processes.
'''
