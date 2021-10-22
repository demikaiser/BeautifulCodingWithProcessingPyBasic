class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

jake = Person("Jake", "Male")
print(dir(jake))
print("name" in dir(jake))
del jake.name
print("name" in dir(jake))




