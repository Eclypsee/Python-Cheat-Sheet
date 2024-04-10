
##############################################################################
print("##################################### Dataclass ################################")
# dataclasses contain a __init__ and __repr__ automatically
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    grades: list[float]

# Usage example
student = Student(name="Alice", age=20, grades=[88.0, 92.5, 79.0])
print(student)
# Output: Student(name='Alice', age=20, grades=[88.0, 92.5, 79.0])

##############################################################################
print("##################################### TypeAlias ################################")
# these aliases allow you to make code more readable
from typing import TypeAlias
feet: TypeAlias = int
altitude: TypeAlias = feet
class_grades: TypeAlias = list[float]
