from collections import defaultdict


class Solution:
    def find_restaurant(self, list1, list2):
        d = defaultdict(int)
        for index, restaurant in enumerate(list1):
            d[restaurant] += index

        min = float("inf")
        ret = []
        for index, restaurant in enumerate(list2):
            if restaurant in d:
                d[restaurant] += index
                if d[restaurant] < min:
                    min = d[restaurant]
                    ret = [restaurant]
                elif d[restaurant] == min:
                    ret.append(restaurant)
                
        return ret