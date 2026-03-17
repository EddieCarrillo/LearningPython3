# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTSolve(0, len(nums) - 1, nums)

    def sortedArrayToBSTSolve(self, left: int, right: int, nums:List[int]):
        if (left > right):
            return None
        m = left + ((right - left) // 2)
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBSTSolve(left, m - 1, nums)
        root.right = self.sortedArrayToBSTSolve(m+1, right, nums)
        return root
