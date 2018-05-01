def inversions(array):
    n = len(array)
    if n == 1:
        return [array, 0]
    [left, left_inv] = inversions(array[:n // 2])
    [right, right_inv] = inversions(array[n // 2:])
    ans = left_inv + right_inv
    i, j = 0, 0
    for k in range(n):
        if j == n - n // 2 or (i < n // 2 and left[i] <= right[j]):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
            ans += n // 2 - i
    return [array, ans]


def naive_inversions(array):
    ans = 0
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                ans += 1
    return ans


with open('array.txt', 'r') as f:
    arr = list(map(int, f.readlines()))
    arr1 = list(arr)

    a = inversions(arr)[1]
    print(a)
    b = naive_inversions(arr1)
    print(b)
    print(a - b)
