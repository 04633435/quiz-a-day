from collections import deque


class Solution:
    def is_bipartite(self, graph):
        n = len(graph)
        RED, GREEN = 1, 2

        color = [0] * n

        # for i in range(n):
        #     if color[i] == 0:
        #         color[i] = RED
        #         color_next = GREEN
        #     else:
        #         color_next = RED if color[i] == GREEN else GREEN
        #     q = deque(graph[i])
        #     while q:
        #         cur_node = q.popleft()
        #         if color[cur_node] == 0:
        #             color[cur_node] = color_next
        #             q.append(graph[cur_node])
        #         elif color_next != color[cur_node]:
        #             return False
        # return True


        for i in range(n):
            if color[i] == 0:
                color[i] = RED
                q = deque([i])
                while q:
                    node = q.popleft()
                    color_next = GREEN if color[node] == RED else RED
                    for j in graph[i]:
                        if color[j] == 0:
                            color[j] = color_next
                            q.append(j)
                        elif color[j] != color_next:
                            return False
        return True

