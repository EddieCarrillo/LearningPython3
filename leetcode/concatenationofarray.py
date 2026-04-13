class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for idx in range(0, n):
            nums.append(nums[idx])
        return nums
