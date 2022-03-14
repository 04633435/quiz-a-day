import queue
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        ret = []
        def dfs(node):
            if node is None:
                return
            ret.append(node.val)
            for child in node.children:
                dfs(node)
        dfs(root)
        return ret           
        


if __name__ == "__main__":
    s = Solution()
    root = [1,None,3,2,4,None,5,6]
    print(s.preorder(root))
