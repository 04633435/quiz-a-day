class Solution:
    def can_partition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2

        
