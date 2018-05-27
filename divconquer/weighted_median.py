from random import randint

from divconquer.median import find
from divconquer.partition import partition


def right_weighted_median(array, l, r, W):
    n = r - l + 1
    if n == 1:
        return array[l]
    else:
        median = find(array[l:r + 1], n // 2, 0, n - 1)
        array, med_index = partition(array, array.index(median, l, r + 1), l, r, False)
        c_weights = sum(x[1] for x in array[:med_index])  # cumulative weights
        if c_weights < W / 2:
            return right_weighted_median(array, med_index, r, W)
        elif c_weights > W / 2:
            return right_weighted_median(array, l, max(med_index - 1, l), W)
        else:
            return array[med_index]


def weighted_median(array):
    """
    Weighted median refers to element in an array where the sum of all weights of all elements less than it is less
    than half the total weight, and the sum of all weights of all elements larger than it is also less than half
    the total weight. There are at most two weighted medians in an array.
    """
    n = len(array)
    W = sum(x[1] for x in array)
    right_med = right_weighted_median(array, 0, n - 1, W)
    array, ind = partition(array, array.index(right_med), 0, n - 1, False)
    if sum(x[1] for x in array[ind:]) <= W / 2:
        return max(array[:ind]), right_med
    return (), right_med


size = 10000
correct = True
for trial in range(10000):
    a = [(randint(0, 100), randint(1, 20), i) for i in range(size)]  # (value, weight, identifier)
    med1, med2 = weighted_median(a)
    std = sorted(a)
    weights = [x[1] for x in std]
    half_weight = sum(weights) / 2

    answers = []
    c_weight = 0
    for i in range(size - 1):
        c_weight += std[i][1]
        if c_weight <= half_weight and half_weight * 2 - c_weight - std[i + 1][1] <= half_weight:
            answers.append(std[i + 1])
    if len(answers) == 1:
        answers.insert(0, ())
    correct = correct and answers[0] == med1 and answers[1] == med2

    if trial % 50 == 0:
        print(trial, correct)
print(correct)
