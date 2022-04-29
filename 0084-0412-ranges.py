from typing import *

class Solution:
    def ranges(self, range: List[List[int]], left, right):
        range.sorted(key=lambda x: [x[0], x[1]])
        for l, r in range: