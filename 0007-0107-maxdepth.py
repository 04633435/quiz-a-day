class Solution:
    def max_depth(self, s):
        maxdepth = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count > maxdepth:
                    maxdepth = count
                count -= 1
        return maxdepth


if __name__ == '__main__':
    s = Solution()
    input_string = "(1+(2*3)+((8)/4))+1"
    print(s.max_depth(input_string))