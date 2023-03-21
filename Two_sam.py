target  = 12
nums = [2, 5, 3, 7, 3, 8]
result =[]
for i in nums:
    if target - i in nums :
        result.append(nums.index(target -i ))
        print(result)
