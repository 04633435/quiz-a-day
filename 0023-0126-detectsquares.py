"""Notes:
    python collections module. 
      - nametuple
      - deque
        Counter > return 0 if the key is not exsited.
        defaultDict > factory function to initialized dict object
      - ChainMap
        OrderedDict
      - UserList
      - UserDict
      - UserString
"""


from collections import defaultdict, Counter

class DetectSquares:
    def __init__(self):
        self.vertices = defaultdict(Counter)


    def add(self, point):
        x, y = point
        self.vertices[x][y] += 1



    def count(self, point):
        x, y = point

        if x not in self.vertices:
            return 0

        ret = 0

        x_count = self.vertices[x]

        for col, col_count in self.vertices.items():
            if col != x:
                d = x - col
                ret += x_count[y+d] * col_count[y] * col_count[y+d]
                ret += x_count[y-d] * col_count[y] * col_count[y-d]

        return ret

        

class DetectSquares1:

    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point) -> None:
        x, y = point
        self.map[y][x] += 1

    def count(self, point) -> int:
        res = 0
        x, y = point

        if not y in self.map:
            return 0
        yCnt = self.map[y]

        for col, colCnt in self.map.items():
            if col != y:
                # 根据对称性，这里可以不用取绝对值
                d = col - y
                res += colCnt[x] * yCnt[x + d] * colCnt[x + d]
                res += colCnt[x] * yCnt[x - d] * colCnt[x - d]
        
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/detect-squares/solution/jian-ce-zheng-fang-xing-by-leetcode-solu-vwzs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



if __name__ == "__main__":
    commands = ["DetectSquares", "add", "add", "add", "add", "count", "count", "add", "count"]
    points = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

    for command, point in zip(commands, points):
        if command == "DetectSquares":
            d_squares = DetectSquares1()
        elif command == "add":
            d_squares.add(point[0])
        else:
            print(d_squares.count(point[0]))
            