def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1]
    print(bubble_sort(nums))