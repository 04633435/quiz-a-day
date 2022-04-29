from collections import defaultdict
from email.policy import default

from prometheus_client import Counter


class Solution:
    def divide_arrays(self, nums):
        n = len(nums)
        if n % 2 != 0:
            return False
        hn = n // 2
        d = Counter(nums)
        return sum([i // 2 for i in d.values()]) == hn




if __name__ == "__main__":
    pass