class Solution:
    def add_digits(self, num):
        while num // 10 != 0:
            digits = []
            while num != 0:
                digits.append(num % 10)
                num = num // 10
            num  = sum(digits)
        return num


if __name__ == "__main__":
    s = Solution()
    num = 38
    print(s.add_digits(num))