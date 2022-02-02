"""Note
    1: string object does not support item assignment
"""


class Solution:
    def reverse_string(self, s):
        """
        Do not return anything, modify s in-place instead
        """

        l, r = 0, len(s) - 1
        while(l < r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


        

if __name__ == '__main__':
    s = Solution()
    # list(input_string) before feed it into reverse_string()
    input_string = 'abc'
    s.reverse_string(input_string)
    print(input_string)
