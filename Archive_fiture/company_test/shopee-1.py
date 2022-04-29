from matplotlib.style import available


class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row: int, columns: int, diagonals1: int, diagonals2: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    count += solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)
                return count

        return solve(0, 0, 0, 0)


    def buildhouse(self, n):
        def counts(r, c, d1, d2):
            if r == n:
                return 1
            else:
                count = 0
                housepositions = ((1 << n) -1) & (~(c | d1 | d2))
                while housepositions:
                    houseposition = housepositions & (-housepositions)
                    housepositions = housepositions & (housepositions - 1)
                    count += counts(r + 1, c | houseposition, (d1 | houseposition) << 1, (d2 | houseposition) >> 1)
                return count
        
        return counts(0, 0, 0, 0)
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/n-queens-ii/solution/nhuang-hou-ii-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。