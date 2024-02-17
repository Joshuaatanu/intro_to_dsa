def merge_sort(list):
    """
    Sorts a list in ascending order
    returns a new sorted list

    Divide: find the mid point of the list
    Conquer : recursively sort the sublist created in the previous step
    combine : Merge the sorted sublist created in the previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divides the unsorted list into sublist
    returns two sublist left and right
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

