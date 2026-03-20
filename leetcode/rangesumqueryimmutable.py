class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.l_range = [] 
        self.r_range = [] 
        self.full_sum = 0
        l_sum = 0
        r_sum = 0
        for idx in range(0, self.n):
            self.l_range.append(l_sum)
            l_sum += nums[idx]
            self.r_range.append(r_sum)
            r_sum += nums[self.n - 1 -idx]
            self.full_sum += nums[idx]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.full_sum - self.l_range[left] - self.r_range[self.n - right - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
