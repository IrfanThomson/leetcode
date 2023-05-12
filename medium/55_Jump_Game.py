class Solution:
    # O(n), dynamic programming
    # Note: O(1) space but destroys the list, left as design choice
    def canJump(self, nums: List[int]) -> bool:
        REACHABLE, UNREACHABLE = -1, -2
        nums[len(nums)-1] = REACHABLE
        for i in range(len(nums)-2, -1, -1):
            for n in range(0, nums[i]+1):
                if nums[i+n] == REACHABLE:
                    nums[i] = REACHABLE
                    break
                nums[i] = UNREACHABLE
        return True if nums[0] == REACHABLE else False