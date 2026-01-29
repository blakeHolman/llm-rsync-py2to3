# 04-03.py
#  Purpose:    Displaying an object's memory location 
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 12:48 PT

number1 = raw_input("Enter first number:\n")
print number1, type(number1), id(number1)
number1 = int(number1)
print number1, type(number1), id(number1)
