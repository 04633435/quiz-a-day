class Solution:
    def is_onebit_character(self, bits):
        i, n = 0, len(bits)
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == n-1
            

if __name__ == "__main__":
    s = Solution()
    bits = [1, 0, 0]
    print(s.is_onebit_character(bits))