# 09-04.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 11:31 PT

def copyFile(oldFile, newFile): 
  f1 = open(oldFile, "r") 
  f2 = open(newFile, "w") 
  while 1: 
    text = f1.read(50) 
    if text == "": 
      break 
    f2.write(text) 
  f1.close() 
  f2.close() 
  return 

filecopy = "C:\\temp\\tester2copy.txt" #this file will be created
fileold = "C:\\temp\\tester2.txt" # existing file
copyFile(fileold, filecopy)
