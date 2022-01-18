from time import time


class Solution:
    def find_min_difference(self, timepoints):
        # Pigeonhole principle, time complexity O(C)
        # https://zh.wikipedia.org/wiki/%E9%B4%BF%E5%B7%A2%E5%8E%9F%E7%90%86
        if len(timepoints) > 1440 : return 0
        def convert(timestr):
            hour, min = timestr.split(":")
            return int(hour) * 60 + int(min)
        timepoints = list(map(convert, timepoints))
        timepoints = sorted(timepoints)
        ans = 1440
        for i in range (len(timepoints)):
            if i == 0:
                diff = timepoints[0] + 1440 - timepoints[-1]
            else:
                diff = timepoints[i] - timepoints[i-1]
            if ans > diff:
                ans = diff
        return ans


if __name__ == '__main__':
    s = Solution()
    timepoints = ["00:00","23:59"]
    print(s.find_min_difference(timepoints))