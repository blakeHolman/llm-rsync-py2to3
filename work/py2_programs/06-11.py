# 06-11.py
#  Purpose:    Demonstrates the use of Python functions
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Sunday 29th October 2006, 12:48 PT                                                                    
                                                                     
                                                                     
                                             
'''
    Thanks to HW for the idea behind this program.

    Note that this is a multi-line comment which starts and ends with
    three single quote marks (')
    
    Note that functions can be defined anywhere,
    as long as they're defined before they're called.

    Note the use in this program of a simple pause function,
    to pause a program until a key is pressed.

    Note that when a function is called, all the lines in the
    function definition (def) are executed in order,
    then the program resumes at the point after the function call.

    Note that this program script starts executing at the line:
    startMessage()
    followed by the line:
    clearScreen()
    followed by the line:
    print "Testing this program"
'''



def pause():
    raw_input("\n\nPress any key to continue...\n\n")

def quitMessage():
    print "Thank you for using this program"
    print "Goodbye"
    
def printThreeLines():
    for i in range(1,4):
        print 'this is line ' + str(i)

def printNineLines():
    for i in range(1,4):
        printThreeLines()

def startMessage():
    print "This program demonstrates the use of Python functions"
    pause()
    
def blank_Line():
    print
    
def clearScreen():
    for i in range(1,26):
        blank_Line()



startMessage()
clearScreen()
print "Testing this program"
printNineLines()
pause()
clearScreen()
printNineLines()
blank_Line()
printNineLines()
pause()
clearScreen()
quitMessage()
