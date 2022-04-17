
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


age = int(input('Введите возраст:'))
name = input('Введите имя:').capitalize().strip()

# Ян вышел из чата...
if len(name) < 4:
    a = 'Имя не может содержать менее 3-х символов'
elif age <= 0:
    a = 'Возраст не может быть отрицательным или равен 0'
elif 0 < age < 14:
    a = 'Минимальный возраст для входа в систему - 14 лет'
elif 16 <= age <= 17:
    a = f'Приветсвую вас, {name}. Ваш возраст {age}. Не забудьте получить Ваш первый паспорт'
elif 25 <= age <= 26:
    a = f'Приветсвую вас, {name}. Ваш возраст {age}. Не забудьте заменить паспорт'
elif 45 <= age <= 46:
    a = f'Приветсвую вас, {name}. Ваш возраст {age}. Пожалуйста, не забудьте обновить паспорт'
else:
    a = f'Приветствую вас, {name}. Ваш возраст {age}'

print(a)






