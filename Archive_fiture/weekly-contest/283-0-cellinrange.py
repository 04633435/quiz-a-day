class Solution:
    def cell_in_range(self, s):
        start, end = s.split(":")
        sr, sc = int(start[1]), start[0]
        er, ec = int(end[1]), end[0]
        ret = []
        for i in range(ord(sc), ord(ec) + 1):
            for j in range(sr, er+1):
                ret.append(f"{chr(i)}{j}")
        return ret

            
if __name__ == "__main__":
    s = Solution()
    input_s = "A1:F1"
    print(s.cell_in_range(input_s))