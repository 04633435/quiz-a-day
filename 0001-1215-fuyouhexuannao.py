# solotion-1 written by myself
class Solution:
    def loud_and_rich(self, richer, quiet):
        # get the number of peopel
        n = len(quiet)
        # create a list of list for every vertex in the graph
        g = [[] for _ in range(n)]
        g_inversed = [[] for _ in range(n)]
        # traverse the 'richer' to create the edges
        for u, v in richer:
            g[u].append(v)
            g_inversed[v].append(u)
        # print(g)
        # calculate the indegree for each vertex
        indgee = [len(x) for x in g]
        
        ret = [-1] * n
        for person in range(n):
            self.recur(person, person, g_inversed, ret, quiet)
        return ret
    
    def recur(self, person, idx, graph_inversed, ret, quiet):
        if ret[person] == -1:
            ret[person] = person
        if len(graph_inversed[person]) == 0:
            return
        for richer_person in graph_inversed[person]:
            if ret[richer_person] != -1 and richer_person < idx:
                richer_person = ret[richer_person]
                if quiet[richer_person] < quiet[ret[idx]]:
                    ret[idx] = richer_person
                continue
            else:
                if quiet[richer_person] < quiet[ret[idx]]:
                    ret[idx] = richer_person
                self.recur(richer_person, idx, graph_inversed, ret, quiet)


# solution-2 dfs
# class Solution:
#     def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         n = len(quiet)
#         g = [[] for _ in range(n)]
#         for r in richer:
#             g[r[1]].append(r[0])

#         ans = [-1] * n
#         def dfs(x: int):
#             if ans[x] != -1:
#                 return
#             ans[x] = x
#             for y in g[x]:
#                 dfs(y)
#                 if quiet[ans[y]] < quiet[ans[x]]:
#                     ans[x] = ans[y]
#         for i in range(n):
#             dfs(i)
#         return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/loud-and-rich/solution/xuan-nao-he-fu-you-by-leetcode-solution-jnzm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# solution-3 topological sorting
# class Solution:
#     def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
#         n = len(quiet)
#         g = [[] for _ in range(n)]
#         inDeg = [0] * n
#         for r in richer:
#             g[r[0]].append(r[1])
#             inDeg[r[1]] += 1

#         ans = list(range(n))
#         q = deque(i for i, deg in enumerate(inDeg) if deg == 0)
#         while q:
#             x = q.popleft()
#             for y in g[x]:
#                 if quiet[ans[x]] < quiet[ans[y]]:
#                     ans[y] = ans[x]  # 更新 x 的邻居的答案
#                 inDeg[y] -= 1
#                 if inDeg[y] == 0:
#                     q.append(y)
#         return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/loud-and-rich/solution/xuan-nao-he-fu-you-by-leetcode-solution-jnzm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



if __name__ == '__main__':
    s = Solution()
    richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
    quiet = [3,2,5,4,6,1,7,0]
    print(s.loud_and_rich(richer, quiet))