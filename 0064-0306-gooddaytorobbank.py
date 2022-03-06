class Solution:
    def goodday_to_rob_bank(self, security, time):
        n = len(security)
        if time == 0:
            return [i for i in range(n)]
        if n < 2 * time + 1:
            return []
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
            if security[n-1-i] <= security[n-i]:
                right[n-1-i] = right[n-i] + 1
        return [i for i in range(n) if left[i] >= time and right[i] >= time]


if __name__  == "__main__":
    s = Solution()
    security = [5,3,3,3,5,6,2]
    time = 2
    print(s.goodday_to_rob_bank(security, time))