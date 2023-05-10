class Solution:
    # O(n), iterate with logic
    def maxProfit(self, prices: List[int]) -> int:
        b, s, result = prices[0], -1, 0
        for p in prices:
            if p <= b:
                b = p
                s = -1
            elif p > s:
                s = p
                result = s - b if result < s - b else result
        return result