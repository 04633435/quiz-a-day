"""Note
    1: better way to count dialog and antidialog -> x - y and x + y
    2: time complexity of *in* operator in set/dict is: Average O(1), Worst O(n)
"""


from typing import List
from collections import deque, Counter


# Solution-1 TLE Time Complexity O(l*q)
class Solution:
    def grid_illumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def determine(lamp, q_position):
            lamp_x, lamp_y = lamp
            qx, qy = q_position
            if lamp_x == qx or lamp_y == qy or abs(lamp_x - qx) == abs(lamp_y - qy):
                return 1
            else:
                return 0
        def turn_off(lamps, query):
            x, y = query
            new_q = []
            for lamp_x, lamp_y in lamps:
                if not (x-1 <= lamp_x <= x+1 and y-1 <= lamp_y <= y+1):
                    new_q.append([lamp_x, lamp_y])
            return new_q

        ret = []
        q = deque(lamps)
        while len(queries):
            curq = queries.pop(0)
            light = 0
            for lamp in lamps:
                light |= determine(lamp, curq)
            ret.append(light)
            lamps = turn_off(lamps, curq)
        return ret


    def grid_illumination_2(self, n, lamps, queries):
        points = set()
        row, col, dialog, antidialog = Counter(), Counter(), Counter(), Counter()
        for r, c in lamps:
            if (r, c) in points:
                continue
            points.add((r, c))
            row[r] += 1
            col[c] += 1
            dialog[r-c] += 1
            antidialog[r+c] += 1
        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            if row[x] or col[y] or antidialog[x+y] or dialog[x-y]:
                ans[i] = 1
            for new_x in range(x-1, x+2):
                for new_y in range(y-1, y+2):
                    if (new_x, new_y) in points:
                        points.remove((new_x, new_y))
                        row[new_x] -= 1
                        col[new_y] -= 1
                        dialog[new_x-new_y] -= 1
                        antidialog[new_x+new_y] -= 1
        return ans


            
            


if __name__ == '__main__':
    s = Solution()
    n = 5
    lamps = [[0,0], [0,4]]
    queries = [[0,4],[0,1],[1,4]]
    print(s.grid_illumination_2(n, lamps, queries))
        