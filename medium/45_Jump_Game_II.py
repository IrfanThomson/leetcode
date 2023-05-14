class Solution:
    # O(n), dynamic programming
    def jump(self, nums: List[int]) -> int:
        nums[len(nums)-1] = 0
        for i in range(len(nums)-2, -1, -1):
            min_jump = 10001
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    min_jump = min(nums[i+j]+1, min_jump)
            nums[i] = min_jump
        return nums[0]