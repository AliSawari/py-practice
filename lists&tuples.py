# lists 
# lists are same as arrays, they can hold multiple and different values
# lists just like arrays in other languages, start from 0

fruits = ['banana','apple','orange','avocado']

# lets see whats inside
print(fruits)

# replacing the 4th item
fruits[3] = 'grape'

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

# the __methodName__ format are called bound methods
# for example __add__ will add an item to the list and returns that list
# but doesnt affect the real fruits list
print(fruits.__add__(['eggs']))
print(fruits) # the list doesnt contain 'eggs'

# another bound method: __contains__
# this is the same as print('apple' in fruits) which will result in True
print(fruits.__contains__('apple'))

# bound method: this will return the actual size of the list in bytes
print(fruits.__sizeof__())




# tuples
# tuples are the same as lists but the values cant be changed once set

movies = ('Matrix', 'Fight Club', 'Se7en')
print(movies[2])

# the code below will raise an error because its a tuple
# so I will skip it but keep it in mind :)
# movies[2] = 'Forrest Gump'

# tuples have the same methods as the lists
print(movies.count('Matrix'))
print(movies.index('Se7en'))
print(movies.__contains__('Fight Club'))


# converting list to Tuple and and vv
days = ['sat','sun','mon','tue','wed','thu','fri']
# since days cant be changed we need a tuple so lets convert it
# simply calling the tuple function 
Days = tuple(days)
print(Days) # now we cant change its values :))

# and since movies can be changed so lets change it 
Movies = list(movies)
# now we can extend it :)
Movies.extend(['The Godfather', 'Silence of the Lambs'])
print(Movies)