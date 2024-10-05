import random
def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False
nums = [random.randint(1, 10) for _  in range(10)]
answer = []

for i_nums in range(0, len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer = answer[::-1]
        break

print('исходный список:', nums)
print('нужно чисел для палиндрома:', len(answer))
print('Список этих чисел:', answer)