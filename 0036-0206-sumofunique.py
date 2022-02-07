from collections import Counter

class Solution:
    def sum_of_unique(self, nums):
        counter = Counter(nums)
        ret = 0
        for key in counter.keys():
            if counter[key] == 1:
                ret += key
        return ret