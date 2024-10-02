
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def remove_chars(self, e_string, chars):
        for char in chars:
            e_string = e_string.replace(char, '')
        return e_string

    def get_all_words(self):
        all_words = {}
        char_list = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = self.remove_chars(line, char_list)
                    words += line.split(' ')
                    # print(words, end='')
            all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}

        for key, value in self.get_all_words().items():
            for i in range(len(value)):
                if value[i] == word:
                    result[key] = i + 1
                    return result

        return f'Слово "{word}" не найдено'


    def count(self, word):
        word = word.lower()
        result = {}

        for key, value in self.get_all_words().items():
            count = 0
            for i in range(len(value)):
                if value[i] == word:
                    count += 1
            if count:
                result[key] = count

        if result:
            return result
        else:
            return f'Слово "{word}" не найдено'

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))