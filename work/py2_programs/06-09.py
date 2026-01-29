# 06-09.py
#  Purpose:    Example: a program with a Boolean function
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 7:21 PT

def isPositive(x):
    if (x >= 0):
        return 1 # 1 is true
    else:
        return 0 # 0 is false
    
x = float(raw_input("Enter a positive or negative number: "))
result = isPositive(x)
print result
print isPositive(x)
