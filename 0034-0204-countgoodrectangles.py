from curses.textpad import rectangle
from urllib.parse import MAX_CACHE_SIZE


class Solution:
    def count_good_rectangles(self, rectangles):
        maxlength = []
        for x, y in rectangles:
            if x < y:
                max_side_length = x
            else:
                max_side_length = y
            maxlength.append(max_side_length)
        max, ans = 0, 0
        for side_length in maxlength:
            if side_length > max:
                max = side_length
                ans = 1
            elif side_length == max:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    print(s.count_good_rectangles(rectangles))