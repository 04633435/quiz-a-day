from collections import deque

class Solution:
    max = 0
    def get_maximum_gold(self, grid):
        m = len(grid)
        n = len(grid[0])
        start_points = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    start_points.append((i, j))
        def dfs(x, y, visited, gold):
            if (x < 0 or x >= m) or (y < 0 or y >= n):
                return
            if (x, y) in visited:
                return 
            if grid[x][y] == 0:
                return
            visited.add((x, y))
            gold += grid[x][y]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nextx, nexty = x + dx, y + dy
                dfs(nextx, nexty, visited, gold)
            if gold > self.max:
                self.max = gold
            visited.remove((x, y))
            gold -= grid[x][y]
        # global max
        # max = 0
        for x, y in start_points:
            visited = set()
            dfs(x, y, visited, 0)
        return self.max


        
        

if __name__ == '__main__':
    s = Solution()
    input = [[34,0,1,0,0,0],[0,0,2,0,1,0],[5,4,3,7,4,2],[0,0,5,0,1,4],[0,0,5,0,2,3]]
    print(s.get_maximum_gold(input))