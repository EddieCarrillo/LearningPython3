class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        inter_range_ptr = 0
        intra_range_ptr = inter_range_ptr
        range_summary = []
        while inter_range_ptr < len(nums):
            #prepare to scan through new range
            intra_range_ptr = inter_range_ptr + 1
            while intra_range_ptr < len(nums) and nums[intra_range_ptr] - nums[intra_range_ptr -1] == 1:
                intra_range_ptr += 1
            #We either hit the end of the array, or encounterd a non range element.
            if intra_range_ptr - 1 == inter_range_ptr:
                range_summary.append(f"{nums[inter_range_ptr]}")
            else:
                range_summary.append(f"{nums[inter_range_ptr]}->{nums[intra_range_ptr - 1]}")
            #new range
            inter_range_ptr = intra_range_ptr
        return range_summary
                
