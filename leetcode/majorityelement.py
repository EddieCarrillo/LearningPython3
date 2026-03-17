class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        maj_val = None
        maj_cnt = 0
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
            if map[num] > maj_cnt:
                maj_cnt = map[num]
                maj_val = num
        return maj_val

        
