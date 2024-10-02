
def  custom_write(file_name, strings):
    strings_positions = {}
    string_num = 1
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        position = file.tell()
        file.write(string + '\n')
        strings_positions[(string_num, position)] = string
        string_num += 1
    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
