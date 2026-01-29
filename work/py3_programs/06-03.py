# 06-03.py
#  Purpose:    Example: using a programmer-defined function
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:19 PT

# start of function definition
def cube( y ):
    return y * y * y
# end of function definition

# prints the cube of numbers 1 to 5
for x in range(1,6):
    print(cube(x))

# the last value of x is 5 
print("last value of x is:",x)
