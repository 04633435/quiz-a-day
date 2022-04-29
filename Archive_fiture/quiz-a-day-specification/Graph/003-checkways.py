from collections import defaultdict


class Solution:
    def check_ways(self, pairs):
        adj = defaultdict(list)
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)
        root = [key for key in adj.keys() if len(adj[key]) == (len(adj) - 1)]
        if len(root) == 0:
            return 0
        else:
            root = root[0]
        # thinking1: how to put the vertex at the correct position according to what?
        # thinking2: the conditions of ways == 0, ways == 1, ways == 2
        
        ans = 1
        for key, item in adj.items():
            if key == root:
                continue
            curdeg = len(item)
            parent = -1
            parentdeg = float('inf')
            # find the closest node whose degree is larger than crudeg
            for neibor in item:
                if curdeg <= len(adj[neibor]) < parentdeg:
                    parentdeg = len(adj[neibor])
                    parent = neibor
            
            if parent == -1 or any(neibor != parent and neibor not in adj[parent] for neibor in item):
                return 0

            if curdeg == parentdeg:
                ans = 2
            
        return ans
        



if __name__ == "__main__":
    s = Solution()
    pairs = [[1,2],[2,3]]
    print(s.check_ways(pairs))