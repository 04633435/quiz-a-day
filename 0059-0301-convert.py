class Solution:
    # Solution-1 establish a 2-dimensional matrix
    def convert(self, s, numRows):
        n = len(s)
        if n <= numRows or numRows == 1:
            return s
        period = numRows + numRows - 2
        column = 1 + numRows - 2
        columns = (n // period + 1) * column
        mat = [[0] * columns for _ in range(numRows)]
        curr, curc = 0, 0
        for i in range(n):
            mat[curr][curc] = s[i]
            if i % period < numRows - 1:
                curr += 1
            else:
                curr -= 1
                curc += 1
        ret = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    ret.append(mat[i][j])

        return ''.join(ret)

    # Solution-2 build the anwser
    def convert_2(self, s, numRows):
        n = len(s)
        t = 2 * numRows - 2
        period = n // (2 * numRows - 2) + 1

        ret = []
        for i in range(numRows):
            for j in range(0, n, t):
                if j+i >= n:
                    continue
                ret.append(s[j+i])
                if 0 < i < numRows - 1 and j+t-i < n:
                    ret.append(s[j+t-i])
        return ''.join(ret)

if __name__ == '__main__':
    s = Solution()
    input_s = "PAYPALISHIRING"
    numRows = 4
    print(s.convert_2(input_s, numRows))