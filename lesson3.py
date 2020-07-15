def append_sum(lst):
    for _ in range(3):
        lst.append(lst[-1] + lst[-2])
    return lst


print('Exercise: 1.1.1')
print(append_sum([1, 1, 2]))
print('-'*80)


def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]


print('Exercise: 1.1.2')
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
print('-'*80)


def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


print('Exercise: 1.1.3')
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
print('-'*80)


def append_size(lst):
    lst.append(len(lst))
    return lst

print('Exercise: 1.1.4')
print(append_size([23, 42, 108]))
print('-'*80)


def combine_sort(lst1, lst2):
    res_list = lst1 + lst2
    res_list.sort()
    return res_list


print('Exercise: 1.1.5')
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
print('-'*80)


def every_three_nums(start):
    if start > 100:
        return []
    else:
        return list(range(start, 101, 3))


print('Exercise: 1.2.1')
print(every_three_nums(91))
print('-'*80)


def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]


print('Exercise: 1.2.2')
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
print('-'*80)


def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2


print('Exercise: 1.2.3')
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
print('-'*80)


def double_index(lst, index):
    if (len(lst) - 1) < index:
        return lst
    else:
        lst[index] = lst[index] * 2
        return lst


print('Exercise: 1.2.4')
print(double_index([3, 8, -10, 12], 2))
print('-'*80)


def add_greetings(names):
    lst = []
    for name in names:
        lst.append('Hello, ' + name)
    return lst


print('Exercise: 2.1.1')
print(add_greetings(["Owen", "Max", "Sophie"]))
print('-'*80)


def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst


print('Exercise: 2.1.2')
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print('-'*80)


def odd_indices(lst):
    new_list = []
    for i in range(1, len(lst), 2):
        new_list.append(lst[i])
    return new_list


print('Exercise: 2.1.3')
print(odd_indices([4, 3, 7, 10, 11, -2]))
print('-'*80)


def exponents(bases, powers):
    new_list = []
    for i in bases:
        for j in powers:
            new_list.append(i**j)
    return new_list


print('Exercise: 2.1.4')
print(exponents([2, 3, 4], [1, 2, 3]))
print('-'*80)


def larger_sum(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2


print('Exercise: 2.1.5')
print(larger_sum([1, 9, 5], [2, 3, 7]))
print('-'*80)