def bubblesort(list_a):

    indexing_length = len(list_a)-1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0,indexing_length):
            if list_a[i] > list_a[i+1]:
                is_sorted = False
                list_a[i],list_a[i+1] = list_a[i+1],list_a[i]
    return list_a


print(bubblesort([4,2,1,2,99,10103,2,4]))