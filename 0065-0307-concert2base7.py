class Solution:
    def convert_to_base7(self, num):
        if num == 0:
            return "0"
        neg = 0
        if num < 0:
            neg = 1
            num = -num
        convert = []
        while num != 0:
            digit = num % 7
            convert.append(str(digit))
            num = num // 7
        ret = ''.join(convert[::-1])
        return ret if not neg else '-' + ret


if __name__ == "__main__":
    s = Solution()
    num = 0
    print(s.convert_to_base7(num))


        