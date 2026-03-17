class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = 0
        for num in nums:
            if num != val:
                nums[new] = num
                new = new + 1
        return new
