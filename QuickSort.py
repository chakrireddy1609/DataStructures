def Quicksort(list_a):

    length = len(list_a)

    if length <=1:
        return list_a

    else:
        pivot = list_a.pop()
        greater = []
        lesser = []
        for i in list_a:
            if pivot < i:
                greater.append(i)
            else:
                lesser.append(i)

        return Quicksort(lesser) + [pivot] + Quicksort(greater)


print(Quicksort([4,3,5,111,11,2,3,5]))