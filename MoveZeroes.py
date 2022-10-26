nums = [1,4,0,4,2,0,9,2,0]
prev = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[prev],nums[i] = nums[i],nums[prev]
        prev += 1

print(nums)
