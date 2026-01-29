# 08-10.py
#  Purpose:    Example: finding a string within a string
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:34 PT


s1 = 'spam and eggs'
s1.replace('and','without')
print(s1)
# the above shows that strings are immutable (cannot change)

s2 = s1.replace('and','without')
print(s2)
