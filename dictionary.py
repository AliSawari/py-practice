# dictionary
# dictionary is a key-value store
# you can think of a dictionary as a list but instead of indexing, we use keys
# to address our items

shopping_list = {
  'chocolate_bars': 2,
  'apples': 4,
  'milks': 2,
  'frying_oils': 1 
}

# accessing an item by its key
print(shopping_list['apples'])

# alternatively you can define a dictionary with the 'dict' built-in function
# it takes tuples to specify the key and the value 
shopping_list = dict({
  ('chocolate_bars', 2),
  ('apples', 4),
  ('milks', 2),
  ('frying_oils', 1),
  ('foo', 'not bar')
})

print(shopping_list['foo'])

# to change a value simply:
shopping_list['foo'] = 'indeed a bar'

# you can use numbers as keys too 
myData = {0:'a', 1:'b', 2: 'c'}

print(myData)

# using dictionary in loops 

# printing the keys and the values 
for x in shopping_list:
  print("We have",shopping_list[x],x)

# logical states 
print('frying_oils' in shopping_list)

# dictionary methods

# get will fetch an item in the dictionary, if it didnt exist, a default value 
# is replaced
print(myData.get(3, 'there is no such value'))

# this method will erase all values in the dictionary
myData.clear()
print(myData)

# this method will create a copy from another dictionary
shoppingList2 = shopping_list.copy()
print(shoppingList2)

# this method will return the keys in a dictionary
print(shopping_list.keys())