class Solution:
    # Solution-1 Enumeration O(n2)
    def sub_array_range(self, nums):
        n = len(nums)
        array_range = 0
        def dfs(r, max, min):
            nonlocal array_range
            if r == n:
                return
            if nums[r] > max:
                max = nums[r]
            elif nums[r] < min:
                min = nums[r]
            array_range += (max - min)
            dfs(r+1, max , min)            
        for i in range(n):
            dfs(i, nums[i], nums[i])
        return array_range
            
    # Solution-2 Monotone Stack O(n)
    def sub_array_range_2(self, nums) -> int:
        n = len(nums)
        minLeft, maxLeft = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            # 如果 nums[maxStack[-1]] == num, 那么根据定义，
            # nums[maxStack[-1]] 逻辑上小于 num，因为 maxStack[-1] < i
            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight, maxRight = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # 如果 nums[minStack[-1]] == num, 那么根据定义，
            # nums[minStack[-1]] 逻辑上大于 num，因为 minStack[-1] > i
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        sumMax, sumMin = 0, 0
        for i, num in enumerate(nums):
            sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * num
            sumMin += (minRight[i] - i) * (i - minLeft[i]) * num
        return sumMax - sumMin

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/sum-of-subarray-ranges/solution/zi-shu-zu-fan-wei-he-by-leetcode-solutio-lamr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.sub_array_range_2(nums))