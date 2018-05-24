from random import randint

from divconquer.partition import partition


def quicksort(A, l, r):
    n = r - l + 1
    if n == 2:
        if A[l] > A[r]:
            A[l], A[r] = A[r], A[l]
    elif n > 2:
        A, p = partition(A, randint(l, r), l, r)
        quicksort(A, l, max(p - 1, l))
        quicksort(A, min(p + 1, r), r)
    return A


correct = True
for _ in range(10000):
    a = [randint(0, 1000) for _ in range(randint(50, 1000))]
    correct = correct and quicksort(a, 0, len(a) - 1) == sorted(a)
print(correct)
