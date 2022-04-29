def recursive(start, end, arr):
    if start >= end:
        return 
    pivot = arr[end]
    left, right = start, end - 1
    while left < right:
        while arr[left] < pivot and left < right:
            left += 1

        while arr[right] > pivot and right > left:
            right -= 1
        
        arr[left], arr[right] = arr[right], arr[left]




def quick_sort(nums):
    def sort(d_nums):
        n = len(d_nums)
        if n == 0:
            return []
        if n == 1:
            return d_nums
        arr_left, arr_right = [], []
        pivot = d_nums[0]
        for i in range(1, n):
            if d_nums[i] > pivot:
                arr_right.append(d_nums[i])
            else:
                arr_left.append(d_nums[i])
        left = sort(arr_left)
        right = sort(arr_right)
        return left + [pivot] + right
    return sort(nums)

if __name__ == '__main__':
    nums = [6, 5, 4, 3, 2, 1]
    print(quick_sort(nums))