# 05-06.py
#  Purpose:    Example: use of continue in a loop
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 16:07 PT


while 1:
    print 'Spam'
    answer = raw_input('Press y for large fries ')
    if answer == 'y':
        print 'Large fries with spam, mmmm, yummy '
        continue
    answer = raw_input('Had enough yet? ')
    if answer == 'y':
        break
print 'Have a '
print 'nice day!'
