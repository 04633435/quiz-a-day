class Solution:
    def maximum_difference(self, nums):
        min_i = float("inf")
        max_diff = 0
        n = len(nums)
        for i in range(n):
            if nums[i] < min_i:
                min_i = nums[i]
                continue
            if nums[i] - min_i > max_diff:
                max_diff = nums[i] - min_i
        return max_diff if max_diff > 0 else -1

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,2,10]
    print(s.maximum_difference(nums))