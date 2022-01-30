from collections import Counter

class Solution:
    def uncommon_from_sentences(self, s1, s2):
        s1_splited = s1.split()
        s2_splited = s2.split()
        s1_counter = Counter(s1_splited)
        s2_counter = Counter(s2_splited)
        ret = []
        for word in s1_splited:
            if s1_counter[word] == 1 and word not in s2_counter:
                ret.append(word)
        for word in s2_splited:
            if s2_counter[word] == 1 and word not in s1_counter:
                ret.append(word)
        return ret


if __name__ == '__main__':
    s = Solution()
    s1, s2 = 'this apple apple is sweet', 'this is sour'
    print(s.uncommon_from_sentences(s1, s2))