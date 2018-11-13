# conditions, Loops, Logical operators

# operators
# equals/not to
print(True == True) # outputs True
print(False == True) # outputs False
print(False == False) # ...
print(4 == 4) 
print(4 != 4)

# greater/less/and equal then
print(5 > 6) 
print(2 < 2) 
print(2 <= 2) 
print(5 >= 4)
# with strings
# len function returns the length of string or list
print(len('two') < len('three')) 

# AND OR NOT operators
# and = both have to be true
# or = either of have to be true
# not = negative of that value
print(True and False)
print(True or False)
print(12 or 0);
print(not False) # => True
print(not True) # => False

# conditions
# if..else
if True:
  print('its true')
else:
  print('no')

name = 'john'
age = 23

# using and to combine 2 conditions
# .format is a string method, see strings.py
if age > 18 and  age < 30:
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 and less than 30 years old')

# a shorter format of the above code is : 

if(30 > age > 18):
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 and less than 30 years old')

# using or to combine 2 conditions 
if age>18 or name=='john':
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 or your name should be john')

# if...elif...else
# elif is another if but in chains and stands for else if
if age>18:
  print('Welcome here {}'.format(name))
elif name == 'john':
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 or your name should be john')

# if in is keywords
# the in operator checks if there's a specified value inside a list
# the is operator can be used for comparing variable to value 
# but not variable to variable like ==
 
# to understand lists(arrays) please see lists&tuples.py
boys = ['ali', 'ahmad', 'reza', 'mehdi']
if 'ali' in boys:
  print("Here's Ali")

if len(boys) is 4:
  print('4 boyz')
else:
  print('not 4 ')

# combining 2 keywords
if len(boys) is not 3:
  print('boyz are not 3') 

# same as above
if len(boys) != 3:
  print('boyz are not 3')



# loops and iteration

# for
for boy in boys:
  print("this is boy %s" % boy)
