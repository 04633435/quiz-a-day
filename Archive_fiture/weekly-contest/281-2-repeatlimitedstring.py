from collections import Counter, deque
import enum


class Solution:
    def repeat_limited_string(self, s, repeatlimit):
        # print(cnt)
        # while True:
        #     cnt.sort(key=lambda x: x[0])
        #     cnt = list(reversed(cnt))
        #     print(cnt)
        #     hasnext = False
        #     for index, (ch, n) in enumerate(cnt):
        #         if n <= 0:
        #             continue
        #         # continue condition
        #         if len(ans) >= repeatlimit and ans[-1] == ch:
        #             continue
        #         hasnext  = True
        #         if n < repeatlimit:
        #             for _ in range(n):
        #                 ans.append(ch)
        #             cnt[index][1] -= n
        #         else:
        #             for _ in range(repeatlimit):
        #                 ans.append(ch)
        #             cnt[index][1] -= repeatlimit
        #         break
        #     if not hasnext:
        #         return ''.join(ans)
        ans = ''
        cnt = list(Counter(s).items())
        cnt = [list(i) for i in cnt]    # the k, v is stored in a tuple
        cnt.sort(key=lambda x: x[0])
        cnt = list(reversed(cnt))

        for i in range(len(cnt)):
            while cnt[i][1]:
                if cnt[i][1] >= repeatlimit:
                    for j in range(len(cnt)):
                        flag = False
                        if ans[-1] == cnt[i][0]:
                            pass
                        if i != j and cnt[j][1] != 0:
                            cnt[j][1] -= 1
                            ans += cnt[i][0] * repeatlimit
                            ans += cnt[j][0]
                            cnt[i][1] -= repeatlimit
                            
                            flag = True
                            break
                    if not flag:
                        for k in range(len(cnt)):
                            if cnt[k][1] != 0:
                                if cnt[k][1] >= repeatlimit:
                                    ans += cnt[k][0] * repeatlimit
                                else:
                                    ans += cnt[k][0] * cnt[k][1]
                        break
                else:
                    ans += cnt[i][0] * cnt[i][1]
                    cnt[i][1] = 0
        return ans



# class Solution:
    def repeatLimitedString_leetcode(self, s: str, repeatLimit: int) -> str:
        ans = ""
        n = len(s)
        freq = [0] * 26 
        for ch in s:
            freq[ord(ch) - ord('a')] += 1 
        
        last, cnt = -1, 0 
        for i in range(n):
            flag = False 
            for j in range(25, -1, -1):
                if freq[j] > 0:
                    if last == j and cnt >= repeatLimit:
                        continue 
                    ans += chr(ord('a') + j)
                    if last == j:
                        cnt += 1 
                    else:
                        cnt = 1 
                    last = j 
                    freq[j] -= 1 
                    flag = True 
                    break 
                    
            if not flag:
                break
        return ans

# 作者：abnershen-t
# 链接：https://leetcode-cn.com/problems/construct-string-with-repeat-limit/solution/tan-xin-by-abnershen-t-qvz9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    s = Solution()
    string = "robnsdvpuxbapuqgopqvxdrchivlifeepy"
    repeatlimit = 2
    print(s.repeat_limited_string(string, repeatlimit))