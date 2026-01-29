# 09-01.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 8:37 PT

file1 = open('C:\\temp\\file1.txt','r')
# the line above opens C:\temp\file1.txt for reading
string = file1.readline()
print(string)
