class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start_ptr = 0
        search_ptr = 0
        n = len(nums)
        max_cnt = 0
        while search_ptr < n:
            while search_ptr < n and nums[search_ptr] != 1:
                search_ptr += 1
            cur_cnt = 0
            start_ptr = search_ptr
            while search_ptr < n and nums[search_ptr] == 1:
                cur_cnt += 1
                search_ptr += 1
            max_cnt = max(max_cnt, cur_cnt)
        return max_cnt
        
