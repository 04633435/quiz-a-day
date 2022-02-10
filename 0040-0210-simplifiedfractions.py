"""Note
    1: using gcd() return greatest common divisor 
    2: two ways to get greawtest common divisor
      1: 欧几里得法
      2: 更相减损法
"""


from math import gcd


class Solution:
    def simplified_fractions(self, n):
        ret = []
        for i in range(2, n+1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    ret.append(f"{j}/{i}")
        return ret


if __name__ == '__main__':
    s = Solution()
    n = 6
    print(s.simplified_fractions(n))