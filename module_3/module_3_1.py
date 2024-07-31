calls = 0

def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    string = str(string)
    cort = (len(string), string.upper(), string.lower())
    return cort


def is_contains(string, list_):
    result = False
    count_calls()
    for i in range(len(list_)):
        if string.lower() == list_[i].lower():
            result = True
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

