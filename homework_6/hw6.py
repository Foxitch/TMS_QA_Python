from datetime import date


class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def person_name(self):
        return self.__name

    @person_name.setter
    def person_name(self, name: str):
        name.strip()
        if not name:
            raise SystemError('You did not enter the name')
        elif len(name) < 3:
            raise SystemError('Name should not be less than 3 symbols')
        else:
            self.__name = name

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age: int):
        if age == '':
            raise ValueError('Age cannot be empty')
        elif age <= 0:
            raise ValueError('Age cannot be negative or 0')
        else:
            self.__age = age

    @staticmethod
    def is_adult(age: int):
        if age > 17:
            return True
        else:
            return False

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        return cls(name, date.today().year - birth_year)

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}'

    def info(self):
        return self