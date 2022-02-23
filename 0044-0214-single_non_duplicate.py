from collections import Counter


class Solution:
    # Solution-1 O(n)
    def single_non_duplicate(self, nums):
        counter = Counter(nums)
        for i in counter.keys():
            if counter[i] == 1:
                return i

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    print(s.single_non_duplicate(nums))