my_dict = {
    'Anton': 1987,
    'Lena': 1988,
    'Max': 1991,
}

my_dict_2 = {
    'New Oleg': 2006,
    'Old Oleg': 1986
}

print('Dict:', my_dict)
print('Dict data:', my_dict.get('Max', 'Данные отсутствуют'))
print('Dict data:', my_dict.get('Alex', 'Данные отсутствуют'))

my_dict.update(my_dict_2)
print('Dict:', my_dict)

oleg_data = my_dict.pop('Old Oleg')
print('Dict data:', oleg_data)
print('Dict:', my_dict)

my_set = {1, 2, True, 'Oleg', 'Not Oleg', 2, True, 'Oleg', 3, False}
print('Set: ', my_set)

more_elems = [5, 6]
# more_elems = {5, 6} - Работает
# more_elems = 5, 6 - тоже

my_set.update(more_elems)
print('Set: ', my_set)

my_set.discard('Oleg')
print('Set: ', my_set)
