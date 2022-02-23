class Solution:
    def reverse_only_letters(self, s):
        ch_lst = []
        for ch in s:
            ch_lst.append(ch)

        l, r = 0, len(ch_lst) - 1
        while l < r:
            if not ch_lst[l].isalpha():
                l += 1
                continue
            elif not ch_lst[r].isalpha():
                r -= 1
                continue
            ch_lst[l], ch_lst[r] = ch_lst[r], ch_lst[l]
            l += 1
            r -= 1
        print(ch_lst)
        return ''.join(ch_lst)

if __name__ == '__main__':
    s = Solution()
    input_s = "a-bC-dEf-ghIj"
    print(s.reverse_only_letters(input_s))