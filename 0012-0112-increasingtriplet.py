import sys
import math

# the longest sequence for current node
class Solution:
    def increasing_triplet(self, nums):
        n = len(nums)
        longest_increasing_seq = [1] * n
        for i in range(1, len(nums)):
            max = -1
            for j in range(i):
                if nums[i] > nums[j]:
                    if longest_increasing_seq[j] > max:
                        max = longest_increasing_seq[j]
            if max != -1:
                longest_increasing_seq[i] = max + 1
        return any([item >= 3 for item in longest_increasing_seq])


    # the smallest node for current length of sequence
    def increasing_triplet_2(self, nums):
        n, ans = len(nums), 1
        f = [sys.maxsize] * (n+1)
        for i in range(n):
            t = nums[i]
            left, right = 1, i+1
            while(left < right):
                mid = (left + right) >> 1
                if f[mid] >= t: right = mid
                else: left = mid + 1
            f[right] = t
            ans = max(ans, right)
            if ans >= 3:
                return True
        return False

    # focus on the limited length, only need to update f[1], f[2]
    def increasing_triplet_3(self, nums):
        n, ans = len(nums), 1
        f = [math.inf] * 3
        for i in range(n):
            t = nums[i]
            if t > f[2]: return True
            elif f[1] < t < f[2]:
                f[2] = t
            elif f[1] > t:
                f[1] = t
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [2, 0, 6, 4, 5, 3]
    print(s.increasing_triplet_3(nums))