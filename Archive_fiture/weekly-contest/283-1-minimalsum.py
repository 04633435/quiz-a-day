class Solution:
    def minimal_sum(self, nums, k):
        n = len(nums)
        ret = 0
        nums.sort()
        if nums[0] - 1 > k:
            ret += ((1 + k) * k) / 2
            return int(ret)
        else:
            ret += ((1 + nums[0]-1) * (nums[0] - 1)) / 2
            k -= nums[0] - 1
        for i in range(0, n):
            s, e = nums[i], nums[i+1] if i+1 < n else None
            if e is None:
                break
            n_nums = e - s - 1
            if n_nums >= 1:
                if n_nums >= k:
                    ret += ((s+1 + s+k) * k) / 2
                    return int(ret)
                else:
                    ret += ((s+1 + e-1) * n_nums) / 2
                    k -= n_nums
        add_edd = nums[-1] + 1
        if k > 0:
            ret += ((add_edd + add_edd + k - 1) * k ) / 2

        return int(ret)


        # n = len(nums)
        # nums.sort()
        # count = 0
        # ret = 0
        # number = 1
        # idx = 0
        # while count < k:
        #     if idx < n:
        #         if number < nums[idx] and number not in nums:
        #             ret += number
        #             number += 1
        #             count += 1
        #         else:
        #             idx += 1
        #             number += 1  
        #     else:
        #         ret += number
        #         count += 1
        #         number += 1

        return ret


if __name__ == "__main__":
    s = Solution()
    # nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
    # k = 35
    nums = [1000000000]
    k = 1000000000
    print(s.minimal_sum(nums, k))