def tenth_power(num=0):
    return pow(num, 10)


print('Exercise: 1.1.1')
print(tenth_power(0))
print(tenth_power(1))
print(tenth_power(2))
print('-'*80)


def first_three_multiples(num=0):
    print(num*1)
    print(num*2)
    print(num*3)
    return num * 3


print('Exercise: 1.2.1')
first_three_multiples(7)
print('-'*80)


def tip(total=0, precentage=0):
    return total*(precentage/100)


print('Exercise: 1.2.2')
print(tip(10, 25))
print(tip(0, 100))
print('-'*80)


def introduction(first_name='', last_name=''):
    return '{0}, {1} {0}'.format(last_name, first_name)


print('Exercise: 1.2.3')
print(introduction('James', 'Bond'))
print(introduction("Maya", "Angelou"))
print('-'*80)


def dog_years(name, age):
    return f'{name}, you are {age*7} year old in dog years'


print('Exercise: 1.2.4 ')
print(dog_years('Lola', 16))
print(dog_years('Baby', 0))
print('-'*80)


def large_power(base, exponent):
    return True if pow(base, exponent) > 5000 else False


print('Exercise: 2.1.1')
print(large_power(2, 13))
print(large_power(2, 12))
print('-'*80)


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < (food_bill + electricity_bill + internet_bill + rent):
        return True
    else:
        return False


print('Exercise: 2.1.2')
print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))
print('-'*80)


def twice_as_large(num1, num2):
    return True if num1 > num2*2 else False


print('Exercise: 2.1.3')
print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
print('-'*80)


def divisible_by_ten(num):
    return True if num % 10 == 0 else False


print('Exercise: 2.1.4')
print(divisible_by_ten(20))
print(divisible_by_ten(25))
print('-'*80)


def not_sum_to_ten(num1, num2):
    return True if num1 + num2 != 10 else False


print('Exercise: 2.1.5')
print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5, 5))
print('-'*80)


def in_range(num, lower, upper):
    # return True if lower <= num >= upper else False
    return lower <= num >= upper


print('Exercise: 2.2.1')
print(in_range(10, 10, 10))
print(in_range(5, 10, 20))
print('-'*80)


def same_name(your_name, my_name):
    return your_name == my_name


print('Exercise: 2.2.2')
print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))
print('-'*80)


def always_false(num):
    # return False
    if num >= 0:
        return False
    if num <= 0:
        return False
    else:
        return False


print('Exercise: 2.2.3')
print(always_false(0))
print(always_false(-1))
print(always_false(1))
print('-'*80)


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num2:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return 'It\'s a tie'


print('Exercise: 2.2.4')
print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))
print('-'*80)
