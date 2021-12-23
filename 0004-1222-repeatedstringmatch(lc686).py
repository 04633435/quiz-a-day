import math

# solution-1
class Solution:
    def repeated_string_match(self, a, b):
        n_a = len(a)
        n_b = len(b)
        for i in range(n_b):
            if b[i] not in a:
                return -1
        # Max length for repeated <a>
        times = math.ceil(n_b-1 / n_a)
        max_len = n_a + n_a * times

        ans = 0
        repeated_a = a
        while len(repeated_a) < max_len:
            if b in repeated_a:
                return ans
            else:
                repeated_a = repeated_a + a
                ans += 1
        return -1  


# solution-2 strHash
# instead of compare the char of a string, convert the string into a integer so that 
# the comparision can be done in O(1).
# Two things need to be kept in mind,
# 1. choose a big number of m, so that the possibility of coillision will be enough small to ignored
#    but not too big, because the overflow will slow down the comparision
# 2. choose the prime number for both m and p, but the reason behind them not figured out yet.
