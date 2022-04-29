from termios import CQUIT


class Solution:
    def MinOperations(self, s):
        n = len(s)
        print(n)
        c1 = 0
        c2 = 0
        s1 = "AB"
        s2 = "BA"
        for i in range(0, n, 2):
            if i+1 >= n:
                break
            if s[i] != s1[0]:
                c1 += 1
            if s[i+1] != s1[1]:
                c1 += 1
            # elif s[i] != s1[0] and s[i+1] != s1[1]:
            #     c1 += 2
            if s[i] != s2[0]:
                c2 += 1
            if s[i+1] != s2[1]:
                c2 += 1
            # elif s[i] != s2[0] and s[i+1] != s2[1]:
            #     c2 += 2
        # print(c1, c2)
        if n % 2 == 0:
            return min(c1, c2)
        else:
            if s[-1] != s1[0]:
                c1 += 1
            if s[-1] != s2[0]:
                c2 += 1
            print(c1, c2)
            return min(c1, c2)
        
        # return ret if s[n-1] != s[n-2] else ret + 1



if __name__ == "__main__":
    s = Solution()
    s_input = "ABABABABBA"
    print(s.MinOperations(s_input))
