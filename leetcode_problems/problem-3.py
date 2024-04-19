names = ["Mary", "John", "Emma"]
heights = [180,165,170]
dic = {}
ans = []
for i in range(len(names)):
    dic[heights[i]] = names[i]

sorted_heights = sorted(heights, reverse=True)
print(sorted_heights)
for val in sorted_heights:
    ans.append(dic[val])

print(ans)