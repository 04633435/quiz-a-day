class Solution:
    def prefix_count(self, words, pref):
        if not words:
            return 0

        num_pref = len(pref)
        
        ret = 0
        for word in words:
            if word[:num_pref] == pref:
                ret += 1
        return ret

if __name__ == "__main__":
    s = Solution()
    words = ["leetcode","win","loops","success"]
    pref = "code"
    print(s.prefix_count(words, pref))