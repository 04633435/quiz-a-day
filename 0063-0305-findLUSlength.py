class Solution:
    def find_LUS_length(self, a, b):
        return max(len(a), len(b)) if a != b else -1


if __name__ == "__main__":
    s = Solution()
    a = 'abc'
    b = 'cfg'
    print(s.find_LUS_length(a, b))