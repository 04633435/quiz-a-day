"""Note
    1: ways to represent the present letters (occur only once or have equvalent value)
      - binary number
      - hashset
"""


class Solution:
    # Solution-1.1 Hashset to determine if it is a nice substring
    def longest_nice_substring_11(self, s):
        n = len(s)
        left = 0
        ret = []

        def process_char(char):
            if char.islower():
                cur_processed = char.upper()
            else:
                cur_processed = char.lower()
            return cur_processed

        while left < n - 1:
            char_set = set()
            if s[left].islower():
                if not s[left].upper() in s[left+1:]:
                    left += 1
                    break
            else:
                if not s[left].lower() in s[left+1:]:
                    left += 1
                    break
            char_set.add(s[left])
            
            right = left + 1

            while right < n:
                cur = s[right]
                cur_processed = process_char(cur)

                if cur in char_set:
                    right += 1
                elif cur_processed in char_set:
                    right += 1
                    char_set.add(cur)
                elif cur not in char_set and cur_processed in s[right+1:]:
                    char_set.add(cur)
                    right += 1
                elif cur not in char_set and cur_processed not in s[right+1:]:
                    
                    if len(char_set) % 2 != 0: # not nice subtring, move on
                        left = right + 1
                        break
                    else:
                        count = 0
                        for char in char_set:
                            char_processed = process_char(char)
                            
                            if char_processed not in char_set: # not nice subtring
                                left = right + 1 
                                break
                            count += 1
                        if count == len(char_set):
                            ret.append((left, right - left))
                            left = right + 1
                        break
        return ret

    # Solution-1.2 Use two hashset to determine if it is a nice substring
    def longest_nice_substring_12(self, s):
        n = len(s)
        max_pos = 0
        max_len = 0
        for i in range(n):
            set_all = set()
            set_upper = set()
            for j in range(i, n):
                set_all.add(s[j])
                set_upper.add(s[j].upper())
                if len(set_all) == len(set_upper) * 2 and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_pos = i
        return s[max_pos:max_pos + max_len]



    # Solution-2 枚举
    def longest_nice_substring_2(self, s):
        n = len(s)
        max_pos, max_len = 0, 0
        for i in range(n):
            lower, upper = 0,0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if upper == lower and j - i + 1 > max_len:
                    max_pos = i
                    max_len = j - i + 1
        return s[max_pos: max_pos + max_len]
                


if __name__ == '__main__':
    s = Solution()
    input_string = "YazaAay"
    print(s.longest_nice_substring_12(input_string))