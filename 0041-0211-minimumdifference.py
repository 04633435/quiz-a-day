class Solution:
    def minimum_difference(self, nums, k):
        if k == 1:
            return 0
        else:
            nums.sort()
            minimum = float("inf")
            for i in range(len(nums) - k + 1):
                minimum = min(minimum, nums[i+k-1]-nums[i])
        return minimum


if __name__ == '__main__':
    s = Solution()
    nums = [9,4,1,7]
    k = 2
    print(s.minimum_difference(nums, k))