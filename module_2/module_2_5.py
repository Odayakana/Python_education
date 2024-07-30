def get_matrix(n, m, value):
    matrix = []

    if n > 0 and m > 0:
        for i in range(n):
            l_list = []

            for j in range(m):
                l_list.append(value)

            matrix.append(l_list)

        return matrix

    else:
        return 'Error'


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(4, 0, 13)

print(result1)
print(result2)
print(result3)
print(result4)
