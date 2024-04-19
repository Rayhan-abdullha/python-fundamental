nums = [8,1,2,2,3]

"""
# brute force approach
ans = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j] and j != i:
            count += 1
    ans.append(count)
print(ans)

""" 

# hashtable effecient solution using hashmap
sort_nums = sorted(nums)
dic = {}
for i in range(len(nums)):
    if sort_nums[i] not in dic:
        dic[sort_nums[i]] = i   

ans = []
for val in nums:
    ans.append(dic[val])
print(ans)
