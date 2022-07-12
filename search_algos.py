def binary_search(input_array, value):
    """Binary search function, uses an iterative approach.
    The function takes two inputs:
    a list to search through, and the value you're searching for.
    Assuming the list only has distinct elements,
    meaning there are no repeated values, and
    elements are in a strictly increasing order.
    Return the index of value, or -1 if the value
    doesn't exist in the list."""
    upper = len(input_array)-1
    lower = 0
    while upper >= lower:
        indx = (upper - lower)//2 + lower
        if input_array[indx] == value:
            return indx
        elif input_array[indx] > value:
            upper = indx -1
        else:
            lower = indx +1
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))