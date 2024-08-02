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
        is_int = True
        try:
            int(i)
        except ValueError:
            is_int = False

        if is_int:
            total += int(i)
        else:
            total += len(i)

            # 'Urban2' - двойку в строке можно посчитать ниже, но решение будет 100 а не 99

            # for j in i:
            #     is_int = True
            #     try:
            #         int(j)
            #     except ValueError:
            #         is_int = False
            #
            #     if is_int:
            #         total += int(j)
            #     else:
            #         total += 1

    return total


result = calculate_structure_sum(data_structure)
print(result)
