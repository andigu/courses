"""
You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its
neighbors. (A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four
neighbors; numbers on the side have three; the four corners have two.) Use the divide-and-conquer algorithm design
paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers.
"""
import random

from math import ceil, log


def lt(a, b):
    global counter
    counter += 1
    return a < b


def minimum(arr, n):
    smallest, index = arr[0], 0
    for i in range(1, n):
        if lt(arr[i], smallest):
            smallest, index = arr[i], i
    return smallest, index


def best_quadrant(a, n):
    """
    Finds the minimum element along the borders and middle axes of the array. From there, we roll downhill one element
    and the quadrant containing this element must contain at least one local minimum. If we imagine continuing
    to roll downhill from this element, we see that every element we visit from then on will be smaller than the
    boundary elements (since we rolled downhill starting from the minimum of all the boundary elements). Thus at some
    point we must find a local minimum since it is impossible to form a cycle (all distinct elements). This function
    returns the coordinates of the first element we find by rolling downhill.
    """
    top, top_index = minimum(a[0], n)
    left, left_index = minimum([r[0] for r in a], n)
    right, right_index = minimum([r[-1] for r in a], n)
    bottom, bottom_index = minimum(a[-1], n)
    mid_row, mid_row_index = minimum(a[n // 2], n)
    mid_col, mid_col_index = minimum([r[n // 2] for r in a], n)
    sted = sorted([top, left, right, bottom, mid_row, mid_col])
    if sted[0] == sted[1]:  # same minimum element appears twice means it is a minimum
        return [sted[0]]
    else:
        if top == sted[0]:
            return [1, top_index] if a[1][top_index] < top else [top]
        elif left == sted[0]:
            return [left_index, 1] if a[left_index][1] < left else [left]
        elif right == sted[0]:
            return [right_index, n - 2] if a[right_index][-2] < right else [right]
        elif bottom == sted[0]:
            return [n - 2, bottom_index] if a[-2][bottom_index] < bottom else [bottom]
        elif mid_row == sted[0]:
            return [n // 2 - 1, mid_row_index] if a[n // 2 - 1][mid_row_index] < mid_row else (
                [n // 2 + 1, mid_row_index] if a[n // 2 + 1][mid_row_index] < mid_row else [mid_row])
        else:
            return [mid_col_index, n // 2 - 1] if a[mid_col_index][n // 2 - 1] < mid_col else (
                [mid_col_index, n // 2 + 1] if a[mid_col_index][n // 2 + 1] < mid_col else [mid_col])


def solve(a):
    n = len(a)
    if n == 2:
        return min(min(a[0]), min(a[1]))
    q = best_quadrant(a, n)
    if len(q) == 1:
        return q[0]
    else:
        if q[0] < n // 2 and q[1] < n // 2:
            return solve([r[:n // 2] for r in a[:n // 2]])
        elif q[0] < n // 2 < q[1]:
            return solve([r[ceil(n / 2):] for r in a[:n // 2]])
        elif q[0] > n // 2 > q[1]:
            return solve([r[:n // 2] for r in a[ceil(n / 2):]])
        else:
            return solve([r[ceil(n / 2):] for r in a[ceil(n / 2):]])


correct = True
for _ in range(10000):
    size = random.randint(5, 50)
    counter = 0
    select = [i for i in range(size * size)]
    array = []
    for i in range(size):
        array.append([])
        for j in range(size):
            ind = random.randint(0, len(select) - 1)
            array[-1].append(select[ind])
            del select[ind]
    values = []
    for i in range(size):
        for j in range(size):
            if all([i == size - 1 or array[i + 1][j] > array[i][j], i == 0 or array[i - 1][j] > array[i][j],
                    j == size - 1 or array[i][j + 1] > array[i][j], j == 0 or array[i][j - 1] > array[i][j]]):
                values.append([i, j])

    ans = solve(array)
    correct = correct and any(ans == array[v[0]][v[1]] for v in values) and counter <= 12*size - 6 * log(size,2)

print(correct)
