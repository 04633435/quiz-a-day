from math import ceil


class Solution:
    def maximum_top(self, nums, k):
        n = len(nums)
        if k % 2 == 1 and n == 1:
            return -1
        n_max, sec_max = -1, -1

        if k <= n:
            for i in range(k-1):
                if nums[i] > n_max:
                    sec_max = n_max
                    n_max = nums[i]
                elif nums[i] > sec_max:
                    sec_max = nums[i]

            if k < n and nums[k] > n_max:
                return nums[k]
            else:
                if nums[k-1] != n_max:
                    return n_max
                else:
                    return sec_max
    
        else:
            for i in range(n):
                if nums[i] > n_max:
                    n_max = nums[i]
            return n_max

if __name__ == "__main__":
    s = Solution()
    n = [5,5,4,4,5]

    k = 5
    print(s.maximum_top(n, k))


