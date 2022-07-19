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
    def __init__(self, name, surname):
        super().__init__(name, surname)
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


student_1 = Student('Student', '1', 'Gender 1')
student_1.finished_courses += ['Git']
student_1.finished_courses += ['C++']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['C']

student_2 = Student('Student', '2', 'Gender 2')
student_2.finished_courses += ['Python']
student_2.finished_courses += ['C']
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['C++']

student_3 = Student('Student', '3', 'Gender 1')
student_3.finished_courses += ['Git']
student_3.finished_courses += ['C++']
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['C']

student_4 = Student('Student', '4', 'Gender 2')
student_4.finished_courses += ['Python']
student_4.finished_courses += ['C']
student_4.courses_in_progress += ['Git']
student_4.courses_in_progress += ['C++']

mentor_1 = Mentor('Mentor', '1')
mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['Git']

mentor_2 = Mentor('Mentor', '2')
mentor_2.courses_attached += ['C++']
mentor_2.courses_attached += ['C']

lecturer_1 = Lecturer('Lecturer', '1')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['C']

lecturer_2 = Lecturer('Lecturer', '2')
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['C++']

lecturer_3= Lecturer('Lecturer', '3')
lecturer_3.courses_attached += ['Python']
lecturer_3.courses_attached += ['C']

lecturer_4 = Lecturer('Lecturer', '4')
lecturer_4.courses_attached += ['Git']
lecturer_4.courses_attached += ['C++']

reviewer_1 = Reviewer('Reviewer', '1')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['C']
reviewer_2 = Reviewer('Reviewer', '2')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['C++']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'C', 8)
reviewer_1.rate_hw(student_1, 'C', 9)
reviewer_1.rate_hw(student_1, 'C', 10)

reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'C++', 10)
reviewer_2.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'C++', 10)

reviewer_1.rate_hw(student_3, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Python', 8)
reviewer_1.rate_hw(student_3, 'Python', 7)
reviewer_1.rate_hw(student_3, 'C', 8)
reviewer_1.rate_hw(student_3, 'C', 10)
reviewer_1.rate_hw(student_3, 'C', 6)

reviewer_2.rate_hw(student_4, 'Git', 9)
reviewer_2.rate_hw(student_4, 'Git', 10)
reviewer_2.rate_hw(student_4, 'Git', 9)
reviewer_2.rate_hw(student_4, 'Git', 10)
reviewer_2.rate_hw(student_4, 'C++', 10)
reviewer_2.rate_hw(student_4, 'C++', 10)
reviewer_2.rate_hw(student_4, 'C++', 10)
reviewer_2.rate_hw(student_4, 'C++', 10)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'C', 10)
student_1.rate_lecture(lecturer_1, 'C', 9)
student_1.rate_lecture(lecturer_1, 'C', 10)
student_1.rate_lecture(lecturer_1, 'C', 9)
student_1.rate_lecture(lecturer_1, 'C', 10)

student_2.rate_lecture(lecturer_2, 'Git', 10)
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Git', 10)
student_2.rate_lecture(lecturer_2, 'C++', 9)
student_2.rate_lecture(lecturer_2, 'C++', 10)
student_2.rate_lecture(lecturer_2, 'C++', 9)

student_1.rate_lecture(lecturer_3, 'Python', 10)
student_1.rate_lecture(lecturer_3, 'Python', 10)
student_1.rate_lecture(lecturer_3, 'Python', 10)
student_1.rate_lecture(lecturer_3, 'Python', 10)
student_1.rate_lecture(lecturer_3, 'Python', 10)
student_1.rate_lecture(lecturer_3, 'C', 9)
student_1.rate_lecture(lecturer_3, 'C', 9)
student_1.rate_lecture(lecturer_3, 'C', 9)
student_1.rate_lecture(lecturer_3, 'C', 9)
student_1.rate_lecture(lecturer_3, 'C', 9)

student_2.rate_lecture(lecturer_4, 'Git', 10)
student_2.rate_lecture(lecturer_4, 'Git', 9)
student_2.rate_lecture(lecturer_4, 'Git', 9)
student_2.rate_lecture(lecturer_4, 'C++', 9)
student_2.rate_lecture(lecturer_4, 'C++', 9)
student_2.rate_lecture(lecturer_4, 'C++', 8)

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

print(student_1)
print(student_2)

print(lecturer_1 < lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)

print(student_1 < student_2)
print(student_1 == student_2)
print(student_1 > student_2)


def average_hw(all_students, course_in_progress):
    sum_grades_hw_of_course = 0
    num_grades_hw_of_course = 0
    for student_object in all_students:
        for learning_course in student_object.grades:
            if learning_course == course_in_progress:
                grades_hw_of_course = student_object.grades[learning_course]
                for i_grade in range(len(grades_hw_of_course)):
                    sum_grades_hw_of_course += grades_hw_of_course[i_grade]
                    num_grades_hw_of_course += 1
    return(sum_grades_hw_of_course/num_grades_hw_of_course)

def average_lecture(all_lecturers, course_in_attached):
    sum_grades_lecture_of_course = 0
    num_grades_lecture_of_course = 0
    for lecturer_object in all_lecturers:
        for attaching_course in lecturer_object.grades:
            if attaching_course == course_in_attached:
                grades_lecture_of_course = lecturer_object.grades[attaching_course]
                for i_grade in range(len(grades_lecture_of_course)):
                    sum_grades_lecture_of_course += grades_lecture_of_course[i_grade]
                    num_grades_lecture_of_course += 1
    return(sum_grades_lecture_of_course/num_grades_lecture_of_course)


list_object_students = [student_1, student_2, student_3, student_4]
course = "Python"
print(f'Средняя оценка за домашние задания по всем студентам по курсу {course}: {average_hw(list_object_students, course)}')
course = "Git"
print(f'Средняя оценка за домашние задания по всем студентам по курсу {course}: {average_hw(list_object_students, course)}')
course = "C"
print(f'Средняя оценка за домашние задания по всем студентам по курсу {course}: {average_hw(list_object_students, course)}')
course = "C++"
print(f'Средняя оценка за домашние задания по всем студентам по курсу {course}: {average_hw(list_object_students, course)}')


list_object_lecturers = [lecturer_1, lecturer_2, lecturer_3, lecturer_4]
course = "Python"
print(f'Средняя оценка за лекции всех лекторов по курсу {course}: {average_lecture(list_object_lecturers, course)}')
course = "Git"
print(f'Средняя оценка за лекции всех лекторов по курсу {course}: {average_lecture(list_object_lecturers, course)}')
course = "C"
print(f'Средняя оценка за лекции всех лекторов по курсу {course}: {average_lecture(list_object_lecturers, course)}')
course = "C++"
print(f'Средняя оценка за лекции всех лекторов по курсу {course}: {average_lecture(list_object_lecturers, course)}')