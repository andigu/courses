from math import ceil
from random import randint

from divconquer.partition import partition


def find(array, i, l, r):
    """
    :return:0-based ith order statistic (i.e. if i=0, returns smallest element in array)
    """
    n = r - l + 1
    if n == 1:
        return array[l]
    medians = [sorted(array[j:j + 5])[int(min(r - j + 1, 5) / 2)] for j in range(l, r + 1, 5)]
    med = find(medians, ceil(n / 10), 0, ceil(n / 5) - 1)
    array, med_index = partition(array, array.index(med, l, r + 1), l, r, False)
    if med_index == i:
        return med
    elif med_index > i:
        return find(array, i, l, med_index - 1)
    else:
        return find(array, i, med_index + 1, r)


if __name__ == '__main__':
    size = 10
    correct = True
    for trial in range(10000):
        a = [randint(0, size * 10) for i in range(size)]
        correct = correct and sorted(a)[size // 2] == find(a, size // 2, 0, len(a) - 1)
        if trial % 50 == 0:
            print(trial, correct)
    print(correct)
