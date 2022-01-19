class Solution:
    def contains_nearby_duplicate(self, nums, k):
        nums_table = {}
        for i in range(len(nums)):
            existed = nums_table.get(nums[i], None)
            if existed:
                nums_table[nums[i]].append(i)
            else:
                nums_table[nums[i]] = [i]
        for i in nums_table.keys():
            if len(nums_table[i]) <= 1:
                continue
            elif len(nums_table[i]) == 2:
                if abs(nums_table[i][0] - nums_table[i][1]) <= k:
                    return True
            else:
                for x in range(len(nums_table[i])):
                    for y in range(x+1, len(nums_table[i])):
                        if abs(nums_table[i][x] - nums_table[i][y]) <= k:
                            return True
        return False

    # 2. use dict maintain the max index of the present element. space efficiency
    def contains_nearby_duplicate_2(self, nums, k):
        nums_table = {}
        for i, num in enumerate(nums):
            if num in nums_table and abs(i - nums_table[num]) <= k:
                return True
            nums_table[num] = i
        return False

    # 3. slicing window
    def contains_nearby_duplicate_3(self, nums, k):
        s = set()
        for i, num in enumerate(nums):
            if i > k: 
                s.remove(nums[i-k-1])
            if num in s:
                return True
            s.add(num)
        return False

if __name__ == '__main__':
    s = Solution()
    nums, k = [99,99], 2
    print(s.contains_nearby_duplicate_3(nums, k))