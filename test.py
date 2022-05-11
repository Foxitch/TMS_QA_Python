# n = '-5'
# if n.isdigit():
#     print('111')
#
# print(float(n))
#
# a = '-.777'
# print(float(a))
#
# list_alpha = [chr(i) for i in range(97, 123)]
# print(list_alpha)


def test_func(string: str):
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


lst = ['-6.7', '5', '5.4r', '-.777', '0', '-e', '33=', '.7.99']
print(
    list(
        map(
            test_func,
            lst,
        )
    )
)







