"""Note:
    1: list slice creates a new object

"""

class Solution:
    # Solution-1
    def sort_even_odd(self, nums):
        even = sorted(nums[::2])
        odd = sorted(nums[1::2], key=lambda x: -x)
        return [even[i // 2] if i % 2 == 0 else odd[i//2] for i in range(len(nums))]

    # Solution-2 
    def sort_even_odd_2(self, nums):
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], key=lambda x : -x)
        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [4, 1, 2, 3]
    print(s.sort_even_odd_2(nums))