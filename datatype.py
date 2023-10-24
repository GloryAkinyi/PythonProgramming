# Data type

number = 100  # int
second = 56.78  # float
text = "Hello there"  # str
ispythoninteresting = True  # bool

# storing multiple values in a variable
cars = ["toyota", "nissan", "vw"]  # List
fruits = ("banana", "oranges", "apples")  # Tuple
countries = {"Kenya", "Tanzania", "Tunisia", "Algeria"}  # Set
details = {
    "firstname": "Glory",
    "age": 34,
    "course": "web development",
    "nationality": "Kenyan"
}  # Dictionary

print(details["firstname"])
print(details)
print(details["age"])
print(second)
print(text)
print(cars)
print(countries)
print(ispythoninteresting)

# Determine a data type
print(type(text))
print(type(countries))
print(type(details))

# Typecasting - Converting one data type to another
print(float(number))
print(int(second))


