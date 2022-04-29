class Solution:
    def find_distant_indices(self, nums, key, k):
        key_indices = []
        for i in range(len(nums)):
            if nums[i] == key:
                key_indices.append(i)
        ret = []
        for i in range(len(nums)):
            for j in range(len(key_indices)):
                if abs(i - key_indices[j]) <= k:
                    ret.append(i)
                    break
        print(ret)


if __name__ == "__main__":
    s = Solution()
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1
    s.find_distant_indices(nums, key, k)