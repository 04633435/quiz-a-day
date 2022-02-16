from collections import Counter


class Solution:
    # Solution-1 TC O(n^2)
    def count_k_difference(self, nums, k):
        n = len(nums)
        ret = 0
        for i in range(n-1):
            for j in range(i, n):
                if abs(nums[i] - nums[j]) == k:
                    ret += 1
        return ret

    
    # Solution-2 HashSet + Traverse Once
    def count_k_difference_2(self, nums, k):
        ret = 0
        counter = Counter()
        for num in nums:
            ret += counter[num+k] + counter[num-k]
            counter[num]
        return ret
