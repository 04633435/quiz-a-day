MOD = 1e9 + 7
class Solution:
    def count_vowel_permutation(self, n):
        # rules 
        # is it nessesary to create the permutation
        # or just count the number of the permutation?
        # ans: dp. no need to generate the permutation.
        # maintatn the number of the targerted permutation.
        dp = (1, 1, 1, 1, 1)
        for _ in range(2, n+1):
            dp = ((dp[1] + dp[2] + dp[4]) % MOD, (dp[0] + dp[2]) % MOD, (dp[1] + dp[3]) % MOD,
                    (dp[2] % MOD), (dp[2] + dp[3]) % MOD)
        return sum(dp) % 1000000007


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.count_vowel_permutation(n))