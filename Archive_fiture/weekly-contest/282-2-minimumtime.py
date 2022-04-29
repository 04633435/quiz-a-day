"""Note:
    1. comsider bisection method when the search space is large.
"""

class Solution():
    # TLE
    def minimum_time(self, time, totaltrips):
        t = 0
        bus_trips = [0] * len(time)
        while True:
            # n_trips = 0
            if t == 0:
                t += 1
                continue
            for i in range(len(time)):
                if t % time[i] == 0:
                    bus_trips[i] = t // time[i]
            
            if sum(bus_trips) >= totaltrips:
                break

            t += 1

        return t
    
    # bisection 
    def minimum_time_leetcode(self, time, totalTrips):
        lo = 1
        hi = min(time) * totalTrips
        while lo <= hi:
            mid = (lo + hi) >> 1
            tot = sum(mid // t for t in time)
            if tot >= totalTrips:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/eU8bPl/view/rUilTq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    s = Solution()
    time = [5, 10, 10]
    totaltrips = 9
    print(s.minimum_time_leetcode(time, totaltrips))