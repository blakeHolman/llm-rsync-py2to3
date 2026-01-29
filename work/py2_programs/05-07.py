# 05-07.py
#  Purpose:    Example: 'sentinel-controlled' while loop
#              Calculates average score of a class
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 6:31 PT


# initialization phase
totalScore = 0     # sum of scores
numberScores = 0   # number of scores entered

# processing phase
score = raw_input( "Enter score, (Enter -9 to end): " )   # get one score
score = int( score )   # convert string to an integer

while score != -9: # -9 is used as a sentinel ( a lookout or sentry value )
    totalScore = totalScore + score
    numberScores = numberScores + 1
    score = raw_input( "Enter score, (Enter -9 to end): " )  
    score = int( score )
   
# termination phase
if numberScores != 0: # division by zero would be a run-time error
   average = float( totalScore ) / numberScores
   print "Class average is", average
else:
   print "No scores were entered"
