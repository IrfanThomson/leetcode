class Solution:
    # O(n), two pointers
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(len(nums)):
            if j > 1 and nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i