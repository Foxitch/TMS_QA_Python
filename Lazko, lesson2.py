
# 1
digit_1, digit_2, digit_3 = 1, 1, 1

# 2
list_1 = ['a']
list_2 = ['a']

# 3
digit_2 = float(digit_2)
digit_3 = str(digit_3)

list_1 = list_2 = tuple(list_1)

print(id(digit_1) != id(digit_2) != id(digit_3))

print(id(list_1) == id(list_2))