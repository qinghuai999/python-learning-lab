"""
File: ClassUse.py
Author: Shiqi(Kiki) Su
Date: 2025-09-18 13:30
Description:
"""
from __future__ import annotations


class Person(object):
    def __init__(self, name: str, age: int, gender: str):
        """
        Construct a person object given their name, age and gender.
        Args:
            name (str): Person's name
            age (int): Person's age
            gender (str): Person's gender
        """
        self._name = name
        self._age = age
        self._gender = gender
        self._friend = None

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the object.

        Returns:
            str: A string containing the title, name and age.

        """
        if self._gender == 'M':
            title = 'Mr'
        elif self._gender == 'F':
            title = 'Miss'
        else:
            title = 'M'
        return title + ' ' + self._name + ' ' + str(self._age)

    def __repr__(self):
        return 'Person: ' + str(self)

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> str:
        return str(self._age)

    def get_gender(self) -> str:
        return self._gender

    def set_friend(self, friend: Person):
        self._friend = friend

    def get_friend(self):
        return self._friend

    def print_friend_info(person: Person) -> None:
        print(person.get_name())
        print(person.get_age())
        friend = person.get_friend()
        if friend is not None:
            print(f"Friends with {friend.get_name()}")

    def create_fry() -> Person:
        return Person("Fry", 25, "M")

    def make_friends(person1: Person, person2: Person) -> None:
        person1.set_friend(person2)
        person2.set_friend(person1)
