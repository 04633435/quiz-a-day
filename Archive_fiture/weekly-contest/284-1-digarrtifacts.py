from collections import defaultdict


class Solution:
    def dig_artifacts(self, n, artifacts, dig):
        dig_dict = defaultdict(bool)
        for x, y in dig:
            if (x, y) in dig:
                continue
            else:
                dig_dict[(x, y)] = True
        ret = 0
        for r1, c1, r2, c2 in artifacts:
            if r1 == r2:
                if all([dig_dict[(r1, id)] for id in range(c1, c2+1)]):
                    ret += 1
            elif c1 == c2:
                if all([dig_dict[(id, c1)] for id in range(r1, r2+1)]):
                    ret += 1
            else:
                if all([dig_dict[(r1, c1)], dig_dict[(r1, c2)], dig_dict[(r2, c1)], dig_dict[(r2, c2)]]):
                    ret += 1

        return ret

    

    # Atteempt 2
    def dig_artifacts(self, n, artifacts, dig):
        fields = [[0] * n for _ in n]
        for x, y in dig:
            fields[x][y] = 1
        ret = 0
        def dig(x1, y1, x2, y2):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if fields[x][y] == 0:
                        return False

            return True
            
        for x1, y1, x2, y2 in artifacts:
            res = dig(x1, y1, x2, y2)
            if res:
                ret += 1


        return ret
        

            
                        


if __name__ == "__main__":
    s = Solution()
    n = 6
    artifacts = [[0,2,0,5],[0,1,1,1],[3,0,3,3],[4,4,4,4],[2,1,2,4]]
    dig = [[0,2],[0,3],[0,4],[2,0],[2,1],[2,2],[2,5],[3,0],[3,1],[3,3],[3,4],[4,0],[4,3],[4,5],[5,0],[5,1],[5,2],[5,4],[5,5]]

    print(s.dig_artifacts(n, artifacts, dig))
    

