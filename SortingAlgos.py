def quicksort(array):
    """Implementation of quick sort in Python.
    Input a list.
    Output a sorted list."""
    if len(array) > 1:
        pivot = len(array) - 1
        check = 0
        while check < pivot:
            if array[check] > array[pivot]:
                temp = array[check]
                array[check] = array[pivot - 1]
                array[pivot - 1] = array[pivot]
                array[pivot] = temp
                pivot -= 1
            else:
                check += 1
        array = quicksort(array[0:pivot]) + quicksort(array[pivot:])
    return array


def mergesort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2

    # recursive call for each side
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    # merged array index
    idx = 0
    # left and right array iterators
    right_idx = 0
    left_idx = 0

    while right_idx < len(right) and left_idx < len(left):
        if left[left_idx] <= right[right_idx]:
            array[idx] = left[left_idx]
            left_idx += 1
        else:
            array[idx] = right[right_idx]
            right_idx += 1
        idx += 1

    # All remaining values
    while left_idx < len(left):
        array[idx] = left[left_idx]
        left_idx += 1
        idx += 1

    while right_idx < len(right):
        array[idx] = right[right_idx]
        right_idx += 1
        idx += 1

    return array


def bubblesort(array):
    if len(array) < 2:
        return array
    for i in reversed(range(0, len(array) - 1)):
        for j in range(0, i + 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(mergesort(test))
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubblesort(test))
