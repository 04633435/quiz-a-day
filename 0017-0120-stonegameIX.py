# tag: 博弈(Game)
class Solution:
    def stone_game_IX(self, stones):
        cn0 = cn1 = cn2 = 0
        for item in stones:
            if item % 3 == 0:
                cn0 += 1
            elif item % 3 == 1:
                cn1 += 1
            elif item % 3 == 2:
                cn2 += 1
        if cn0 % 2 == 0:
            return cn1 >= 1 and cn2 >= 1
        return cn1 - cn2 > 2 or cn2 - cn1 > 2
            

if __name__ == '__main__':
    s = Solution()
    stones = [2, 1]
    print(s.stone_game_IX(stones))