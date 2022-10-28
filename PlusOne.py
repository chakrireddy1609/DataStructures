class Solution:

    def plusOne(self,nums):
        nums = nums[::-1]
        count,i = 1,0

        while count:
            if i < len(nums):
                if nums[i] == 9:
                    nums[i] = 0

                else:
                    nums[i] += 1
                    count = 0
            else:
                nums.append(1)
                count = 0
            i+=1
        return nums[::-1]


s = Solution()
print(s.plusOne([1,2,9]))


