class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        secondMax = None; lastMax = None; max = None;
        for num in nums:
            if num == max or num == secondMax or num == lastMax:
                continue
            if max == None or num > max:
                secondMax = lastMax
                lastMax = max
                max = num
            elif lastMax == None or num > lastMax:
                secondMax = lastMax
                lastMax = num
            elif secondMax == None or num > secondMax :
                secondMax = num

        return max if secondMax == None else secondMax
