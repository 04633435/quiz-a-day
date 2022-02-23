class Solution:
    def pancake_sort(self, arr):
        ans = []
        for i in range(len(arr), 1, -1):
            index = 0
            for j in range(i):
                if arr[j] > arr[index]:
                    index = j

            if index == i - 1:
                continue
            for idx in range((index + 1) // 2):
                arr[idx], arr[index-idx] = arr[index-idx], arr[idx]
            # print(arr)
            for idx in range(i // 2):
                arr[idx], arr[i-1-idx] = arr[i-1-idx], arr[idx]
            ans.append(index+1)
            ans.append(i)
        return ans           

    def pancake_sort_2(self, arr):
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n - 1:
                continue
            m = index
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]  # 原地反转
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # 原地反转
            ans.append(index + 1)
            ans.append(n)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/pancake-sorting/solution/jian-bing-pai-xu-by-leetcode-solution-rzzu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    s = Solution()
    arr = [1,4,2,3]
    print(s.pancake_sort_2(arr))