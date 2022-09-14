def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("index find in: " ,index)
    else:
        print("index has not been found")

        

my_list = [1,2,3,4,5,6,7,8,9,10]

mock_search = linear_search(my_list, 8)
verify(mock_search)


