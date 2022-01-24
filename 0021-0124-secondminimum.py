from collections import defaultdict, deque

class Solution:
    def second_minimum(self, n, edges, time, change):
        road_map = defaultdict(list)
        for x, y in edges:
            road_map[x].append(y)
            road_map[y].append(x)
        
        dist = [[float('inf')] * 2 for _ in range(n+1)]
        dist[1][0] = 0
        path = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            cur = path.popleft()
            for y in road_map[cur[0]]:
                step = cur[1] + 1
                if step < dist[y][0]:
                    # dist[y][1] = dist[y][0]
                    dist[y][0] = step
                    path.append((y, step))
                elif step > dist[y][0] and step < dist[y][1]:
                    dist[y][1] = step
                    path.append((y, step))
        
        ans = 0
        for _ in range(dist[n][1]):
            t_wait = 0 if 0 <= ans % (2 * change) < change else (2*change) - ans % (2 * change)
            ans += t_wait + time 
        return ans




if __name__ == '__main__':
    s = Solution()
    n, edges, time, change = 5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5
    print(s.second_minimum(n, edges, time, change))
