"""Note:
    Problem: https://leetcode-cn.com/problems/coin-change-2/
    blog: https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247486586&idx=1&sn=da57c4d7d39bcbd2e16c2cc4e21b2361&chksm=fd9ca765caeb2e73c8fab98ada138d429e0fba35e8af83489cbb4c7a5b6e1e68c1ec341f1cd8&token=536156957&lang=zh_CN#rd
"""

class Solution:
    # Solution-1
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0] * (amount + 1) for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                add = dp[i][j-coins[i-1]] if j-coins[i-1] >= 0 else 0
                dp[i][j] = dp[i-1][j] + add

        return dp[-1][-1]

    # Solution-2 optimization
    def change_2(self, amount, coins):
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(len(dp)):
                add = dp[j-coins[i-1]] if j-coins[i-1] >= 0 else 0
                dp[j] = dp[j] + add
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    amount = 10
    coins = [10]
    print(s.change_2(amount, coins))
