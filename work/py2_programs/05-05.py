# 05-05.py
#  Purpose:    Example: use of break to end an infinite loop
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 16:02 PT


while 1:
    print 'Spam'
    answer = raw_input('Press y to end this loop')
    if answer == 'y':
        print 'Fries with that?'
        break
print 'Have a '
print 'nice day!'
