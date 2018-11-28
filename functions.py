# functions in python

# add function takes 2 numbers and returns the sum
def add(a , b):
  c = a + b
  return c

# calling a function and storing the result in a variable
result = add(3, 5)
print(result)

# alternatively you can print out the result directly
print(add(12,90))

# a simple function that returns your info
# using the format() method in string
def sayHi(name, age):
  return "Hi, my name is {} and I am {} years old.".format(name, age)

print(sayHi("Ali",20))




# Python Built-in functions


# the range() function gives us a range of data from a start to an end
# lets print from 0 to 5
for x in range(0,5):
  print(x)
# it prints only to 4, because 0 is included, so we practically are printing 5 values

# the pow() function takes two numbers to execute x in power of y
nu = 2
print(pow(nu, 3))


# lets write the above function from scratch :)
# notice we already have a function for that in python which is pow()
# but lets just see how its done
def power(a,b):
  r = 1
  for x in range(0, b):
    r *= a
  return r

print(power(2,4))


# the len function returns the length of a list or string
here = 'something'
print("Length of here: ", len(here))

# convertion 
# use these functions to convert types 
num = 4
myL = ['one', 'two', 'three']
# to integer 
print(int(num))
# to float
print(float(num))
# to string
print(str(num))
# to tuple
tu = tuple(myL)
print(tu)
# to list
l2 = list(tu)
print(l2)


# hash returns the hash value of a value
print(hash('HashThis'))

# hex returns the lowercase hex value prefixed with 0x from an integer
print(hex(651))

# the open() function will take the path for a file and opens it
# second argument to open() is the mode, r for reading, w writing and e executing
# then we can read the data in file.txt
# I will open file.txt
txt = open('file.txt', 'r').read()
print(txt)

# alternatively, we can seperate the data by each line, we will use split() function
# which is a method for any string
lines = txt.split('\n')
print(lines)

# lets append line1 in the beginning of each line
for x in lines:
  print("Line", lines.index(x) + 1, x)
