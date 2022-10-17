def selectionSort(list_a):

    indexing_length = len(list_a)-1
    for i in range(0,indexing_length):
        min_value = i

        for j in range(i+1,len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[i],list_a[min_value] = list_a[min_value],list_a[i]

    return list_a


print(selectionSort([4,2,1,2,99,10103,2,4]))
