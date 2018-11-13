# classes in python

class Person:
  # the __init__ function get called when an object of Person is created
  # it takes 2 arguments, name and age, self is needed in order to set properties
  # self refers to the object which is being created
  def __init__(self, name, age):
    # assigning properties to the object based on the input data
    self.name = name
    self.age = age

  # defining methods to our new object
  # we need self to get our properties
  def sayHi(self):
    return "Hello my name is {} and I am {} years old".format(self.name, self.age)

# creating our new object
Ali = Person('Ali Sawari', 20)

# getting properties
print(Ali.name)
print(Ali.age)

# calling methods
print(Ali.sayHi())