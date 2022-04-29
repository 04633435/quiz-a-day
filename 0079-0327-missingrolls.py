from math import floor


class Solution:
    def missing_rolls(self, rolls, mean, n):
        sum_rolls = sum(rolls)
        l = len(rolls)
        sum_all = mean * (l + n)
        diff = sum_all - sum_rolls
        if n > diff or  diff > n * 6:
            return []
        m = floor(diff / n)
        r = diff % n
        return [m] * (n-r) + [m+1] * r
        


if __name__ == "__main__":
    s = Solution()
    rolls = [3, 2, 4, 3]
    mean = 4
    n = 2
    print(s.missing_rolls(rolls, mean, n))