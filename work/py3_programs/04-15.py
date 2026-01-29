# 04-15.py
#  Purpose:    A nested if example - using if/elif/else
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 4th October 2004, 13:28 PT

score = input("Enter score: ")
score = int(score)
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 55:
    grade = 'C'
elif score >= 50:
    grade = 'Pass'
else:
    grade = 'Fail'
print("\n\nGrade is: " + grade)
