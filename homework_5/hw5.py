# 1. Написать lambda функцию, определяющую четное/нечетное. Функция принимает параметр (число) и если четное, то выдает
# слово "четное", если нет - то "нечетное"

# 2. Дан список чисел. Вернуть список, где при помощи map() каждое число переведено в строку. В map() в качестве
# функции передавать lambda

# 3. При помощи функции filter() из кортежа слов отфильтровать только те, которые являются полиндромами

# 4. Написать декоратор к 2-м любым функциям, который считает время выполнения функций

# *5. Сделать функцию, которая на вход принимает строку. Анализирует ее методом .isdigit() и переводит строку в число.
# Функция должна распознавать отрицательные и дробные числа


import math
from time import time
from typing import Optional


""" 1.lambda функция """
print(
    list(
        map(lambda x: 'Even' if x % 2 == 0 else 'Odd', [1, 2, 3, 4, 5])
    )
)

print()

""" 2. map() """
number_list = [i for i in range(11)]
print(
    list(
        map(
            lambda x: str(x),
            number_list,
        )
    )
)

print()

""" 3. filter() """
words_list = ('маДам', 'Шабаш', 'лишил', 'ковер', 'луна', 'солнце')
print(
    list(
        filter(
            lambda x: x.lower() == x[::-1].lower(),
            words_list,
        )
    )
)

print()

"""4. Декораторы """


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = round(end_time - start_time, 5)
        print(f'The function {func.__name__} needs {total_time} seconds for complete')
        return result

    return wrapper


@decorator
def factorial(digit: int) -> int:
    result = 1
    for i in range(1, digit + 1):
        result *= i
    return result


@decorator
def factorial_math_module(digit: int) -> int:
    return math.factorial(digit)


print(factorial(10_000))
print()
print(factorial_math_module(10_000))

print()

""" 5. Из строки в число """


def from_str_to_digit(string: str):
    if string.isdigit():
        return f'You entered the positive integer digit: {int(string)}'

    if '.' in string:
        try:
            string = float(string)
            return f'You entered the fractional number: {string}'
        except ValueError:
            return f'You entered the wrong digit: {string}'
    else:
        try:
            string = int(string)
            return f'You entered the integer number: {string}'
        except ValueError:
            return f'You entered the wrong digit: {string}'


def main():
    lst = ['-6.7', '5', '5.4r', '-.777', '0', '-e', '33=', '.7.99', '', '6e', '8 ** 2']
    print(
        list(
            map(
                from_str_to_digit,
                lst,
            )
        )
    )


if __name__ == '__main__':
    main()
