class Solution:
    def maxScoreIndices(self, nums):
        n = len(nums)
        score_left = [0] * (n + 1)
        score_right = [0] * (n + 1)
        for index in range(1,n+1):
            if nums[index-1] == 0:
                score_left[index] = score_left[index-1] + 1
            else:
                score_left[index] = score_left[index-1]
        n_right = n - score_left[n-1]
        score_right[0] = n_right
        for index in range(1,n+1):
            if nums[index-1] == 1:
                score_right[index] = score_right[index-1] - 1
            else:
                score_right[index] = score_right[index-1]
        score = []
        for i in range(len(score_left)):
            score.append(score_left[i] + score_right[i])
        max_score = max(score)
        ret = []
        for i, score in enumerate(score):
            if score == max_score:
                ret.append(i)
        return ret