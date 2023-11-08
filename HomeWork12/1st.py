nums = [1, 2, 5]


def max_number(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
        return max_num


def min_number(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        min_num = nums[0]
        for num in nums:
            if num < min_num:
                min_num = num
        return min_num


def logger(func1, func2):
    def wrapper(nums):
        print(f"Function name is: {func1.__name__}")
        print(f"Function name is: {func2.__name__}")
        result = func1(nums), func2(nums)
        return result
    return wrapper


print(logger(max_number, min_number)(nums))
