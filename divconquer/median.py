from math import ceil
from random import randint

from divconquer.partition import partition


def find(array, i, l, r):
    n = r - l + 1
    if n == 1:
        return array[l]
    medians = [sorted(array[j:j + 5])[int(min(r - j + 1, 5) / 2)] for j in range(l, r + 1, 5)]
    med = find(medians, ceil(n / 10), 0, ceil(n / 5) - 1)
    array, med_index = partition(array, array.index(med, l, r + 1), l, r)
    if med_index == i:
        return med
    elif med_index > i:
        return find(array, i, l, med_index - 1)
    else:
        return find(array, i, med_index + 1, r)


size = 10000
correct = True
for trial in range(10000):
    a = [randint(0, size * 10) for i in range(size)]
    correct = correct and sorted(a)[size // 2] == find(a, size // 2, 0, len(a) - 1)
    if trial % 50 == 0:
        print(trial, correct)
print(correct)
