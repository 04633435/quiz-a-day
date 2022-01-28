"""Note:
    1: the keyword argument "key" of list.sort() and sorted() accept a function
    2: for the problem that needs to be sorted from two dimensions, we can sort it twice
      1: sort it according to one dimension
      2: for the identical element from the first dimension, sort it by the other dimension (ascending or descending according to the specific problem)

"""


class Solution:
    # solution-1
    def number_of_weak_characters1(self, properties) -> int:
        char_dict = {attc: deff for attc, deff in properties}
        keys = char_dict.keys()
        keys = sorted(keys)[::-1]
        print(keys)
        weak_char = set()
        for i in range(1, len(keys)):
            for j in range(i):
                if char_dict[keys[i]] < char_dict[keys[j]] and (keys[i], char_dict[keys[i]]) not in weak_char:
                    weak_char.add((keys[i], char_dict[keys[i]]))
        return len(weak_char)

    # solution-2
    def number_of_weak_characters2(self, properties):
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = properties[0][1]
        for attack, defense in properties:
            if defense < max_def:
                ans += 1
            else:
                max_def = defense
        return ans
        


if __name__ == "__main__":
    s = Solution()
    properties = [[5,5],[3,6],[3,3], [4,9]]
    print(s.number_of_weak_characters2(properties))