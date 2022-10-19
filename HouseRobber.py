nums = [2,7,9,3,1]
rob0,rob1 = 0,0

for n in nums:
    temp = max(rob0+n,rob1)
    rob0 = rob1
    rob1 = temp
print(rob1)

