"""Note:
    1: be careful of calculating the hash, '%' is prior to the += 
    2: pow() method is time-cosuming, if possible do it only one time instead.
    3: in case negative number, add modulo to the final remain
"""

class Solution:
    def subStrHash(self, s, power, modulo, k, hashValue) -> str:
        def s_val(ch):
            return ord(ch) - ord('a') + 1
        n = len(s)
        start_point = n - k
        hvalue = 0
        p = 1
        matches = []
        for i in reversed(list(range(start_point+1))):
            if i == start_point:
                for index_ch in range(i,i+k):
                    hvalue = (hvalue + ((ord(s[index_ch]) - ord('a') + 1) * p)) % modulo
                    if index_ch != i+k-1:
                        p = p * power % modulo
            else:
                add = ord(s[i]) - ord('a') + 1
                minus = s_val(s[i+k]) * pow(power, k-1) % modulo
                hvalue = (add + ((hvalue - minus + modulo) * power)) % modulo
            # hvalue = hvalue_non_module % modulo
            if hvalue == hashValue:
                matches.append(i)
        return s[matches[-1]: matches[-1] + k]


if __name__ == '__main__':
    s = Solution()
    print(s.subStrHash(s='xmmhdakfursinye', power=96, modulo=45, k=15, hashValue=21))
    
            