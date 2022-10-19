class TwoNumbers:

    def two_num(self,list_a, target):
        prev_array = {}
        for i,n in enumerate(list_a):
            rem_num = target - n
            if rem_num in prev_array:
                return [prev_array[rem_num],i]
            prev_array[n] = i
        return


t = TwoNumbers()
print(t.two_num([3,4,5,6,7],13))

