class Solution:
    def min_steps(self, s, t):
        s_char_count = [0] * 26
        t_char_count = [0] * 26
        for char in s:
            s_char_count[ord(char) - ord('a')] += 1
        for char in t:
            t_char_count[ord(char) - ord('a')] += 1
        ret = 0
        for i in range(26):
            if s_char_count[i] != t_char_count[i]:
                ret += abs(s_char_count[i] - t_char_count[i])
        
        return ret

if __name__ == '__main__':
    s = Solution()
    in_s = "night"
    t = "thing"
    print(s.min_steps(in_s, t))