# 04-16.py
#  Purpose:    Demo of DeMorgan's Laws:
#  1.  a Not And is equivalent to an Or with two negated inputs
#  2.  a Not Or is equivalent to an And with two negated inputs
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 21st March 2005, 05:53 PT
#  Test data: 0 0, 0 1, 1 0, 1 1
#  For ***any*** value of x and y, (not(x < 15 and y >= 3)) == (x >= 15 or y < 3)
#  Common uses of De Morgan's rules are in digital circuit design
#  where it is used to manipulate the types of logic gates.
#  Also, computer programmers use them to change a complicated statement
#  like IF ... AND (... OR ...) THEN ... into its opposite (and shorter) equivalent.
#  http://en.wikipedia.org/wiki/De_Morgan%27s_law
#  http://www.coquitlamcollege.com/adawson/DeMorgansLaws.htm

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
print((not(x < 15 and y >= 3)))
print((x >= 15 or y < 3))
