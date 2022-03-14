from collections import defaultdict


class Solution:
    def count_highest_score_nodes(self, parents):
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        maxScore, cnt = 0, 0
        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        dfs(0)
        return cnt


if __name__ == "__main__":
    s = Solution()
    parents = [-1,2,0,2,0]
    print(s.count_highest_score_nodes(parents))