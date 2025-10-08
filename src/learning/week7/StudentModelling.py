"""
File: StudentModelling.py
Author: Shiqi(Kiki) Su
Date: 2025-09-18 16:28
Description:
"""
from __future__ import annotations


class Course:
    def __init__(self, course_code: str, course_name: str, units: int = 2):
        self._course_code = course_code
        self._course_name = course_name
        self._units = units
        self._students = []

    def get_name(self) -> str:
        return self._course_name

    def get_code(self) -> str:
        return self._course_code

    def get_units(self):
        return self._units

    def get_students(self):
        return self._students

    def add_student(self, student: Student):
        if student not in self._students:
            self._students.append(student)


class Student(object):
    """Simple representation of a university student."""
    def __init__(self, name: str, student_num: int, degree: str):
        self._name = name
        self._student_num = student_num
        self._degree = degree
        self._grade: dict[Course, int] = {} # dictionary {course: grade}
        # list of (course, semester)
        self._current_course: list[tuple[Course, str]] = []
        # list of tuple (course and tuition fee.)
        self._enrolments: list[tuple[str, int]] = []

    def get_name(self) -> str:
        return self._name

    def get_student_num(self) -> int:
        return self._student_num

    def get_degree(self) -> str:
        return self._degree

    def set_degree(self, degree: str):
        self._degree = degree

    def get_first_name(self) -> str:
        name = self._name.split()
        return name[0] if name else ''

    def get_last_name(self) -> str:
        name = self._name.split()
        return name[-1] if len(name) >= 2 else ''

    def get_email(self) -> str:
        # email = f"{self.get_first_name().lower()}.{self.get_last_name().lower()}@uq.net.au"
        email = '{0}.{1}@uq.net.au'.format(self.get_first_name().lower(),
                                           self.get_last_name().lower())
        return email

    def add_grade(self, course: Course, grade: int, semester: str):
        """
        Adds a grade for the given course to this Student.

        Args:
            course (Course): The course code of the course.
            grade (int): Grade achieved in the course.
        """
        self._grade[course] = grade
        if semester:
            self._current_course.append((course, semester))
        course.add_student(self)

    def gpa(self) -> float:
        if not self._grade:
            return 0.0
        total_points = sum(self._grade * course.get_units()
                           for course, grade in self._grade.items())
        total_units = sum(course.get_units() for course in self._grade.keys())
        return total_points / total_units

    def get_current_course(self):
        return list(self._current_course)

    def enrol(self, course_code: str, fee: int):
        return self._enrolments.append((course_code, fee))

    def calculate_fees(self):
        total = 0
        for course_code, fee in self._enrolments:
            total += fee
        return total


    def __str__(self):
        return (f"'{self._name} ({self.get_email()}, "
                f"{self._student_num}, {self._degree})'")

    def __repr__(self):
        return (f"\"Student('{self._name}', '{self._student_num}',"
                f" '{self._degree}')\"")


def check_validity(self, students: list[Student]) -> bool:
    if len(students) == 0:
        return False

    for student in students:
        if self._student_num == student.get_student_num():
            return False
    return True




