# 06-06.py
#  Purpose:    Example: function with no return statement
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 6:30 PT

def times(x):
    for i in range(1,11):
        print "%d x %d = %d" % (i, x, i * x)

print "This is the 1 times tables:"
times(1)

print "This is the 2 times tables:"
times(2)
