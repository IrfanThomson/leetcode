class Solution:
    # O(n) dynamic programming
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        result = []
        for n in nums:
            result.append(left)
            left *= n
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i] 
        return result