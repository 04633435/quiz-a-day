class Solution:
    def count_operations(self, num1, num2):
        if num1 == 0 and num2 == 0:
            return 0
        count = 0
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            count += 1
        return count + 1