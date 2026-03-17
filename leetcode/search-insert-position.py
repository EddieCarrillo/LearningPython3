class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        m: int = 0
        while l <= r:
            m = (l + (r - l) // 2) # Half way between the distance between l and r. For overflow reasons
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return m + 1 if target > nums[m] else m
