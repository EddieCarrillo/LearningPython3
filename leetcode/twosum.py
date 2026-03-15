# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online
# programiz.pro/ide/python

from typing import List

#ex 1
nums = [2,7,11,15]
target = 9

#ex 2
nums2 = [3,2,4]
target2 = 6

#ex 3
nums3 = [3,3]
target3 = 6


# O(n^2) time, O(k) space 
class BadSolution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for idx in range(len(nums)):
      for idx2 in range(len(nums)):
        if idx == idx2: 
          continue
        if nums[idx] + nums[idx2] == target:
          return [idx, idx2]
    return []

#(O(n) time O(n) space (single pass))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {nums[0]: 0}
        for idx in range(1,len(nums)):
            if target - nums[idx] in visited:
              return [visited[target - nums[idx]], idx]
            visited[nums[idx]] = idx
        return []

sol = Solution()

result = sol.twoSum(nums, target)
print(result)

result = sol.twoSum(nums2, target2)
print(result)

result = sol.twoSum(nums3, target3)
print(result)

badSold = BadSolution()

result = badSold.twoSum(nums, target)
print(result)

result = badSold.twoSum(nums2, target2)
print(result)

result = badSold.twoSum(nums3, target3)
print(result)