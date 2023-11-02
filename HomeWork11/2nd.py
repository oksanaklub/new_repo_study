def min_number(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        min_num = nums[0]
        for num in nums:
            if num < min_num:
                min_num = num
        return min_num
