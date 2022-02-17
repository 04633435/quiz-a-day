from collections import deque


class Solution:
    # Solution-1 
    def num_enclaves(self, grid):
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or vis[r][c]:
                return
            vis[r][c] = True
            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                dfs(x, y)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        return sum(grid[i][j] and not vis[i][j] for i in range(1, m - 1) for j in range(1, n - 1))

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/number-of-enclaves/solution/fei-di-de-shu-liang-by-leetcode-solution-nzs3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    count = 0
    def num_enclaves_2(self, grid):
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, visited, m, n):
            if (x, y) in visited or x >= m or x < 0 or y >= n or y < 0 or grid[x][y] == 0:
                return False
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and grid[x][y] == 1:
                return True
            visited.add((x, y))
            ret = False
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newx, newy = x + direction[0], y + direction[1]
                ret |= dfs(newx, newy, visited, m, n)
            return ret

        enclaves = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    enclaves.append((i, j))
        result = [False] * len(enclaves)
        for i in range(len(enclaves)):
            x = enclaves[i][0]
            y = enclaves[i][1]
            visited = set()
            result[i] = dfs(x, y, visited, m, n)

        return len(enclaves) - sum(result)
            

if __name__ == '__main__':
    s = Solution()
    grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
    print(s.num_enclaves_2(grid))