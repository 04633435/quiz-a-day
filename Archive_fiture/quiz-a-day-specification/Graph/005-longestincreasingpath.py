from functools import lru_cache


class Solution:
    DIRS = [[1, 0],[0, 1],[-1, 0],[0, -1]]
    # Solution-1 dfs + 记忆化搜索
    def longest_increasing_path(self, matrix):
        l_x, l_y = len(matrix), len(matrix[0])
        

        @lru_cache(None)
        def dfs(curx, cury):
            best = 1
            for dx, dy in Solution.DIRS:
                newx, newy = curx + dx, cury + dy
                if 0 <= newx < l_x and 0 <= newy < l_y and matrix[newx][newy] > matrix[curx][cury]:
                    best = max(best, dfs(newx, newy) + 1)
                # longest = max(longest, dir_longest)
            return best
        ret = 0
        for i in range(l_x):
            for j in range(l_y):
                ret = max(ret, dfs(i, j))

        return ret

    # Solution-2 Topological Sort
    


if __name__ == "__main__":
    s = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(s.longest_increasing_path(matrix))
        

