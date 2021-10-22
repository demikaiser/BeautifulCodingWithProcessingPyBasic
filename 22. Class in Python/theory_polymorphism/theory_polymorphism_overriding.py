

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def introduce(self):
        print("Hello I am" + self.name + ". (Person)")


class Teacher(Person):
    def __init__(self, name, gender, teacher_id):
        super().__init__(name, gender)
        self.teacher_id = teacher_id

    def introduce(self):
        print("Hello I am" + self.name + ". (Teacher)")


class Student(Person):
    def __init__(self, name, gender, student_id):
        super().__init__(name, gender)
        self.student_id = student_id

    def introduce(self):
        print("Hello I am" + self.name + ". (Student)")


jake = Person("Jake", "Male")
jake.introduce()  # Hello I am Jake. (Person)

jake = Teacher("Jake", "Male", "Teacher 1")
jake.introduce()  # Hello I am Jake. (Teacher)


