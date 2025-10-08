"""
File: InheritCalls.py
Author: Shiqi(Kiki) Su
Date: 2025-09-28 12:00
Description:
"""
from __future__ import annotations

from symtable import Class


class Employee(object):
    """
    A salaried employee.

    """

    def __init__(self, name: str, salary: float) -> None:
        """
        Initialise a new Employee instance.

        Parameters:
            name (str): The employee's name.
            salary (float): The employee's annual salary.
        """

        self._name = name
        self._salary = salary

    def get_name(self) -> str:
        """
        (str) Return the name.
        """

        return self._name

    def wage(self) -> float:
        """
        (float) Return the forgnightly wage.
        """

        return self._salary / 26


class Worker(Employee):
    def __init__(self, name: str, salary: float, manager: Employee) -> None:
        super().__init__(name, salary)
        self._manager = manager

    def get_manager(self) -> Employee:
        """
        Get the manager information
        Returns:
            Employee: Return the entity Employee
        """
        return self._manager


class Executive(Employee):
    def __init__(self, name: str, salary: float, bonus: float) -> None:
        super().__init__(name, salary)
        self._bonus = bonus

    def wage(self) -> float:
        """
        Calculate the wage include bonus.
        Returns:
            float: the pro-rated fortnightly amount of the annual bonus.

        """
        base = super().wage()
        return base + self._bonus / 26
