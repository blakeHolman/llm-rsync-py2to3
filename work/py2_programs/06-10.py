# 06-10.py
#  Purpose:    Example: a polymorphic function
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 7:34 PT

def doubleIt(x):
    return (2 * x)

y = 3
print doubleIt(y)
z = "Spam "
print doubleIt(z)

# This program works because the * operator can be used with
# numbers and with strings.  This is an example of Polymorphism.

# Poly means "many" and morph means "form"

# Polymorphism : the meaning of the operations depends on the objects
# being operated on. The * operator is said to be "overloaded"

# An overloaded operator behaves differently depending on
# the type of its operands.
