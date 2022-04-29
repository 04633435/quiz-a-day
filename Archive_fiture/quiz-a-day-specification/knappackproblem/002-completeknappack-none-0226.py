"""
    link: https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247486107&idx=1&sn=e5fa523008fc5588737b7ed801caf4c3&chksm=fd9ca184caeb28926959c0987208a3932ed9c965267ed366b5b82a6fc16d42f1ff40c29db5f1&token=990510480&lang=zh_CN#rd
"""

class Solution():
    def complete_knappack(self, n, c, v, w):
        dp = [0] * (c + 1)

        for i in range(1, n+1):
            for j in range(c+1):
                comp = dp[j-w[i-1]] + v[i-1] if j-w[i-1] >= 0 else 0 
                dp[j] = max(dp[j], comp)
        return dp[c]

if __name__ == '__main__':
    s = Solution()
    n = 2
    c = 5
    v = [1, 2]
    w = [1, 2]
    print(s.complete_knappack(n, c, v, w))