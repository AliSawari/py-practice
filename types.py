# this is the python data types :

# first of all print() is a function which will print the result to the output
print("Hi Welcome!")

# second of all this is a simple comment, comments will be ignored by the python interpreter

# single line comments 
'''
Multiple
Line
Commnets
'''

# types => 
# with their constructor functions

# strings
myName = 'Ali Sawari'
# constructor and converter function for string 
myName = str('Ali Sawari')

# whole numbers or int
myNum = 3
# constructor and converter function for integers
myNum = int(3)

# floating numbers or float
myFlo = 14.6
myFlo = float(14.6)

# None is the same as null or undefined value, it holds nothing and shows nothing
none = None

# booleans
myBool = True
myBool = bool(True)

# lists(arrays)
myList = [1,2,'Hello',3.14]
myList = list(1,2,'Hello',3.14)

# tuples (constant arrays)
myTuple = (1,2,3,4)
myTuple = tuple(1,2,3,4)

# dictionaries (key-value stores)
myDict = {'name':'Ali','lastName':'sawari', 'age': 20}
myDict = dict(['name', 'Ali'], ['lastName', 'sawari'], ['age', 20])

# functions
def MyFunc():
  print('Hello')

# classes
class MyClass:
  print('Hello')


# objects
myObj = object()
# or creating an object from a class 
myObj = MyClass()