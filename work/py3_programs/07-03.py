# 07-03.py
#  Purpose:    Example: appending to an empty list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:17 PT

list1 = []
print(list1)
list1.append(67)
print(list1[0])
list1.append("spam")
print(list1)
print(list1[0])
print(list1[1])
# the following statement would generate an out-of-range error
#print list1[2]
