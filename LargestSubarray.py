class maxSubArray:

    def maxSum(self,list_a):
        maxSub = list_a[0]
        curSum = 0

        for i in list_a:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub,curSum)

        return maxSub

mx = maxSubArray()
print(mx.maxSum([-2,1,-3,4,-1,2,1,-5,11]))