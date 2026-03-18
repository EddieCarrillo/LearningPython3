class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing_num = n
        for idx in range(0, n):
            missing_num ^= (nums[idx] ^ idx)
        return missing_num

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = (n * (n + 1)) // 2
        sum_nums = sum(nums)
        return sum_n - sum_nums
