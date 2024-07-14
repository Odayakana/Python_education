immutable_var = 1, True, 'string', 5.1
print('Immutable tuple: ', immutable_var)
# immutable_var[1] = False

mutable_list = [1, True, 'string', 5.1]
mutable_list[2] = ('apple', 2)
print('Mutable list: ', mutable_list)
print('Mutable list tuple element: ', mutable_list[2][0])
mutable_list.remove(mutable_list[2])
print('Mutable list: ', mutable_list)
mutable_list.insert(1, 'new_string')
mutable_list.append(False)
mutable_list.extend(['one more element'])
print('Mutable list: ', mutable_list)
