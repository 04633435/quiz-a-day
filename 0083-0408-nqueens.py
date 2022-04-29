from re import I


class Solution:
    # def n_queens(self, n):
    #     solutions = []  # a list of solved board
    #     # non-avalible position 
    #     c = set()
    #     d1 = set()
    #     d2 = set()
    #     ans = 0
    #     def build_one_row(row):
    #         if row == n:
    #             nonlocal ans
    #             ans += 1
    #         for col in range(n):
    #             if col in c or row - col in d1 or row + col in d2:
    #                 continue
    #             c.add(col)
    #             d1.add(row - col)
    #             d2.add(row + col)
    #             build_one_row(row + 1)
    #             c.remove(col)
    #             d1.remove(row - col)
    #             d2.remove(row + col)
    #     build_one_row(0)
    #     return ans
    
    # Solution-2 bit operations
    def n_queens(self, n):
        def build_one_row(row, c, d1, d2):
            if row == n:
                return 1
            else:
                count = 0
                availablePosition = (1 << n) - 1 & (~(c | d1 | d2))
                a = (~(c | d1 | d2))
                while availablePosition:
                    position = availablePosition & (-availablePosition)
                    availablePosition = availablePosition & (availablePosition - 1)
                    count += build_one_row(row+1, c | position, (d1 | position) << 1, (d2 | position) >> 1)
                return count
        return build_one_row(0, 0, 0, 0)


if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.n_queens(4))
        



            