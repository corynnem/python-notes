bicycles = ['trek', 'canondale', 'redline', 'specialized']


print(bicycles[2])
print(bicycles[1].title())       #title case element in list
print(bicycles[-1])              #access last element in list




bicycles[1] = 'yamaha?' # change an element in a list
print(bicycles[1])

bicycles.append('suzuki') # append suzuki to the end of the list
print(bicycles)

bicycles.insert(1, 'im a bike, vroom') # <= insert string at position 1
print(bicycles)

del bicycles[-1] # <= delete an item from list by index
print(bicycles)

print(bicycles.pop()) # <= removes and returns the last item in the list
print(bicycles.pop(2)) # <= remove an item from list by index
print(bicycles)

bicycles.remove('im a bike, vroom') # <= removing an item by value
print(bicycles)


foods = ['pizza', 'brownies', 'ice cream', 'dino nuggets', 'spinach', 'eggs', 'avocado']
# foods.sort() # <= sort a list alphabetically forever 
print(foods)

print(sorted(foods)) # <= temporarily sort a list
print(foods)

foods.reverse() # <= reverse order of list
print(foods)

print(len(foods)) # <= like .length()

