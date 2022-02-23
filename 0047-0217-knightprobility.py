class Solution:
    total_prob = 0
    count = 0
    # Solution-1 dfs TLE
    def knight_probility(self, n, k, row, column):
        if k == 0:
            return 1
        
        def dfs(n, k_num, r, c, prob):
            if r < 0 or r >= n or c < 0 or c >= n:
                return
            if k_num == 0:
                self.total_prob += prob
                self.count += 1
                return
            for dr, dc in [[2, 1], [2, -1], [-2, 1], [-2, -1], \
                            [1, 2], [-1, 2], [1, -2], [-1, -2]]:
                curr, curc = r + dr, c + dc
                dfs(n, k_num - 1, curr, curc, prob * 1 / 8)
            
        dfs(n, k, row, column, 1)
        print(self.count)
        return self.total_prob
    
    # Solution-2 Memory Search

    # Solution-3 DP
    def knight_probility_3(self, n, k, row, column):
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
        for step in range(k+1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for dr, dc in [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]:
                            next_r, next_c = i + dr, j + dc
                            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n:
                                continue
                            dp[step][i][j] += dp[step-1][next_r][next_c] / 8
        return dp[k][row][column]



if __name__ == '__main__':
    s = Solution()
    n = 6
    k = 30
    row = 3
    column = 2
    print(s.knight_probility_3(n, k, row, column))