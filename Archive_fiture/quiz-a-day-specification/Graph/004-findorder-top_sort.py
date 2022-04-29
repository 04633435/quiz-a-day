from collections import defaultdict, deque


class Solution:
    def findorder(self, numCourses, prerequisites):
        g = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indegrees[a] += 1
        q = deque(idx for idx, indegree in enumerate(indegrees) if indegree == 0)
        ret = []
        while q:
            pre_course = q.popleft()
            ret.append(pre_course)
            # next_course = g[pre_course]
            for next_course  in g[pre_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    q.append(next_course)

        if any(indegrees):
            return []
        else:
            return ret


if __name__ == "__main__":
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(s.findorder(numCourses, prerequisites))