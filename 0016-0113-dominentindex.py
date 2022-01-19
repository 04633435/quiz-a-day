class Solution:
    def dominent_index(self, nums):
        n = len(nums)
        if n == 1: return 0
        a, b = -1, 0
        for i in range(1, n):
            if nums[i] > nums[b]:
                a, b = b, i
            elif a == -1 or nums[i] > nums[a]:
                a = i
        return b if nums[b] > nums[a] * 2 else -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4,  6, 13]
    print(s.dominent_index(nums))