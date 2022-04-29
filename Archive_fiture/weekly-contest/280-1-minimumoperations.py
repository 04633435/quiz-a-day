from collections import Counter


class Solution:
    def minimum_operations(self, nums):
        n = len(nums)
        if n % 2 == 0:
            n_odd = n // 2
            n_even = n_odd
        else:
            n_odd = n // 2
            n_even = n_odd + 1 
        
        odd_counter = Counter(nums[1::2])
        even_counter = Counter(nums[::2])

        odd_most_list = odd_counter.most_common()
        even_most_list = even_counter.most_common()

        odd_most_num = odd_most_list[0][0]
        even_most_num = even_most_list[0][0]
        odd_most = odd_most_list[0][1]
        even_most = even_most_list[0][1]

        if odd_most_num != even_most_num:
            ret = n_odd - odd_most + n_even - even_most
        else:
            odd_sub = odd_most_list[1][1] if len(odd_most_list) > 1 else float('inf')
            even_sub = even_most_list[1][1] if len(even_most_list) > 1 else float('inf')
            cp1 = abs(n_odd - odd_most + n_even - even_sub)
            cp2 = abs(n_odd - odd_sub + n_even - even_most)
            ret = min(cp1, cp2)

        return ret if ret != float("inf") else n // 2


if __name__ == '__main__':
    s = Solution()
    nums = [2,2,2, 2, 2]
    print(s.minimum_operations(nums))



