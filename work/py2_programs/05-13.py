# 05-13.py
#  Purpose:    Example: outputting strings and numbers
#              in a single print statement
#              using string formatting.
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 7:35 PT


x = 20
y = 75
print 'The sum of %d and %d is %d' % (x, y, x + y)

x = 20.512
y = 15.269
print 'The sum of %f and %f is %f' % (x, y, x + y)
x = 20.512
y = 15.269
print 'The sum of %0.2f and %0.2f is %0.2f' % (x, y, x + y)
