"""
You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or
zero. You want to decide whether or not there is an index i such that A[i] = i. Design the fastest algorithm that you
can for solving this problem.
"""
import random


def solve(array, lower, upper):
    middle_index = (upper + lower) // 2
    middle = array[middle_index]
    if upper - lower <= 1 and middle != middle_index:
        return False
    elif middle == middle_index:
        return True
    elif middle < middle_index:
        return solve(array, middle_index + 1, upper)
    else:
        return solve(array, lower, middle_index)


correct = True
for trial in range(2, 1000):
    size = trial
    a = []
    for i in range(size):
        generated = random.randint(0, size * 10)
        while generated in a:
            generated = random.randint(0, size * 10)
        a.append(generated)
    a = sorted(a)
    correct = correct and any(i == a[i] for i in range(size)) == solve(a, 0, size)
print(correct)
