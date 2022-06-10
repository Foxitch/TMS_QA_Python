class Validator:

    @staticmethod
    def validate_name(name: str) -> str | None:
        if not name:
            return 'You did not enter the name. '
        elif name.count(' ') > 1:
            return 'Name should not have more than one whitespace. '
        elif len(name) < 3:
            return 'Name should not be less than 3 symbols. '

    @staticmethod
    def validate_age(age: int) -> str | None:
        if age == '':
            return 'Age cannot be empty. '
        elif age <= 0:
            return 'Age cannot be negative or 0. '
        elif age < 14:
            return 'Min age to login into the system is 14. '

    @staticmethod
    def give_advice(age: int) -> str | None:
        if 16 <= age <= 17:
            return f'Do not forget to get your first passport. '
        elif 25 <= age <= 26:
            return f'Do not forget to change your passport. '
        elif 45 <= age <= 46:
            return f'Do not forget to update your passport. '

