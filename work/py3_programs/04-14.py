# 04-14.py
#  Purpose:    A nested if example - using if/else
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 4th October 2004, 13:25 PT

score = input("Enter score: ")
score = int(score)
if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else:
        if score >= 55:
            grade = 'C'
        else:
            if score >= 50:
                grade = 'Pass'
            else:
                 grade = 'Fail'
print("\n\nGrade is: " + grade)
