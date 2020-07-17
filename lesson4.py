def unique_english_letters(word):
    return len(set(word))


print('Exercise: 1.1.1')
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))
print('-'*80)


def count_char_x(word, x):
    return list(word).count(x)


print('Exercise: 1.1.2')
print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))
print('-'*80)


def count_multi_char_x(word, x):
    count = 0
    ret = 0
    while ret != -1:
        ret = word.find(x)
        if ret != -1:
            count += 1
            word = word[ret+1::]
    return count


print('Exercise: 1.1.3')
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))
print('-'*80)


def substring_between_letters(word, start, end):
    s1 = word.find(start)
    s2 = word.find(end)
    if s1 == -1 or s2 == -1:
        return word
    else:
        return word[s1+1:s2]


print('Exercise: 1.1.4')
print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))
print('-'*80)


def x_length_words(sentence, x):
    lst = sentence.split(' ')
    for i in lst:
        if len(i) < 2:
            return False
    return True


print('Exercise: 1.1.5')
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))
print('-'*80)


def check_for_name(sentence, name):
    #return bool(sentence.lower().count(name.lower()))
    return name.lower() in sentence.lower()


print('Exercise: 1.1.6')
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))
print('-'*80)


def sum_values(my_dictionary):
    dict_sum = 0
    for i in my_dictionary.values():
        dict_sum += i
    return dict_sum


print('Exercise: 2.1.1')
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
print(sum_values({10: 1, 100: 2, 1000: 3}))
print('-'*80)


def sum_even_keys(my_dictionary):
    even_sum = 0
    for key, value in my_dictionary.items():
        if key % 2 == 0:
            even_sum += value
    return even_sum


print('Exercise: 2.1.2')
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
print('-'*80)


def add_ten(my_dictionary):
    return {key: item+10 for key, item in my_dictionary.items()}


print('Exercise: 2.1.3')
print(add_ten({1: 5, 2: 2, 3: 3}))
print(add_ten({10: 1, 100: 2, 1000: 3}))
print('-'*80)


def values_that_are_keys(my_dictionary):
    lst = []
    for val in my_dictionary.values():
        for key in my_dictionary.keys():
            if val == key:
                lst.append(val)
                break
    return lst


print('Exercise: 2.1.4')
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
print('-'*80)


def max_key(my_dictionary):
    return max(my_dictionary, key=my_dictionary.get)


print('Exercise: 2.1.5')
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
print(max_key({"a": 100, "b": 10, "c": 1000}))
print('-'*80)
