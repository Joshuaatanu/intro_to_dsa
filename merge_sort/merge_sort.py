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


def merge(left, right):
    """
    Merges two lists(arrays), sorting them in the process
    Returns a new Merged list
    """

    l = []
    i = 0  # indexes in the left list
    j = 0  # indexes in the right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

alist=[54,26,93,17,77,31,44,55,20]
l =merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
