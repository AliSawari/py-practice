# string formating


myName = 'Ali'
# variable injection
# C style
print('hey my name is %s' % myName)
# using format method, I suggest this cuz C style could get a bit busy
print('hey my name is {}'.format(myName))

# return the length of the string
print(len('lets see the length'))

# word counting
print('Ali sawari Ali'.count(myName))

#  from:to character
print('Ok so lets see this'[0:10])

# from:to:skip character
print('Ok so lets see this'[0:10:2])

# reverser
print('this is another simple string'[::-1])

# uppercase and lowercase
print('want this to be upper?'.upper())
print('WANT THIS TO BE LOWER?'.lower())

# splitting, output will be a list
print('Hello world its a nice day huh?'.split(' '))

# encoding the string
print('Lets see this in encode'.encode('ansi'))