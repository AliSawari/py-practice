# dictionary
# dictionary is a key-value store
# you can think of a dictionary as a list but instead of indexing, we use keys
# to address our items

shopping_list = {
  'chocolate_bars': 2,
  'apple': 4,
  'milk': 2,
  'frying_oil': 1 
}

# accessing an item by its key
print(shopping_list['apple'])

# alternatively you can define a dictionary with the 'dict' built-in function
# it takes tuples to specify the key and the value 
shopping_list = dict({
  ('chocolate_bars', 2),
  ('apple', 4),
  ('milk', 2),
  ('frying_oil', 1),
  ('foo', 'not bar')
})

print(shopping_list['foo'])