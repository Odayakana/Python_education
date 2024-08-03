data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    str_ = str(data).replace(':', ',')
    str_ = str_.translate({ord(i): None for i in '(){}[],\''})
    str_ = str_.split()
    total = 0
    for i in str_:
        try:
            total += int(i)
        except ValueError:
            total += len(i)

            # 'Urban2' - двойку в строке можно посчитать ниже, но решение будет 100 а не 99

            # for j in i:
            #     is_int = True
            #     try:
            #         total += int(j)
            #     except ValueError:
            #         total += 1

    return total


def calculate_structure_sum_v2(data):
    total = 0
    if type(data) == list:
        for i in data:
            total += calculate_structure_sum_v2(i)

    if type(data) == tuple:
        for i in data:
            total += calculate_structure_sum_v2(i)

    if type(data) == set:
        total += calculate_structure_sum_v2(list(data))

    if type(data) == dict:
        for key, value in data.items():
            total += calculate_structure_sum_v2(key) + calculate_structure_sum_v2(value)

    if type(data) == str:
        return len(data)

    if type(data) == int:
        return data

    return total


result = calculate_structure_sum(data_structure)
print(result)

result = calculate_structure_sum_v2(data_structure)
print(result)

