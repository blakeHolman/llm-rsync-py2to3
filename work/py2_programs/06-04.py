# 06-04.py
#  Purpose:    Example: using two programmer-defined functions
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:45 PT

def cube( y ):
    return y * y * y

def doubleIt ( z ):
 return 2 * z

print "1 to 5 cubed"
for x in range(1,6):
    print cube(x),
print
print

print "1 to 5 doubled"    
for x in range(1,6):    
    print doubleIt(x),



#  File:       myFunctions.py 
#  Purpose:    two programmer-defined functions
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:57 PT

def cube( y ):
    return y * y * y

def doubleIt ( z ):
 return 2 * z
