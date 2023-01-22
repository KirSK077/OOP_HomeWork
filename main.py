class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw_grade(self):
        grades_list = []
        for _ in self.grades:
            for j in self.grades.values():
                grades_list += j
            return round(sum(grades_list) / len(grades_list), 2)
        else:
            return 'Студент оценки за домашние задания еще не получал'

    def __str__(self):
        return f' Имя: {self.name} \n Фамилия: {self.surname} ' \
               f' \n Средняя оценка за домашние задания: {self.average_hw_grade()} ' \
               f' \n Курсы в процессе изучения: {", ".join(self.courses_in_progress)} ' \
               f' \n Завершенные курсы: {", ".join(self.finished_courses)}'

    def compare_student(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        if type(self.average_hw_grade()) == str or type(other.average_hw_grade()) == str:
            return f'Невозможно сравнить, один из студентов не имеет оценок'
        if self.average_hw_grade() > other.average_hw_grade():
            return f'Рейтинг успеваемости выше у студента: {self.name} {self.surname}'
        elif self.average_hw_grade() == other.average_hw_grade():
            return f'Рейтинг успеваемости у обоих студентов одинаковый'
        else:
            return f'Рейтинг успеваемости выше у студента: {other.name} {other.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        grades_list = []
        for _ in self.grades:
            for j in self.grades.values():
                grades_list += j
            return round(sum(grades_list) / len(grades_list), 2)
        else:
            return 'Оценки за лекции отсуствуют'

    def __str__(self):
        return f' Имя: {self.name} \n Фамилия: {self.surname} ' \
               f' \n Средняя оценка за лекции: {self.average_grade()}'

    def compare_lecturer(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        if type(self.average_grade()) == str or type(other.average_grade()) == str:
            return f'Невозможно сравнить, один из лекторов не имеет оценок'
        if self.average_grade() > other.average_grade():
            return f'Рейтинг одобрения студентами выше у лектора: {self.name} {self.surname}'
        elif self.average_grade() == other.average_grade():
            return f'Рейтинг одобрения у обоих лекторов одинаковый'
        else:
            return f'Рейтинг одобрения студентами выше у лектора: {other.name} {other.surname}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя: {self.name} \n Фамилия: {self.surname}'


student_1 = Student('Tom', 'Holt', 'man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Офисные программы']
student_2 = Student('Katy', 'Price', 'woman')
student_2.courses_in_progress += ['Python', 'JavaScript']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Nikita', 'Ivanov')
lecturer_1.courses_attached += ['Python', 'JavaScript']
lecturer_2 = Lecturer('Alexander', 'Gromov')
lecturer_2.courses_attached += ['JavaScript']

reviewer_1 = Reviewer('Ivan', 'Kuznetsov')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Sergey', 'Ponomarev')
reviewer_2.courses_attached += ['Python', 'JavaScript']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'JavaScript', 10)
reviewer_2.rate_hw(student_2, 'JavaScript', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'JavaScript', 10)

students_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def get_av_student_course_grade(students_list, course):
    grade_list = []
    for student in students_list:
        for key, val in student.grades.items():
            if key == course:
                grade_list += val
    return f'Средняя оценка успеваемости на курсе {course}: {round(sum(grade_list) / len(grade_list), 2)}'


def get_av_lecturer_course_grade(lecturer_list, course):
    grade_list = []
    for lecturer in lecturer_list:
        for key, val in lecturer.grades.items():
            if key == course:
                grade_list += val
    return f'Средняя оценка работы лекторов на курсе {course}: {round(sum(grade_list) / len(grade_list), 2)}'


print('Студенты:')
print(student_1)
print(student_2)
print('Лекторы:')
print(lecturer_1)
print(lecturer_2)
print('Эксперты:')
print(reviewer_1)
print(reviewer_2)
print('Сравнение успеваемости студентов:')
print(student_1.compare_student(student_2))
print('Сравнение качества работы лекторов:')
print(lecturer_1.compare_lecturer(lecturer_2))
print('Средняя оценка на курсах:')
print(get_av_student_course_grade(students_list, 'JavaScript'))
print(get_av_lecturer_course_grade(lecturer_list, 'Python'))
