from collections import deque

class Solution:
    def minumum_removal(self, beans):
        def recursion(q, sum_, n_non_zero, pre_count):

            minimum = q.popleft()

            count = sum_ - n_non_zero * minimum
            if count == 0:
                return pre_count
            else:
                sum_ -= minimum 
                return min(count + pre_count, recursion(q, sum_, n_non_zero-1, pre_count+minimum))
        
        sum_ = sum(beans)
        n_non_zero = 0
        for i in beans:
            if i != 0:
                n_non_zero += 1
        q = deque(sorted(beans))

        return recursion(q, sum_, n_non_zero, 0)


if __name__ == '__main__':
    s = Solution()
    beans = [4,1,6,5]

    print(s.minumum_removal(beans))
            