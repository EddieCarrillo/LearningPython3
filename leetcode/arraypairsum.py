class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(self.ssort(nums)[::2])

    def ssort(self, tosort: List[int]) -> List[int]:
        tosort.sort()
        return tosort

  class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

    class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = 0
        for i in range(0, len(nums), 2):
            pair_sum += nums[i]
        return pair_sum

    class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = 0
        for i in range(1, len(nums), 2):
            pair_sum += nums[i-1]
        return pair_sum

    class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sum = 0
        for i in range(1, len(nums), 2):
            pair_sum += min(nums[i-1], nums[i])
        return pair_sum
