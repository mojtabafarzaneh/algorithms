def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last) // 2


        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target :
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("the index find in: ", index)

    else:
        print("the index was not found!")


numbers= [1,2,3,4,5,6,7,8,9,10]

mock_search = binary_search(numbers, 8)
verify(mock_search)

mock_search = binary_search(numbers, 12)
verify(mock_search) 


