class Solution():
    def optimal_division(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/({'/'.join(str(i) for i in nums[1:])})"

if __name__ == "__main__":
    s = Solution()
    nums = [1000,100,10,2]
    print(s.optimal_division(nums))