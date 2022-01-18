print("hello world")

#variables
# - variable declaration and initialization happen in the same step

message = "hi my name is corynne"
print(message)

# strings
# - almost the same rules as JS, "" === ''
# \t tab in a string
# \n next line in a string
string_one = "get out of town"
string_two = "\t\nno you!!!"

# concatenation 
print(string_one + string_two)

# string methods
name = "coryNne MaRie Moody"

# first letter of each word uppercase
print(name.title())

# letters all uppercase
print(name.upper())

# letters all lowercase
print(name.lower())

# stripping whitespace
whitespace = "   whitespace  "
print("|" + whitespace.rstrip() + "|")
print("|" + whitespace.lstrip() + "|")
print("|" + whitespace.strip() + "|")