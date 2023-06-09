class Solution:
    # O(n), voting algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = -1
        for n in nums:
            if count == 0:
                candidate = n
                count = 1
            else:
                count = count + 1 if candidate == n else count - 1
        return candidate