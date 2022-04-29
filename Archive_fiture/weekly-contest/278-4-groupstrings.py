"""Note
    1: disjoint-set data structure. 
      - find(). Recursive method to find the root of each set
      - union(). Union two set if the roots of the sets are the same
      - PS: initialize each set according to the quiz. e.g., in this quiz, the union sets are
        initialized with the size of the groups.
    2: Enumeration is a good method if the search space if not large.
"""


from collections import defaultdict

class Solution:
    def groupStrings(self, words):
        # 并查集模板（哈希表写法）
        fa, size = {}, defaultdict(int)
        groups, max_size = len(words), 0
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(x: int, y: int):
            nonlocal groups, max_size
            if y not in fa:
                return
            x, y = find(x), find(y)
            if x == y:
                return
            fa[x] = y
            size[y] += size[x]
            max_size = max(max_size, size[y])  # 维护答案
            groups -= 1

        for word in words:
            x = 0
            for ch in word:
                x |= 1 << (ord(ch) - ord('a'))  # 计算 word 的二进制表示
            fa[x] = x  # 添加至并查集
            size[x] += 1
            max_size = max(max_size, size[x])  # 维护答案
            if size[x] > 1:
                groups -= 1

        for x in fa:  # 枚举所有字符串（二进制表示）
            for i in range(26):
                merge(x, x ^ (1 << i))  # 添加或删除字符 i
                if (x >> i) & 1:
                    for j in range(26):
                        if ((x >> j) & 1) == 0:
                            merge(x, x ^ (1 << i) | (1 << j))  # 替换字符 i 为 j
        return [groups, max_size]

# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/groups-of-strings/solution/bing-cha-ji-wei-yun-suan-by-endlesscheng-uejd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':
    s = Solution()
    words = ["a","b","ab","cde"]
    print(s.groupStrings(words))