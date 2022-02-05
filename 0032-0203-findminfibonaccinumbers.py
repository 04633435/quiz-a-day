class Solution:
    # Solution-1 dp(TLE)
    def find_min_fibonacci_numbers(self, k):
        f1, f2 = 1, 1
        fn = [f1, f2]
        while(fn[-1] + fn[-2] <= k):
            n = len(fn)
            fn.append(fn[n-1] + fn[n-2])
        dp = [[0 for _ in range(k+1)] for _ in range(len(fn))]

        dp[1] = [i for i in range(k+1)]

        for i in range(2, len(dp)):
            for j in range(1, len(dp[0])):
                if j - fn[i] >= 0:
                    comp_2 = dp[i][j-fn[i]] + 1
                else:
                    comp_2 = float('inf')
                comp_1 = dp[i-1][j]
                dp[i][j] = min(comp_1, comp_2)
        # print(dp)
        return(dp[-1][-1])


    # Solution-2 Greedy Algorithm
    def find_min_fibonacci_numbers_2(self, k):
        fn = [1, 1]
        while(fn[-1] + fn[-2] <= k):
            n = len(fn)
            fn.append(fn[n-1] + fn[n-2])
        ans, i = 0, len(fn) - 1
        while k:
            if k >= fn[i]:
                k -= fn[i]
                ans += 1
            i -= 1
        return ans
        


if __name__ == '__main__':
    s = Solution()
    k = 420000
    print(s.find_min_fibonacci_numbers_2(k))