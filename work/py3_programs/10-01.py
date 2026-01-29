# 10-01.py
#  Purpose:    Example: sequential search of a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 11th November 2004, 14:05 PT


list1 = [11,27,36,44,51,22,65,1,78]
numbertofind = int(input("Enter a number\n"))
found = 0
for i in list1:
    if numbertofind == i:
        print(numbertofind, " at index: ",list1.index(numbertofind))
        found = 1
if found == 0:
    print("Number not found")
