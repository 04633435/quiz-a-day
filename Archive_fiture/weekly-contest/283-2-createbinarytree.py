"""Note:
    1: Tree is a 简单连通无环图
    2: the concept of degree    
"""

from collections import Counter
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution():
    def create_binary_tree(self, description):
        v = {}
        deg = Counter()

        for p, c, l in description:
            if p not in v:
                v[p] = TreeNode()
            if c not in v:
                v[c] = TreeNode()
            if l == 1:
                v[p].left = v[c]
            else:
                v[p].right = v[c]
            deg[c] += 1
        for i in deg.values():
            if deg[i] == 0:
                head = i
        return v[head]
