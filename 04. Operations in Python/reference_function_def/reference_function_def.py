fruit = "Apple"
number_of_letters = len(fruit)
wrapper = "<" * number_of_letters
fruit = wrapper + fruit
wrapper = ">" * number_of_letters
fruit = fruit + wrapper
print(fruit)

fruit = "Orange"
number_of_letters = len(fruit)
wrapper = "<" * number_of_letters
fruit = wrapper + fruit
wrapper = ">" * number_of_letters
fruit = fruit + wrapper
print(fruit)

fruit = "Banana"
number_of_letters = len(fruit)
wrapper = "<" * number_of_letters
fruit = wrapper + fruit
wrapper = ">" * number_of_letters
fruit = fruit + wrapper
print(fruit)


def wrap_fruit(fruit):
    number_of_letters = len(fruit)
    wrapper = "<" * number_of_letters
    fruit = wrapper + fruit
    wrapper = ">" * number_of_letters
    fruit = fruit + wrapper
    print(fruit)

wrap_fruit("Apple")
wrap_fruit("Orange")
wrap_fruit("Banana")



