jake_name = "Jake"
jake_gender = "Male"
jake_teacher_id = "Teacher 1"
jake_student_id = None

alice_name = "Alice"
alice_gender = "Female"
alice_teacher_id = "Teacher 2"
alice_student_id = None

bob_name = "Bob"
bob_gender = "Male"
bob_teacher_id = None
bob_student_id = "Student 1"

sally_name = "Sally"
sally_gender = "Female"
sally_teacher_id = None
sally_student_id = "Student 2"


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):
    def __init__(self, name, gender, teacher_id):
        super().__init__(name, gender)
        self.teacher_id = teacher_id


class Student(Person):
    def __init__(self, name, gender, student_id):
        super().__init__(name, gender)
        self.student_id = student_id


jake = Teacher("Jake", "Male", "Teacher 1")
alice = Teacher("Alice", "Female", "Teacher 2")
bob = Student("Bob", "Male", "Student 1")
sally = Student("Sally", "Female", "Student 2")


