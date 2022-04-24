
# Запрашивает у пользователя имя и возраст;

# Проверяет минимальный возраст 14;
# Проверяет возраст на отрицательное число или 0;
# Проверяет, что возраст 16-17 лет и нужно не забыть получить первый паспорт;
# возраст 25-26 лет и нужно заменить паспорт;
# возраст 45-46 лет и нужно второй раз заменить паспорт;

# Проверяет имя на пустоту;
# Проверяет, что имя введено и минимальное количество символов в имени — 3;

# Выводит либо текст с ошибкой (по каждому условию разный текст ошибки), либо приветствие пользователя с его именем
# (с заглавной буквы), указанием возраста и советом получить/заменить паспорт (если совет актуален).
# Совет с паспортом выводить только в том случае, если отображается приветствие.

# Только один раз можно использовать print


"""
 Declaring and Initializing variables name, age
"""
name: str = input('Enter your name:').capitalize().strip()
age: int = int(input('Enter your age:'))

# Validate name and age. Initializing print message
if len(name) < 3:
    a = 'Name cannot be less than 3 symbols'
elif age <= 0:
    a = 'Age cannot be negative or 0'
elif 0 < age < 14:
    a = 'Min age to login is 14'
elif 16 <= age <= 17:
    a = f'Hello, {name}. Your age is {age}. Do not forget to get your first passport'
elif 25 <= age <= 26:
    a = f'Hello, {name}. Your age is {age}. Do not forget to change your passport'
elif 45 <= age <= 46:
    a = f'Hello, {name}. Your age is {age}. Do not forget to update your passport'
else:
    a = f'Hello, {name}. Your age is {age}'

print(a)
