"""
You are a given a uni-modal array of n distinct elements, meaning that its entries are in increasing order up until its
maximum element, after which its elements are in decreasing order. Give an algorithm to compute the maximum element
that runs in O(log n) time.
"""
import random


def largest(array):
    middle = len(array) // 2
    if array[middle - 1] < array[middle] and array[middle] > array[middle + 1]:
        return array[middle]
    else:
        if array[middle - 1] > array[middle]:
            return largest(array[:(middle+1)])
        else:
            return largest(array[(middle-1):])

correct = True
for _ in range(100000):
    a = [1]
    size = 5
    for i in range(size // random.randint(2, 5)):
        a.append(a[-1] + random.randint(1,size))
    for i in range(size - len(a)):
        a.append(a[-1] - random.randint(1, size))
    correct = correct and max(a) == largest(a)
print(correct)
