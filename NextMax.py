class Solution:

    def newMax(self,nums):
        right_max = -1
        for i in range(len(nums)-1,-1,-1):
            newMax = max(right_max,nums[i])
            nums[i] = right_max
            right_max = newMax
        return nums

s = Solution()
print(s.newMax([18,3,4,8,6,7,1]))


