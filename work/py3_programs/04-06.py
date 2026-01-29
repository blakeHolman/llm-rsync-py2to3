# 04-06.py
#  Purpose:    Examples of use of arithmetic operators 
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:10 PT

# mixing data types in expressions
# mixed type expressions are "converted up"
# converted up means to take the data type with the greater storage
# float has greater storage (8 bytes) than a regular int (4 bytes)

print(2 + 4.0)
print(6 - 4.0)
print(6 * 3.0)
print(6 / 3.0)
print(6 % 3.0)
print(6 // 3.0) # floor division: always truncates fractional remainders
print(-5.0)
print(3**2.0)   # three to the power of 2
