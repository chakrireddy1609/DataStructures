def sum_two(list_a,target):
    index_map = {}
    for index, value in enumerate(list_a):
        remaining_number = target - value
        if remaining_number in index_map:
            return [index_map[remaining_number], index]
        else:
            index_map[value] = index


print(sum_two([4,3,2,7,8,2,3,1,7],9))