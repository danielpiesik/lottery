#!/usr/bin/env python3

from random import randint
from collections import Counter


def count_duplicates(items):
    return len([item for item in Counter(items).most_common() if item[1] > 1])


def generate(num=8, min=1, max=20, allowed_duplicates=2):
    assert allowed_duplicates > 0 or max - min >= num, 'infinity loop'

    numbers = []
    while len(numbers) < num:
        new_number = randint(min, max)
        if count_duplicates(numbers + [new_number]) <= allowed_duplicates:
            numbers.append(new_number)
    return sorted(numbers)


if __name__ == '__main__':
    print(generate())
