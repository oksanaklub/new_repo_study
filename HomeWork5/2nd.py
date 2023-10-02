# second task
nums = [1, 2, 3, 4, 5, 68, 0]

for i in range(len(nums)-1):
    if nums[i] != nums[i - 1] + 1:
        print("Перше непослідовне число:", nums[i])
        break
else:
    print("Всі числа послідовні")
