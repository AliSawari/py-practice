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