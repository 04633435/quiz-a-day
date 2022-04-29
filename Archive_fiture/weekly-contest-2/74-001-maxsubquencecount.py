class Solution:
    def maximun_subquence_count(self, text, pattern):
        if pattern[0] == pattern[1]:
            a = 0
            for ch in text:
                if ch == pattern[0]:
                    a += 1
            return (a + 1) * a / 2

        else:
            ans, f, b = 0, 0, 0
            for ch in text:
                if ch == pattern[0]:
                    f += 1
                elif ch == pattern[1]:
                    b += 1
                    ans += f
            ans += max(f, b)
            return ans

if __name__ == "__main__":
    s = Solution()
    text = "abdcdbc"
    pattern = "ac"
    s.maximun_subquence_count(text, pattern=pattern)