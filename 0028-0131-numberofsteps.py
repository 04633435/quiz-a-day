"""Note:
    1: division and subtraction from the perspective of binary mode
    2: the ways to calculate the number of '1' in a binary number, aka Hamming Problem
      - n & (n-1) 
      - 平行算法 (Parallel Algorithm)
"""

class Solution:
    # Solution-1 Simulation
    def number_of_steps(self, num):
        def next(num, steps):
            if num == 0:
                return steps
            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num -= 1
                steps += 1
            return next(num, steps)
        return next(num, 0)


    # Solution-2 binary calculation
    def numberOfSteps(self, num: int) -> int:
        def length(num: int) -> int:
            clz = 0
            if (num >> 16) == 0:
                clz += 16
                num <<= 16
            if (num >> 24) == 0:
                clz += 8
                num <<= 8
            if (num >> 28) == 0:
                clz += 4
                num <<= 4
            if (num >> 30) == 0:
                clz += 2
                num <<= 2
            if (num >> 31) == 0:
                clz += 1
            return 32 - clz
        def count(num: int) -> int:
            num = (num & 0x55555555) + ((num >> 1) & 0x55555555)
            num = (num & 0x33333333) + ((num >> 2) & 0x33333333)
            num = (num & 0x0F0F0F0F) + ((num >> 4) & 0x0F0F0F0F)
            num = (num & 0x00FF00FF) + ((num >> 8) & 0x00FF00FF)
            num = (num & 0x0000FFFF) + ((num >> 16) & 0x0000FFFF)
            return num
        return length(num) - 1 + count(num) if num else 0

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/solution/jiang-shu-zi-bian-cheng-0-de-cao-zuo-ci-ucaa4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    s = Solution()
    num = 8
    print(s.numberOfSteps(num))