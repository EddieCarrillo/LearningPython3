from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        max_candies = n // 2
        unique_candies = set()
        for candy in candyType:
            unique_candies.add(candy)
            if len(unique_candies) >= max_candies:
                break
        return len(unique_candies)

sol = Solution()

print(sol.distributeCandies([1,1,2,2,3,3]))
print(sol.distributeCandies([1,1,2,3]))
print(sol.distributeCandies([6,6,6,6]))
