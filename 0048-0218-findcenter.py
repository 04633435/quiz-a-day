from collections import Counter


class Solution:
    # Solution-1 O(n)
    def find_center(self, edges):
        c = {}
        for a, b in edges:
            if a not in c:
                c[a] = 1
            else:
                c[a] += 1
            if b not in c:
                c[b] = 1
            else:
                c[b] += 1
        for k, v in c.items():
            if v == len(edges):
                return k
    # Solution-2 O(1)
    def find_center(self, edges):
        a, b = edges[0]
        if a in edges[1]:
            return a
        else:
            return b

if __name__ == '__main__':
    s = Solution()
    edges = [[1,2],[2,3],[4,2]]
    print(s.find_center(edges))