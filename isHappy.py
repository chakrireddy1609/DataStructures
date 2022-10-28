class Solution:

    def isHappy(self,num):
        visit = set()
        while num not in visit:
            visit.add(num)
            num = self.addSquares(num)
            if num == 1:
                return True
        return False

    def addSquares(self,num):
        output = 0
        while num:
            digit = num % 10
            digit = digit ** 2
            output += digit
            num = num // 10
        return output

s = Solution()
print(s.isHappy(191))

