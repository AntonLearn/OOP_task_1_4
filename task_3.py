class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __student_average(self):
        sum_grades = 0
        num_grades = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_grades += grade
                num_grades += 1
        return sum_grades / num_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {self.__student_average()}\n'
        course_str = ",".join(self.courses_in_progress)
        res += f'Курсы в процессе изучения: {course_str}\n'
        finished_str = ",".join(self.finished_courses)
        res += f'Завершенные курсы: {finished_str}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        else:
            return self.__student_average() < other.__student_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}

    def __lecturer_average(self):
        sum_grades = 0
        num_grades = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_grades += grade
                num_grades += 1
        return sum_grades/num_grades

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__lecturer_average()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        else:
            return self.__lecturer_average() < other.__lecturer_average()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)