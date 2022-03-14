class Solution:
    def pose_order(self, root):
        ret = []
        def dfs(node):
            if node is None:
                return
            for child in node.children:
                dfs(child)
            
            ret.append(node.val)
        dfs(root)
        return ret