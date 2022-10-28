class Solution:

#BUBBLE SORT
    def bubbleSort(self, list_a):
        is_Sorted = False

        while not is_Sorted:
            is_Sorted = True
            for i in range(len(list_a)-1):
                if list_a[i] > list_a[i+1]:
                    is_Sorted = False
                    list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
        return list_a

#Selection Sort
    def selectionSort(self, list_a):
        for i in range(len(list_a)-1):
            min_value = i

            for j in range(i+1, len(list_a)):
                if list_a[j] < list_a[min_value]:
                    min_value = j

            if min_value != i:
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

        return list_a

#Insertion Sort
    def insertionSort(self, list_a):

        for i in range(1, len(list_a)):

            if list_a[i-1] > list_a[i] and i > 0:
                list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
                i -= 1
        return list_a

#Quick Sort
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

#Merge Sort
    def merge(self,left,right):
        result = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        result += left[i:]
        result += right[j:]
        return result

    def mergeSort(self,list_a):
        if len(list_a) <= 1:
            return list_a
        else:
            mid = len(list_a)//2
            left = self.mergeSort(list_a[:mid])
            right = self.mergeSort(list_a[mid:])
            return self.merge(left, right)


s = Solution()
print(s.bubbleSort([3,1,2,6,5,7]))
print(s.selectionSort([3,1,2,6,5,7]))
print(s.insertionSort([3,1,2,6,5,7]))
print(s.quickSort([3,1,2,6,5,7]))
print(s.mergeSort([3,1,2,6,5,7]))