class Solution:
    # O(n), two pointers
    def removeDuplicates(self, nums: List[int]) -> int:
        i,k = 0,1
        for n in nums:
            if nums[i] != n:
                i += 1
                nums[i] = n
                k += 1
        return k