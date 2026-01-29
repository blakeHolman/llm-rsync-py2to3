# 09-02.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 10:38 PT

file1 = open("C:\\temp\\tester2.txt","w")
print(file1) # prints out details about the file
file1.write("Today is Monday\n") 
file1.write("Tomorrow is Tuesday")
file1.close()
