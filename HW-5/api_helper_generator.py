import random


def get_random_number(count, min_num, max_num):
    num = random.sample(range(min_num, max_num+1), count)
    for i in num:
        yield i


def get_random_tuple(count, count_el, length):
    res = []
    while count:
        count -= 1
        num = random.sample(range(1, length + 1), count_el)
        res = res.append(num)
    for i in res:
        yield i
