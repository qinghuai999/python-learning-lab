"""
File: InheritanceTask.py
Author: Shiqi(Kiki) Su
Date: 2025-09-28 14:17
Description: Week8 tutorial homework.
"""

from src.learning.week7.StudentModelling import Student, Course

class CollegeStudent(Student):
    def __init__(self, course_code: str, course_name: str,
                 college_name: str, college_fee: int):
        super().__init__(course_code, course_name)
        self._college = college_name
        self._college_fee = college_fee


    def get_college(self):
        return self._college

    def calculate_fees(self):
        return Student.calculate_fees(self) + self._college_fee
