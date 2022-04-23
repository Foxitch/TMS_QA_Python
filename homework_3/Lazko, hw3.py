# 0. Обязательно к прочтению Дзен python
# 1. Создать несколько функций на проверку введённых данных:
# - Проверка имени
# - Проверка возраста
# Функции должны возвращать строку с ошибкой. Если функции вернули ошибки, нужно вывести пользователю ошибки
# 2. Улучшить проверку имени: в имени допускается только 1 пробел
# 3. Сделать совет по получению или замене паспорта в отдельной функции,
# которая возвращает строку с советом или ничего не возвращает
# 4. Создать функцию main, в которой будут вызовы всех остальных функций, ввод данных и прочее
# 5. Создать цикл до тех пор, пока пользователь не введёт верные данные без ошибок
# 6. Создать функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки
# 7. Все функции должны иметь документацию (docstring) (вспоминаем второй урок) и аннотации
#
# И по классике — ограничения:
# Разрешается использовать только два раза print
# Нельзя использовать глобальные переменные


def validate_name(name: str) -> str:
    if not name:
        return 'You did not enter the name. '
    elif name.count(' ') > 1:
        return 'Name should not have more than one whitespace. '
    elif len(name) < 3:
        return 'Name should not be less than 3 symbols. '


def validate_age(age: int) -> str:
    if age == '':
        return 'Age cannot be empty. '
    elif age <= 0:
        return 'Age cannot be negative or 0. '
    elif age < 14:
        return 'Min age to login into the system is 14. '


def give_advice(age: int) -> str:
    if 16 <= age <= 17:
        return f'Do not forget to get your first passport. '
    elif 25 <= age <= 26:
        return f'Do not forget to change your passport. '
    elif 45 <= age <= 46:
        return f'Do not forget to update your passport. '


def main():
    name = ''
    age = 0
    is_validate_name: bool = False
    is_validate_age: bool = False

    while not is_validate_name or not is_validate_age:
        message: str = ''
        if not is_validate_name:
            name: str = input('Enter your name: ').title().strip()
        if not is_validate_age:
            age_str: str = input('Enter your age: ')
            age = int(age_str) if age_str != '' else age_str
        name_error_message = validate_name(name)
        age_error_message = validate_age(age)
        if not name_error_message:
            is_validate_name = True
        else:
            message += name_error_message
        if not age_error_message:
            is_validate_age = True
        else:
            message += age_error_message
        if message != '':
            print(message)

    advice = give_advice(age)
    if not advice:
        advice = ''
    print(f'Hello, {name}. Your age is {age}. ' + advice)


if __name__ == '__main__':
    main()
