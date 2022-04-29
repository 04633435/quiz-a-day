from collections import Counter


class Solution:
    def count_max_or_subsets(self, nums):
        n = len(nums)
        d = Counter()
        max = 0
        for i in range(n):
            if nums[i] > max:
                max = nums[i]
            d[nums[i]] += 1
            inter = nums[i]
            for j in range(i+1, n):
                inter |= nums[j]
                if inter > max:
                    max = inter 
                d[inter] += 1
        return d[max]
        
if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 2]
    print(s.count_max_or_subsets(nums))