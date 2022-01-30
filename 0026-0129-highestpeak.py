"""Note:
    1: Shallow list (fucking shallow list)
    2: the concept of bfs
"""


from collections import deque
import numpy as np

DIREACTION = [(0,1), (0,-1), (1,0), (-1, 0)]

class Solution:
    # Solution-1, start bfs at each water point, update the ret_matrix according to cur_matrix and ret_matrix
    def highest_peak(self, iswater):
        x_len = len(iswater)
        y_len = len(iswater[0])
        water_areas = []
        for index, x in np.ndenumerate(iswater):
            # print(index, x)
            if x == 1:
                water_areas.append(index)
        mat = [[0 for _ in range(y_len)] for _ in range(x_len)]
        for i in range(len(water_areas)):
            ret = [[0 for _ in range(y_len)] for _ in range(x_len)]
            q = deque([water_areas[i]])
            while q:
                cur_x, cur_y = q.popleft()
                cur_height = ret[cur_x][cur_y]
                for direction in DIREACTION:
                    dx, dy = direction
                    newx, newy = cur_x + dx, cur_y + dy
                    if 0 <= newx < x_len and 0 <= newy < y_len and (newx, newy) not in water_areas and ret[newx][newy] == 0:
                        if i == 0:
                            ret[newx][newy] = cur_height + 1
                            q.append((newx, newy))
                        else:
                            new_height = cur_height + 1
                            if new_height < mat[newx][newy]:
                                mat[newx][newy] = new_height
                                ret[newx][newy] = new_height
                                q.append((newx, newy))
            if i == 0:
                mat = ret
        return mat




if  __name__ == '__main__':
    s = Solution()
    # iswater is a 2-dimension matrix
    iswater = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,0,1],[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1]]
    print(s.highest_peak(iswater))