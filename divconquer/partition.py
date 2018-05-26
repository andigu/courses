def partition(array, p, l, r, inplace=True):
    i = r  # index of left most element larger than pivot
    if not inplace:
        array = list(array)
    array[l], array[p] = array[p], array[l]
    for j in range(l + 1, r + 1):
        if array[j] < array[l] and i != r:
            array[j], array[i] = array[i], array[j]
            i += 1
        elif array[j] > array[l] and i == r:
            i = j
    pivot = i - 1 if array[i] > array[l] else i
    array[pivot], array[l] = array[l], array[pivot]
    return array, pivot
