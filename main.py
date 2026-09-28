def greet_user(name):
  print(f"Hello, {name}! Welcome to Python!")
greet_user("Quan")

def add_numbers(a, b):
    total = a + b
    return total

result = add_numbers(10, 5)
print(f"10 + 5 = {result}")

def describe_pet(name, animal="dog"):
  print(f"{name} is a {animal}.")

describe_pet("Hazel")

def area_of_rectangle(width, height):
  area = width + height
  return area

room_area = area_of_rectangle(8, 5)
print(f"Area of Rectangle: {room_area} square feet")

def square(number):
  return number * number

def print_square_and_double(number):
    squared = number ** 2
    doubled = squared * 2
    print(f"Number: {number}")
    print(f"Square: {squared}")
    print(f"Double the square: {doubled}")

print_square_and_double(4)

def is_even(number):
  if number % 2 == 0:
    return True
  return False

for value in [2, 7, 10, 13, 22]:
  print(f"{value} is even? {is_even(value)}")