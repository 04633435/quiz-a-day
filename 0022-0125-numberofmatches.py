class Solution:
    def number_of_matches(self, n):
        def recursive(n_team, n_matching):
            if n_team % 2 == 0:
                n_matching += n_team // 2
                n_team = n_team / 2
            else:
                n_matching += (n_team - 1) // 2
                n_team = (n_team - 1) / 2 + 1
            if n_team == 1:
                return n_matching
            return recursive(n_team, n_matching)
        return recursive(n, 0)


if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.number_of_matches(10))
