class Solution:
    def smallest_number(self, num):
        if num > 0:
            flag = False
        else:
            flag = True
            num *= -1
        bits = []
        while num != 0:
            bit = num % 10
            num //= 10
            bits.append(bit)
        ret = 0
        bits.sort()
        if flag:
            ten = 1
            for i in bits:
                ret += i * ten
                ten *= 10
            ret *= -1
        else:
            ten = 1
            if 0 in bits:
                for i in range(len(bits)):
                    if bits[i] != 0 and bits[i-1] == 0:
                        zero_index = i
                bits = [bits[zero_index]] + bits[:zero_index] + bits[zero_index+1:]
                for i in bits[::-1]:
                    ret += i * ten
                    ten *= 10
            else:
                
                for i in bits[::-1]:
                    ret += i * ten
                    ten *= 10

        return ret


if __name__ == '__main__':
    s = Solution()
    num = -7605
    print(s.smallest_number(num))