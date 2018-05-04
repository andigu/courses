# Goal is to find a the second largest number in an array with n + log_2(n) - 2 comparisons
# A linear scan will not work, because if the first element is the largest, the second largest will never be found
# without doing a reverse scan (making 2n comparisons)
import random
from math import log


def lt(a, b):
    """
    Returns if a is less than b. Used to maintain a global counter of number of comparisons made.
    """
    global comparisons
    comparisons += 1
    return a < b


def largest(array):
    """
    Returns an array containing the largest number of the array as its first element, and then the rest of the array
    contains every number with which this element has been compared. Since the second largest number must have been
    compared with the largest number at some point, it will be in this array. This function takes n-1 comparisons
    since it makes n/2 comparisons at its leaves, n/4 one level up, and so on until 1 comparison at the root (for a
    sum of n-1). The array contains log_2(n) since its size increases by 1 for each level of the recurrence tree.
    """
    n = len(array)
    if n == 1:
        return array
    left = largest(array[:n // 2])
    right = largest(array[n // 2:])
    if lt(left[0], right[0]):
        return right + [left[0]]
    else:
        return left + [right[0]]


correct = True
for _ in range(1000):
    a = []
    comparisons = 0
    size = 2 ** 8
    for i in range(size):
        generated = random.randint(0, size * 10)
        while generated in a:
            generated = random.randint(0, size * 10)
        a.append(generated)

    hist = largest(list(a))[1:]
    second = hist[0]
    for i in hist[1:]:
        if lt(second, i):
            second = i
    correct = correct and second == sorted(a)[-2] and comparisons == size + log(size, 2) - 2
print(correct)
