from sortedcontainers import SortedList
from heapq import *

class Solution:
    def busiest_server(self, k, arrival, load):

        cnts = [0] * k
        n, m = len(arrival), 0
        busy, free = [], SortedList(range(k))
        for i in range(n):
            start, end = arrival[i], arrival[i] + load[i]
            while busy and busy[0][0] <= start:
                free.add(busy[0][1])
                heappop(busy)
            if (idx := free.bisect_left(i % k)) == len(free) == (idx := free.bisect_left(0)):
                continue
            u = free[idx]
            free.remove(u)
            heappush(busy, (end, u))
            cnts[u] += 1
            m = max(m, cnts[u])
        return [i for i in range(k) if cnts[i] == m]

# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/solution/by-ac_oier-zgm6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    s = Solution()
    k = 3
    arrival = [1, 2, 3, 4, 5]
    load = [5,2,3,3,3] 
    s.busiest_server(k, arrival, load)
    a = "a"
    a.islower