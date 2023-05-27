class Solution:
    # O(n), iteration with trick, but there are ways to do it with patterns
    def trap(self, height: List[int]) -> int:
        total, cur_trap, peak, cur_elevation = 0, 0, 0, 0
        for h in height:
            if h >= cur_elevation:
                cur_elevation = h
                total += cur_trap
                cur_trap = 0
            else:
                cur_trap += cur_elevation - h
        peak = cur_elevation
        cur_elevation = 0
        cur_trap = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] >= cur_elevation:
                cur_elevation = height[i]
                total += cur_trap
                cur_trap = 0
                if height[i] == peak:
                    break
            else:
                cur_trap += cur_elevation - height[i]
        return total