from random import randint


def partition(A, p, l, r):
    i = r
    A[l], A[p] = A[p], A[l]
    for j in range(l + 1, r + 1):
        if A[j] < A[l] and i != r:
            A[j], A[i] = A[i], A[j]
            i += 1
        elif A[j] > A[l] and i == r:
            i = j
    pivot = i - 1 if A[i] > A[l] else i
    A[pivot], A[l] = A[l], A[pivot]
    return A, pivot


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
