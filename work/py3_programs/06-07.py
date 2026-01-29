# 06-07.py
#  Purpose:    Example: a function with two return statements
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 6:37 PT

def division(x,y):
    if (y == 0):
        print("division by zero not allowed")
        return
    else:
        " returning %f divided by %f " % (x, y)
        return x / y

print(" 5.0 / 2  returns:")
result = division( 5.0 , 2 )
print(result)

print(" 5.0 / 0  returns:")
result = division( 5.0 , 0 )
print(result)
