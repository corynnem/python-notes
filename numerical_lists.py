for value in range(1, 5):   
    print(value)    # <= will only print 1-4


# fizzbuzz loop
for value in range(1, 100):
    if value % 3 == 0 and value % 5 == 0:
        print('fizzbuzz')
    elif value % 3 == 0: 
        print('fizz')
    elif value % 5 == 0:
        print('buzz')
    else: 
        print(value)


# use range to make a list of numbers
numbers = list(range(0, 21))
print(numbers)

#tell python to skip specific numbers in a range is the 3rd param
even_numbers = list(range(0, 21, 2))
print(even_numbers)

# simple stats with a list of numbers
print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))


# take each value in a list and increase it exponentially 
squares = [value**2 for value in range(1, 11)]
print(squares)