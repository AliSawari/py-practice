# conditions, Loops, Logical operators

# ---------------------- (operators) -----------------------



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




# ---------------------- (conditions) -----------------------



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


# ---------- (loops and iteration) -----------------------


# for
for boy in boys:
  print("this is boy %s" % boy)

# range method is a common method in python
# it sets a range to specify how many times to iterate
for x in range(5):
  print(x)

# start:stop
# note: stop wont be included
for x in range(3,5):
  print(x)

# start:stop:skip 
for x in range(2,8,2):
  print(x)

# while 
# += is just a shorthand assignment, see numbers.py
counter = 0
while counter < 10:
  print('counter: ', counter)
  counter += 1

# break statement
# this will stop the iteration if a condition stands true
counter = 0
while True:
  print('counter: ', counter)
  counter += 1
  if counter > 6:
    break

# continue statement
# continue will skip the current element and goes to the next one
# so the code below will print the odd numbers since we are skipping the even ones(x % 2 is 0)
for x in range(10):
  if x % 2 is 0:
    continue
  print(x)