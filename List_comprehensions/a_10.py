nums = [x for x in range(1, 100) if x % 10 == 0]
new_nums = nums[:]
new_nums[3] = 0

# for i_elem in range(2, 8):
#     print(nums[i_elem], end=' ')
#
# print()
#
# for i_elem in range(2, 8):
#     print(new_nums[i_elem], end=' ')

print(new_nums[2:8 ])