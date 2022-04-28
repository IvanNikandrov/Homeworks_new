def prime(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        return n == 2

    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def odd(n):
    return n % 2 != 0


def even(n):
    return n % 2 == 0


"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, type_filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if type_filter == ODD:
        return list(filter(odd, numbers))
    elif type_filter == EVEN:
        return list(filter(even, numbers))
    elif type_filter == PRIME:
        return list(filter(prime, numbers))

