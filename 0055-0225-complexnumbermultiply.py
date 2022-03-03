class Solution:
    def complex_number_multiply(self, num1, num2):
        n1_splited = num1.split('+')
        r1, i1 = int(n1_splited[0]), int(n1_splited[1][:-1])
        n2_splited = num2.split('+')
        r2, i2 = int(n2_splited[0]), int(n2_splited[1][:-1])
        # r_new = int(r1) + int(r2)
        # i_new = int(i1) + int(i2)
        return f"{r1*r2-i1*i2}+{r1*i2+i1*r2}i"

if __name__ == '__main__':
    s = Solution()
    num1 = "1+1i"
    num2 = "1+1i"
    print(s.complex_number_multiply(num1, num2))