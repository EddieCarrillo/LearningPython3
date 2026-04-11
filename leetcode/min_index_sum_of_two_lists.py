from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = len(list1) + len(list2)
        map_1 = {}
        least_strings = []
        for i in range(0, len(list1)):
            map_1[list1[i]] = i
        for i in range(0, len(list2)):
            cur_str = list2[i]
            if cur_str in map_1:
                if map_1[cur_str] + i < min_index:
                    least_strings = []
                    least_strings.append(cur_str)
                    min_index = map_1[cur_str] + i
                elif map_1[cur_str] + i == min_index:
                    least_strings.append(cur_str)
        return least_strings
sol = Solution()
print(sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
print(sol.findRestaurant(["happy","sad","good"], ["sad","happy","good"]))
