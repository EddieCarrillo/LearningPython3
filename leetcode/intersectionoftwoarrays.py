from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1_str = "A"
        s2_str = "B"
        n = len(nums1)
        m = len(nums2)
        max_len = max(n, m)
        inter = {}
        for idx in range(0, max_len):
            #Scan both lists at once
            #Check if a particular key is present, 
            # if not, then, insert, 
            #if it does, and it's not already marked 
            # as being present from a particular array
            if idx < n:
                if nums1[idx] not in inter:
                    inter[nums1[idx]] = ""
                if "A" not in inter[nums1[idx]]:
                    inter[nums1[idx]] += "A"
            if idx < m:
                if nums2[idx] not in inter:
                    inter[nums2[idx]] = ""
                if "B" not in inter[nums2[idx]]:
                    inter[nums2[idx]] += "B"
                    
        intersect = []
        print(inter)
        for (k,v) in inter.items():
            if "A" in v and "B" in v:
                intersect.append(k)
        return intersect
    
sol = Solution()
i1 = [[1,2,2,1], [2,2]]
print(sol.intersection(i1[0], i1[1]))

i2 = [[4,9,5], [9,4,9,8,4]]
print(sol.intersection(i2[0], i2[1]))
