from collections import deque

base, dirs = 131, ([1, 0], [0, 1], [0, -1], [-1, 0])
class Solution:
    def is_escape_possible(self, blocked, source, targert):
        block = {b[0] * base + b[1] for b in blocked}
        n = len(blocked)
        max_vis = n * (n - 1) // 2
        # bfs
        queue = deque()
        queue.append(source)
        def check(a, b):
            vis = {a[0] * base + a[1]}
            d = deque([a])
            while len(d) != 0 and len(vis) <= max_vis:
                curr = d.popleft()
                for dir in dirs:
                    nxt = [curr[0] + dir[0], curr[1] + dir[1]]
                    if nxt[0] >= int(1e6) or nxt[0] < 0 or nxt[1] >= int(1e6) or nxt[1] < 0:
                        continue
                    if nxt == b:
                        return True
                    hash_val = nxt[0] * base + nxt[1]
                    if hash_val in block or hash_val in vis:
                        continue
                    vis.add(hash_val)
                    d.append(nxt)
            return len(vis) > max_vis
        return check(source, target) and check(target, source)



# Solution two
# EDGE, MAX, BASE, DIR = int(1e6), int(1e5), 131, [(1, 0), (-1, 0), (0, 1), (0, -1)]
# class Solution:
#     def is_escape_possible(self, blocked, source, target):
#         block = {p[0] * BASE + p[1] for p in blocked}
#         n = len(blocked)
#         MAX = n * (n-1)//2 # 可直接使用 1e5
#         def check(a, b):
#             vis = {a[0] * BASE + a[1]}
#             d = deque([a])
#             while len(d) and len(vis) <= MAX:
#                 x, y = d.popleft()
#                 if x == b[0] and y == b[1]:
#                     return True
#                 for dx, dy in DIR:
#                     nx, ny = x + dx, y + dy
#                     if nx < 0 or nx >= EDGE or ny < 0 or ny >= EDGE:
#                         continue
#                     h = nx * BASE + ny
#                     if h in block or h in vis:
#                         continue
#                     d.append((nx, ny))
#                     vis.add(h)
#             return len(vis) > MAX
#         return check(source, target) and check(target, source)

# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/escape-a-large-maze/solution/gong-shui-san-xie-bfs-gei-ding-zhang-ai-8w63o/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
if __name__ == "__main__":
    s = Solution()
    blocked = [[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
    source = [655988,180910]
    target = [267728,840949]
    print(s.is_escape_possible(blocked, source, target))