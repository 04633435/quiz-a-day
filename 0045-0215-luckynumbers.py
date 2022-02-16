class Solution:
    def lucky_numbers(self, nums):
        m = len(nums)
        n = len(nums[0])
        min_row = [float('inf')] * m
        max_col = [0] * n
        for i in range(m):
            for j in range(n):
                if nums[i][j] < min_row[i]:
                    min_row[i] = nums[i][j]
                if nums[i][j] > max_col[j]:
                    max_col[j] = nums[i][j]

        # return min_row
        ret = []
        for i in range(m):
            for j in range(n):
                if max_col[j] == min_row[i]:
                    ret.append(max_col[j])
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(s.lucky_numbers(nums))