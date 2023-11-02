def max_number(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
        return max_num
