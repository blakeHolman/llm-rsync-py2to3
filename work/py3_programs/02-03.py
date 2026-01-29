# 02-03.py

total = 0.0
count = 0
while count < 3:
    number=float(input("Enter a number: "))
    count = count + 1
    total = total + number
average = total / 3
print("The average is " + str(average))
