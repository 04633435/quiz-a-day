class Solution:
    def lucky_numbers(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        min_row = [float('inf')] * m
        max_col = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < min_row[i]:
                    min_row[i] = matrix[i][j]
                if matrix[i][j] > max_col[j]:
                    max_col[j] = matrix[i][j]

        # return min_row
        ret = []
        for i in range(m):
            for j in range(n):
                if max_col[j] == min_row[i]:
                    ret.append(max_col[j])
        return ret


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(s.lucky_numbers(matrix))