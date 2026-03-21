from typing import List

print(len({'a':"1", 'b': "2"}))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Use two maps,
        # one for input array 1
        # second for input array 2
        # get the count for each type of element,
        # then, take the min count for each key type
        # then, write that many into a new array
        a_cnt = {}
        b_cnt = {}
        m = len(nums1)
        n = len(nums2)
        max_len = max(m, n)
        min_len = min(m, n)
        for idx in range(0, max_len):
            if idx < m:
                if nums1[idx] not in a_cnt:
                    a_cnt[nums1[idx]] = 0
                a_cnt[nums1[idx]] += 1
            if idx < n:
                if nums2[idx] not in b_cnt:
                    b_cnt[nums2[idx]] = 0
                b_cnt[nums2[idx]] += 1
        min_dict = a_cnt if len(a_cnt) < len(b_cnt) else b_cnt 
        intersect = []
        for v in min_dict:
            if v not in a_cnt or v not in b_cnt:
                continue
            min_cnt = min(a_cnt[v], b_cnt[v])
            for idx in range(0, min_cnt):
                intersect.append(v)
        return intersect
            
    
sol = Solution()
i1 = [[1,2,2,1], [2,2]]
print(sol.intersect(i1[0], i1[1]))

i2 = [[4,9,5], [9,4,9,8,4]]
print(sol.intersect(i2[0], i2[1]))

class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_cnt = {}
        intersect = []
        for num in nums1:
            if num not in num_cnt:
                num_cnt[num] = 0
            num_cnt[num] += 1
        for num in nums2:
            if num not in num_cnt:
                num_cnt[num] = 0
            if num_cnt[num] > 0:
                intersect.append(num)
                num_cnt[num] -= 1
        return intersect
