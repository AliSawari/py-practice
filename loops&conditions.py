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
print(len('two') < len('three')) 

# AND OR operators
print(True and False)
print(True or False)
print(12 or 0);

# conditions
# if..else
if True:
  print('its true')
else:
  print('no')

name = 'john'
age = 23

if age > 18 and  age < 30:
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 and less than 30 years old')

# a shorter format of the above code is : 

if(30 > age > 18):
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 and less than 30 years old')

if age>18 or name=='john':
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 or your name should be john')

# if...elif...else
if age>18:
  print('Welcome here {}'.format(name))
elif name == 'john':
  print('Welcome here {}'.format(name))
else:
  print('you have to be more then 18 or your name should be john')