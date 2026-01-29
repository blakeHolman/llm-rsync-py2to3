# 04-13.py
#  Purpose:    A nested if example (an if statement within another if statement)
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 4th October 2004, 13:21 PT

score = raw_input("Enter score: ")
score = int(score)
if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else:
	grade = 'C'
print "\n\nGrade is: " + grade
