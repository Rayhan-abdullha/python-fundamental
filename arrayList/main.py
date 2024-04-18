int_list = [1, 20, 3, 4, 5, 6]
# print(int_list[1:8])
# print(int_list[2]) # 2 number index data will be show
# print(int_list[:3]) # last 3 data will be show
# print(int_list[:2]) # first 2 data will be show


# method
max_val = max(int_list)
min_val = min(int_list)
sum_val = sum(int_list)
# print('max value = ', max_val)
# print('min value = ',min_val)
# print('sum = ', sum_val)

# calculate sum
# res_sum = 0
# for val in int_list:
#     res_sum += val
# print(res_sum)

# find max value
max_val = int_list[0]
for val in int_list:
    if max_val < val:
        max_val = val
print(max_val)