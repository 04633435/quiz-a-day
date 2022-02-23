from collections import Counter

class Solution:
    def number_of_good_subsets_leetcode(self, nums):
        """Problems gonna to solve:
            - how to determine the prime
            - how to traverse all of the subsets
        """
        # Solution-leetcode
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10**9 + 7

        freq = Counter(nums)
        f = [0] * (1 << len(primes))
        f[0] = pow(2, freq[1], mod)

        for i, occ in freq.items():
            if i == 1:
                continue
            
            # 检查 i 的每个质因数是否均不超过 1 个
            subset, x = 0, i
            check = True
            for j, prime in enumerate(primes):
                if x % (prime * prime) == 0:
                    check = False
                    break
                if x % prime == 0:
                    subset |= (1 << j)
            
            if not check:
                continue

            # 动态规划
            for mask in range((1 << len(primes)) - 1, 0, -1):
                if (mask & subset) == subset:
                    f[mask] = (f[mask] + f[mask ^ subset] * occ) % mod

        ans = sum(f[1:]) % mod
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/the-number-of-good-subsets/solution/hao-zi-ji-de-shu-mu-by-leetcode-solution-ky65/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,25,6,27,2,2]
    print(s.number_of_good_subsets_leetcode(nums))