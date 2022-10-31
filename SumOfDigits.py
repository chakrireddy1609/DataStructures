class Solution:

    def sumOfDigits(self,num):
        sum = 0
        for i in range(1,10000):
            last_digit = num%10
            sum += last_digit
            num = num//10
        return sum


s = Solution()
print(s.sumOfDigits(999933339))

