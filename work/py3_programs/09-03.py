# 09-03.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 10:56 PT

file2 = open("C:\\temp\\tester2.txt","r")
print(file2) # prints out details about the file
string1 = file2.read()
print(string1)
file2.close()
file2 = open("C:\\temp\\tester2.txt","r")
string1 = file2.read(5)
print(string1)
string1 = file2.read(5)
print(string1)
string1 = file2.read(5)
print(string1)
file2.close()
