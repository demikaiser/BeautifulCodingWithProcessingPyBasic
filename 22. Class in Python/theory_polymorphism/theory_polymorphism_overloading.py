class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def introduce(self):
        print("Hello I am" + self.name + ". (Person)")

    def introduce(self, name1):
        print(name1 + "! Hello I am" + self.name + ". (Person)")

    def introduce(self, name1, name2):
        print(name1 + ", " + name2 + "! Hello I am"
              + self.name + ". (Person)")


jake = Person("Jake", "Male")
jake.introduce()  # Hello I am Jake. (Person)
jake.introduce("Alice")  # Alice! Hello I am Jake. (Teacher)
jake.introduce("Alice", "Bob")  # Alice, Bob! Hello I am Jake. (Teacher)






