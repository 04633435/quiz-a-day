import math


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