class Solution:
    def has_alternating_bits(self, n):
        a = n ^ (n >> 1)
        return a & (a + 1)