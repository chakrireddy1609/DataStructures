class Solution:
    def Single(self,nums):
        res = 0
        for n in nums:
            res = res ^ n
        return res

s = Solution()
print(s.Single([2,2,1,1,4]))