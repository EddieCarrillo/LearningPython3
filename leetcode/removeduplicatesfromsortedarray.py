class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = 0
        review = 1
        for review in range(1, len(nums)):
            if nums[review] != nums[new]:
                new = new + 1
                nums[new] = nums[review]
        return new + 1
