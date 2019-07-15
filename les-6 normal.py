class Human:
    def __init__ (self, surname, name, mother = None, father = None):
        self.surname = surname
        self.name = name
        self.mother = mother
        self.father = father

class Teacher(Human):
    grades = []
    def __init__ (self, surname, name, subject):
        Human.__init__(self, surname, name)
        self.subject = subject

class Student(Human):
    grade = None
    def __init__ (self, surname, name, mother, father, grade):
        Human.__init__(self, surname, name, mother, father)
        self.grade = grade

    def __str__(self):
        return f'{self.surname} {self.name[0].upper()}.'

    def getParents:
        return f'{self.mother} and {self.father}'

class School:
    students = []
    teachers = []
    grades = []
    sch_number = int()
    def __init__(self, sch_number: int, grades: lst):
        self.sch_number = sch_number
        self.grades = grades    #исхожу из того, что школа знает,
                                # какие у неё есть классы

    @property
    def get_teachers(self):
        return self.teachers

    def add_teacher(self, teacher: Teacher):
        if teacher is Teacher:
            self.teachers.append(teacher)
        else:
            print('This person is not a teacher')

    def add_grade(self, grade: Grade):
        if grade is Grade:
            self.grades.append(grade)
        else:
            print('Not a grade')

    def add_student(self, student):
        if student is Student:
            self.students.append(student)
        else:
            print('This is not a student')

    def get_all_students(self):
        return self.students

class Subject:
    def __init__(self, subject):
        self.subject = subject

class Grade:
    school = None
    teachers = []
    students = []
    def __init__ (self, num_let):
        self.num_let = num_let

    @property
    def get_teachers:
        return self.teachers

    def add_teacher(self, teacher: Teacher):
        if teacher is Teacher:
            self.teachers.append(teacher)
            teacher.grades.append(self)
        else:
            print('This person is not a teacher')

    @property
    def get_students:
        return self.students

    def add_student(self, student: Student):
        if student is Student:
            self.students.append(student)
        else:
            print('This is not a student')



#cоздаём представителей классов

School_342 = School(324, ['8A', '8B', '10A'])

student1 = Student('Ivanov', 'Pyotr', 'Ivanova Maria', 'Ivanov Andrey', '8A')
student2 = Student('Volkova', 'Anastasia', 'Volkova Anna', 'Volkov Dmitry', '8A')
student3 = Student('Komov', 'Vyacheslav', 'Komova Elizaveta', 'Komov Anton', '8B')
student4 = Student('Danko', 'Ekaterina', 'Danko Elena', 'Danko Artyom', '8B')
student5 = Student('Slavina', 'Olga', 'Slavina Inna', 'Slavin Makar', '10A')
"""
понимаю, что не красиво, но не придумала, как студентов сначала сделать списком так,
чтобы это тоже не было вручную:
В разборе дз список людей создавался генератором сразу в список,
но в жизни людей вбивают в базу руками
"""
School.add_student(student1)
School.add_student(student2)
School.add_student(student3)
School.add_student(student4)
School.add_student(student5)


teacher1 = Teacher('Kolotova', 'Anna', 'maths')
teacher2 = Teacher('Korotko', 'Valentin', 'maths')
teacher3 = Teacher('Rostova', 'Violetta', 'russian')
teacher4 = Teacher('Kosheleva', 'Maria', 'russian')
teacher5 = Teacher('Kataev', 'Oleg', 'economics')
teacher6 = Teacher('Tarachuk', 'Evgenia', 'economics')

School.add_teacher(teacher1)
School.add_teacher(teacher2)
School.add_teacher(teacher3)
School.add_teacher(teacher4)
School.add_teacher(teacher5)
School.add_teacher(teacher6)

