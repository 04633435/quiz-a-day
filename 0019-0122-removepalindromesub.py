class Solution:
    def remove_palindrome_sub(self, s):
        # how to determine the palindrome sub?
        # judge if the corresponding elements are identical
        return 1 if s == s[::-1] else 2


if __name__ == '__main__':
    s = Solution()
    input_str = "baabb"
    ret = s.remove_palindrome_sub(input_str)
    print(ret)