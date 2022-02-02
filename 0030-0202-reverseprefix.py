class Solution:
    def reverse_prefix(self, word, ch):
        prefix_pos = -1
        for idx, element in enumerate(word):
            if element == ch:
                prefix_pos = idx
                break
        return word[:prefix_pos+1][::-1] + word[prefix_pos+1:]

if __name__ == '__main__':
    s = Solution()
    word, ch = 'abcdefg', 'd'
    print(s.reverse_prefix(word, ch))