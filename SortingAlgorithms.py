class Solution:

    def bubbleSort(self, list_a):
        is_Sorted = False

        while not is_Sorted:
            is_Sorted = True
            for i in range(len(list_a)-1):
                if list_a[i] > list_a[i+1]:
                    is_Sorted = False
                    list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
        return list_a

    def selectionSort(self, list_a):
        for i in range(len(list_a)-1):
            min_value = i

            for j in range(i+1, len(list_a)):
                if list_a[j] < list_a[min_value]:
                    min_value = j

            if min_value != i:
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

        return list_a

    def insertionSort(self, list_a):

        for i in range(1, len(list_a)):

            if list_a[i-1] > list_a[i] and i > 0:
                list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
                i -= 1
        return list_a

    def quickSort(self, list_a):
        if len(list_a) <= 1:
            return list_a
        else:
            pivot = list_a.pop()
            items_greater = []
            items_lesser = []

        for item in list_a:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lesser.append(item)

        return self.quickSort(items_lesser) + [pivot] + self.quickSort(items_greater)


s = Solution()
print(s.bubbleSort([3,1,2,6,5,7]))
print(s.selectionSort([3,1,2,6,5,7]))
print(s.insertionSort([3,1,2,6,5,7]))
print(s.quickSort([3,1,2,6,5,7]))