# class definition
class Student():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def get_info_string(self):
        return f'{self.name}, {self.age} years old, {self.sex}'

def main():
    # object creation based on the class
    students = []
    students.append(Student("Dominic", 19, "Male"))
    students.append(Student("Olivia", 21, "Female"))
    students.append(Student("Eric", 19, "Male"))

    print('LIST OF STUDENTS')
    print('================')
    for student in students:
        print(student.get_info_string())

if __name__ == "__main__":
    main()