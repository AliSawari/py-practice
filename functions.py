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
def sayHi(name, age):
  return "Hello {} you are {} years old ".format(name, age)


print(sayHi("Ali",20))


# Python Built-in functions

# the len function returns the length of a list or string
here = 'something'
print("Length of here: ", len(here))

# convertion 
# use these functions to convert types 
num = 4
# to integer 
print(int(num))
# to float
print(float(num))
# to string
print(str(num))

# hash returns the hash value to a value
print(hash('HashThis'))

# hex returns the lowercase hex value prefixed with 0x from an integer
print(hex(651))