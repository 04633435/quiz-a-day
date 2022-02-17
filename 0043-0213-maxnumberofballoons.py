from collections import Counter


class Solution():
    def max_number_of_balloons(self, text):
        n_character = Counter(text)
        minimum = float("inf")
        for ch in "ban":
            if n_character[ch] == 0:
                return 0
            if n_character[ch] < minimum:
                minimum = n_character[ch]
        n_l = n_character['l']
        n_o = n_character['o']
        if n_l < 2 or n_o < 2:
            return 0
        return min(minimum, n_l // 2, n_o // 2)


if __name__ == '__main__':
    s = Solution()
    text = "balon"
    print(s.max_number_of_balloons(text))