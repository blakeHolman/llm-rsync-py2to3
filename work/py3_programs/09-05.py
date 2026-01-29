# 09-05.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 11:31 PT

filename = input('Enter a file name: ') 
try: 
  f = open (filename, "r") 
except: 
  print('There is no file named', filename)
