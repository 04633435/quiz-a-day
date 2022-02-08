class Solution:
    def longest_diverse_string(self, a, b, c):
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasnext = False
            for index, (n, ch) in enumerate(cnt):
                if n <= 0:
                    break
                if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                    continue
                hasnext = True
                ans.append(ch)
                cnt[index][0] -= 1
                break
            if not hasnext:
                return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    a, b, c = 3, 2, 3
    print(s.longest_diverse_string(a, b, c))
