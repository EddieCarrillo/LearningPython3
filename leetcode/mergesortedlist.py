class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Start from the right of the larger buffer, since this doesn't lead to overwrites
        l_idx = m - 1
        r_idx = n - 1
        new_idx = m + n - 1
        while (l_idx >= 0 and l_idx < m and r_idx < n and r_idx >= 0):
            if nums1[l_idx] > nums2[r_idx]:
                nums1[new_idx] = nums1[l_idx]
                l_idx -= 1
            else:
                nums1[new_idx] = nums2[r_idx]
                r_idx -= 1
            new_idx -= 1
        while(r_idx >= 0 and r_idx < n):
            nums1[new_idx] = nums2[r_idx]
            new_idx -= 1
            r_idx -= 1
        #Nothing needed for the left-case, since, it's already in order
