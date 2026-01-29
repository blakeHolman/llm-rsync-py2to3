# 08-14.py
# Anne Dawson
# Sunday 20th March 2005, 04:44 PT
# Demonstration of printing Unicode characters
# For explanation, see:
# http://www.network-theory.co.uk/docs/pytut/tut_17.html
# For character charts go to:
# http://www.unicode.org/charts/
# http://www.unicode.org/charts/PDF/U2580.pdf (Block Elements)
# \u2588 is a Full Block which can be used to build up a black square 
str1 = 'Hello\u2588out there' # solid black block within text
print(str1)
str1 = '\u2588\u2588' #two full block characters
print(str1)
print()
print()
print("two lines of two full blocks")
print(str1)
print(str1)
print()
print()
# Note: a space is \u0020
print('two lines of two full blocks, two spaces, two full blocks:')
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print(str1)
print(str1)
print()
print()
print('two lines of two full blocks, the number 17 and two full blocks:')
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020' + '17' + '\u2588\u2588\u2588\u2588'
print(str1)
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print(str1)
