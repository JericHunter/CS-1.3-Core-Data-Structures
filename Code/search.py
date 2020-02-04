#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

        begin = 0
        end = len(array)- 1

        while begin <=  end:
            mid = begin + (end-begin) // 2
            mid_value = array[mid]

            if mid_value == item :
                return mid

            elif item < mid_value:
                # now check left side of the array
                end = mid - 1

            else:  # item greater than mid value
                # check right side of the array
                begin = mid + 1

        return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None:
        left = 0

    if right == None:
        right = len(array)-1

    if left > right:
        return None

    mid = (left + right) // 2

    if item < array[mid]:
        return binary_search_recursive(array, item, left, mid -1)
    elif item > array[mid]:
        return binary_search_recursive(array, item, mid +1, right)
    else:
        return mid

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
