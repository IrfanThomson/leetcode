class Solution:
    # O(n) swap trick
    def reverse(self, nums: List[int], low: int, high: int) -> None:
        while high > low:
            nums[high], nums[low] = nums[low], nums[high]
            high -= 1
            low += 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)