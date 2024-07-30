def get_pass(value):
    result = ''
    for i in range(1, value):
        for j in range(i, value):

            if value % (i + j) == 0 and j != i:
                result += str(i) + str(j)

    return result


for i in range(3, 21):
    result_pass = get_pass(i)
    print(f'{i} - {result_pass}')
