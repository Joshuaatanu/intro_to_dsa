def linear_search(list, target):
    """
    return the index of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None



def verify(index):
    if index is not None:
        print("target found at index :", index)
    else:
        print("target not found in list")

numbers =[1,2,3,4,5,6,7,8,9,10]

result= linear_search(numbers, 12)

verify(result)