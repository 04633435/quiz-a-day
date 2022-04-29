from re import L


class Solution:
    def count_even(self, num):
        count = 0
        for number in range(1, num+1):
            if number < 10:
                if number % 2 == 0:
                    count += 1
            else:
                sum = 0
                while number:
                    bit = number % 10
                    number = number // 10
                    sum += bit
                if sum % 2 == 0:
                    count += 1

        return count

if __name__ == '__main__':
    s = Solution()
    num = 30
    print(s.count_even(num))