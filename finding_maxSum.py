nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curr = nums[0]
maxm = nums[0]

for i in range(1,len(nums)):
    curr = max(nums[i],curr + nums[i])
    maxm = max(maxm,curr)

print(maxm)
