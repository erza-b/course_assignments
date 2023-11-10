# Task 1

# School

# Make a class structure in python representing people at school. Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def class_student(self, class_number):
        print(f"{self.name} is studying,in {class_number} class ")


class Teacher(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching.")

    def display_salary(self):
        print(f"{self.name}'s salary is ${self.salary} with the id {self.employee_id}.")


person1 = Person("Mr. Jef", 30)
person1.introduce()

student1 = Student("Erza Berbatovci", 20, "12345")
student1.introduce()
student1.class_student(621)

teacher1 = Teacher("Mr. Johnson", 40, "98765", 50000)
teacher1.introduce()
teacher1.teach()
teacher1.display_salary()
