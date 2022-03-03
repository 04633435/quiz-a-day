class Solution():
    # Solution-1 elimiating the rings 
    def maximum_requests(self, n, requests):
        in_ = [0] * n
        out_ = [0] * n
        for request in requests:
            in_[request[1]] += 1
            out_[request[0]] += 1
        print(0) 
    
    # Solution-2 binary enumeration
    def maximum_requests_2(self, n, requests):
        ret = 0
        for mask in range(1 << len(requests)):
            cnt = bin(mask).count("1")
            if cnt <= ret:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] -= 1
                    delta[y] += 1

            if all(x == 0 for x in delta):
                ret = cnt
        return ret


    def maximum_requests_leetcode(self, n, requests):
        ans = 0
        for mask in range(1 << len(requests)):
            cnt = bin(mask).count("1")
            if cnt <= ans:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/solution/zui-duo-ke-da-cheng-de-huan-lou-qing-qiu-ae0e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    s = Solution()
    n = 5
    requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    # requests = [[0, 1], [0, 1], [1, 2], [1, 3]]
    print(s.maximum_requests_2(n, requests))