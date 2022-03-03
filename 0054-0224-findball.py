class Solution:
    def find_ball(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = [i for i in range(n)]
        for i in range(m):
            for j in range(n):
                if ans[j] == -1:
                    continue
                pos = ans[j]

                if pos == 0 and grid[i][0] == -1:
                    ans[j] = -1
                elif pos == n-1 and grid[i][n-1] == 1:
                    ans[j] = -1
                elif grid[i][pos] == 1 and grid[i][pos+1] == -1:
                    ans[j] = -1
                elif grid[i][pos] == -1 and grid[i][pos-1] == 1:
                    ans[j] = -1
                else:
                    ans[j] = pos + 1 if grid[i][pos] == 1 else pos - 1
        return ans



if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    print(s.find_ball(grid))
