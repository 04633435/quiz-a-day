from collections import defaultdict
from collections import deque


class Solution:
    def can_finish(self, numCourses, prerequisites):
        n = numCourses
        g = [[] for _ in range(n)]
        indegree = [0] * n
        for course, pre_course in prerequisites:
            g[pre_course].append(course)
            indegree[course] += 1
        q = deque([id for id, indeg in enumerate(indegree) if indeg == 0])
        used = set()
        while q:
            cur = q.popleft()
            used.add(cur)
            for next in g[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)
        if any(indegree):
            return False
        else:
            return True

        

        


if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(s.can_finish(numCourses, prerequisites))