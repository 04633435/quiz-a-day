class Solution:
    def longestword(self, words):
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary/solution/ci-dian-zhong-zui-chang-de-dan-ci-by-lee-k5gj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。