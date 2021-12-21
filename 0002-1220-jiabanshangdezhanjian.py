# solution-1 solved by myself
class Solution(object):
    n_ships = 0
    def count_battle_ships(self, board):
        m = len(board)
        n = len(board[m-1])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    self.n_ships += 1
                    board[i][j] = '.'
                    self.search(board, i+1, j)
                    self.search(board, i, j+1)
                    self.search(board, i-1, j)
                    self.search(board, i, j-1)
        print(self.n_ships)
    

    def search(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == '.': return
        if board[i][j] == 'X':
            board[i][j] = '.'
            self.search(board, i+1, j)
            self.search(board, i, j+1)
            self.search(board, i-1, j)
            self.search(board, i, j-1)


# solution-2 dfs



if __name__ == '__main__':
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    s = Solution()
    s.count_battle_ships(board=board)