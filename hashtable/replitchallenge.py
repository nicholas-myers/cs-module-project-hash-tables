def bigSorting(unsorted):
    # unsorted is a list of integers
    # the first part of the array is sorted
    print(unsorted)
    sorted_list = []
    while len(unsorted) > 0:
        lowest = int(unsorted[0])
        lowest_index = 0
        for index, num in enumerate(unsorted):
            if int(num) < lowest:
                lowest = int(num)
                lowest_index = index
        sorted_list.append(unsorted[lowest_index])
        unsorted.pop(lowest_index)
        print(unsorted)
    print(sorted_list)
    return sorted_list