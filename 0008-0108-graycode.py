import math

class Solution:
    def gray_code(self, n):
        count = 1
        seq = [0]
        while count < math.pow(2,n):
            reversed_seq = seq[::-1]
            reversed_seq = [ele + count for ele in reversed_seq]
            seq = seq + reversed_seq
            count = count << 1
        return seq


if __name__ == '__main__':
    s = Solution()
    n = 2
    print(s.gray_code(n))