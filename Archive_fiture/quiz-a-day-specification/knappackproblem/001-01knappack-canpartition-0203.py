class Solution:
    def can_partition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)

        dp = [[0 for _ in range(int(target) + 1)] for _ in range(n)]

        # dp[0] = [nums[0] if j >= nums[0] else 0 for j in range(target+1)]

        for i in range(1, n):
            for j in range(len(dp[0])):
                no = dp[i-1][j]
                yes = dp[i-1][j-nums[i]] + nums[i] if j - nums[i] >= 0 else 0

                dp[i][j] = max(yes, no)

        return dp[n-1][target] == target


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,5,5,5,5]
    print(s.can_partition(nums))
