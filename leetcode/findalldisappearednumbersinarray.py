class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disappeared = []
        #be careful with iterators, and updating, they don't work well
        #eleIdx = the current element iterated
        #val = val at eleIdx
        #mappedIdx = val, but used to map to an index in the array, may be negative, so, need to make it positive, then, it's within 1...n, so, we need to subtract by one.
        #nums[mappedIdx] value at place where val represents
        for eleIdx in range(0, n):
            val = abs(nums[eleIdx])
            mappedIdx = abs(val) - 1
            nums[mappedIdx] = abs(nums[mappedIdx]) * -1
        for idx in range(1, n+1):
            if nums[idx - 1] >= 0:
                disappeared.append(idx)
        return disappeared
