# lists 
# lists are same as arrays, they can hold multiple and different values

fruits = ['banana','apple','orange','grape']

# lets see whats inside
print(fruits)

# some list methods down here

# add an item to the list
fruits.append('pineapple')
print(fruits)

# extend the list with another list
fruits.extend(['pomegranate', 'apple', 'melon']);
print(fruits)

# how many apples are in the list
print(fruits.count('apple'))

# returns the position of the item.
print(fruits.index('pineapple'))

# insert an item and specify its position, so it will push the other items forward
fruits.insert(4, 'peach')
print(fruits)

# remove the item by its index and returns it
print(fruits.pop(2))
print(fruits)

# removing an item
fruits.remove('pineapple')
print(fruits)

# reverse the list, [1,2,3] => [3,2,1]
fruits.reverse()
print(fruits)

#  sorts the list alphabetically
fruits.sort()
print(fruits)

# the __methodName__  are called bound methods
# for example __add__ will add an item to the list and returns that list
# but doesnt affect the real fruits list
print(fruits.__add__(['eggs']))
print(fruits) # the list doesnt contain 'eggs'

# another bound method: __contains__
# this is the same as print('apple' in fruits) whichi will result in True
print(fruits.__contains__('apple'))

# bound method: this will return the actual size of the list in bytes
print(fruits.__sizeof__())