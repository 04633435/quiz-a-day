import heapq


class Solution:
    def half_array(self, nums):
        sum_nums = sum(nums)
        target = sum_nums / 2
        # nums.sorted(revesre=True)
        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        pq = heapq.heapify(nums)
        count = 0
        while sum_nums > target:
            largest_num = heapq.heappop(nums)
            sum_nums += largest_num * 0.5
            heapq.heappush(nums, largest_num * 0.5)
            count += 1

        return count





        
