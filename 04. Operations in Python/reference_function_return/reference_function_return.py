def increment_one(number):
    return number + 1

def multiply_two(number):
    return number * 2

number = 3
number = increment_one(number)
number = multiply_two(number)
print(number)

print(multiply_two(increment_one(3)))


