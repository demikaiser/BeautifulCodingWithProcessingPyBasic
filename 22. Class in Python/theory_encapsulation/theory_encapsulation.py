
jake_name = "Jake"
jake_gender = "Male"
jake_residence = "South Korea"
jake_occupation = "Teacher"
jake_hobby = "Fishing"

alice_name = "Alice"
alice_gender = "Female"
alice_residence = "USA"
alice_occupation = "Teacher"
alice_hobby = "Music"

bob_name = "Bob"
bob_gender = "Male"
bob_residence = "Germany"
bob_occupation = "Student"
bob_hobby = "Soccer"

sally_name = "Sally"
sally_gender = "Female"
sally_residence = "Brazil"
sally_occupation = "Student"
sally_hobby = "Dance"


class Person:
    def __init__(self, name, gender,
                 residence, occupation,
                 hobby):
        self.name = name
        self.gender = gender
        self.residence = residence
        self.occupation = occupation
        self.hobby = hobby


jake = Person("Jake", "Male", "South Korea",
              "Teacher", "Fishing")
alice = Person("Alice", "Female", "USA",
               "Teacher", "Music")
bob = Person("Bob", "Male", "Germany",
             "Student", "Soccer")
sally = Person("Sally", "Female", "Brazil",
               "Student", "Dance")

print(jake.name)
print(alice.name)
print(bob.name)
print(sally.name)

