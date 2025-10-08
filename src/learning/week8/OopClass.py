"""
File: OopClass.py
Author: Shiqi(Kiki) Su
Date: 2025-09-25 13:57
Description: Encapsulation, Inheritance and Polymorphism
"""
class Animal():
    def __init__(self, name: str, age: int) -> None:
        self._name, self._age = name, age

    def info(self) -> str:
        animal_type = type(self).__name__.lower()
        return f"{self._name} the {animal_type} is {self._age} years old."

    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self) -> str:
        return 'Meow'

class Dog(Animal):
    def speak(self) -> str:
        return 'Bark'

class Fox(Animal):
    def __init__(self, name: str, age: int, nationality: str) -> None:
        super().__init__(name, age)
        self._nationality = nationality

    def speak(self):
        return 'Woof Woof'

    def info(self) -> str:
        return 'Fox is better than cat'


fox = Fox('Ketty', 2)
print(fox.speak())
print(fox.info())


