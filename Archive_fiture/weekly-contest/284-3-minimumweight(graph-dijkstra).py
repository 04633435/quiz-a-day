from collections import defaultdict
import heapq
from typing import *

class Solution:
    def minimum_weight(self, n, edges, src1, src2, dest):
        g, grev = defaultdict(list), defaultdict(list)
        for (f, t, w) in edges:
            g[f].append((t, w))
            grev[t].append((f, w))
        
        def dijkstra(graph: Dict[int, List[int]], start: int) -> List[int]:
            dist = [-1] * n
            dist[start] = 0
            used = set()
            q = [(0, start)]

            while q:
                u = heapq.heappop(q)[1]
                if u in used:
                    continue
                
                used.add(u)
                for (v, weight) in graph[u]:
                    target = dist[u] + weight
                    if dist[v] == -1 or target < dist[v]:
                        dist[v] = target
                        heapq.heappush(q, (dist[v], v))

            return dist
        
        dist1, dist2, dist3 = dijkstra(g, src1), dijkstra(g, src2), dijkstra(grev, dest)
        
        ans = -1
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1 and dist3[i] != -1:
                result = dist1[i] + dist2[i] + dist3[i]
                if ans == -1 or result < ans:
                    ans = result
        
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/minimum-weighted-subgraph-with-the-required-paths/solution/de-dao-yao-qiu-lu-jing-de-zui-xiao-dai-q-mj2c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    s = Solution()
    n = 6
    edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
    src1 = 0
    src2 = 1
    dest = 5
    print(s.minimum_weight(n, edges, src1, src2, dest))