from curses.ascii import isdigit


"""Note:
try to use map() method to solve the problem that is iterable and the solutions for each element are the same
"""


class Solution:
    def count_valid_words(self, sentence):
        count = 0
        # for word in sentence.split(" "):
        def valid(word):
            if not word:
                return False
            hashyphens = False
            for i, ch in enumerate(word):
                if isdigit(ch) or ch in ",!." and i < len(word) - 1:
                    return False
                if ch == '-':
                    if hashyphens == True or i == 0 or i == len(word) - 1 or not word[i-1].islower() or not word[i+1].islower():
                        return False
                    hashyphens = True

            return True
        return sum(list(map(valid, sentence.split())))
        


if __name__ == '__main__':
    s = Solution()
    sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    print(s.count_valid_words(sentence))