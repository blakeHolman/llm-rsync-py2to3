# 12-01.py
#  Purpose:    Example: a recursive function
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 11th November 2004, 14:25 PT

def factorial(n): 
  if n == 0: 
    return 1 
  else: 
    return n * factorial(n-1) 

print(" 5! has a value of: ", end=' ')
result = factorial(5)
print(result)

print(" 4! has a value of:", end=' ')
result = factorial(4)
print(result)
