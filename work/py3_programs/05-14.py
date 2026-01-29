# 05-14.py
#  Purpose:    Example: how to repeat a program at the user's request
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 19th October 2006, 7:58 PT


print("This is the start of the program")
answer = 'y'
while (answer == 'y' or answer == 'Y'):
    print("This is a statement from within the while loop")
    print("This is another statement from within the while loop")
    answer = input("Do you want to run this program again? y/n")
print("Goodbye!")
