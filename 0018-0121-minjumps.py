
from collections import deque, defaultdict

class Solution:
    # dp
    def min_jumps(self, arr):
        jump_map = {}
        for index, ele in reversed(list(enumerate(arr))):
            if jump_map.get(ele, None):
                jump_map[ele].append(index)
            else:
                jump_map[ele] = [index]
        n = len(arr)
        dp = [0] * n

        for i in range(1, n):
            num = arr[i]
            jump = float('inf')
            if len(jump_map[num]) > 1 and jump_map[num][-1] != i:
                for previous_index in jump_map[num]:
                    if previous_index < i and dp[previous_index] < jump:
                        jump = dp[previous_index]

            next = float('inf')
            if i+1 < n:
                next_num = arr[i+1]
                index_lst = jump_map[next_num]
                if len(index_lst) > 1 and index_lst[-1] != i+1:
                    for previous_index in index_lst:
                        if previous_index < i and dp[previous_index] < next:
                            next = dp[previous_index]
                next += 1
            dp[i] = min(dp[i-1], jump, next) + 1
        return dp[n-1]

    
    # bfs
    def min_jumps_2(self, arr):
        idxSameValue = defaultdict(list)
        for i, a in enumerate(arr):
            idxSameValue[a].append(i)
        visitedIndex = set()
        q = deque()
        q.append([0, 0])
        visitedIndex.add(0)
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            v = arr[idx]
            step += 1
            for i in idxSameValue[v]:
                if i not in visitedIndex:
                    visitedIndex.add(i)
                    q.append([i, step])
            del idxSameValue[v]
            if idx + 1 < len(arr) and (idx + 1) not in visitedIndex:
                visitedIndex.add(idx + 1)
                q.append([idx+1, step])
            if idx - 1 >= 0 and (idx - 1) not in visitedIndex:
                visitedIndex.add(idx - 1)
                q.append([idx-1, step])

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/jump-game-iv/solution/tiao-yue-you-xi-iv-by-leetcode-solution-zsix/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    
if __name__ == '__main__':
    s = Solution()
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    print(s.min_jumps_2(arr))