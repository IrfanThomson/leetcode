class Solution:
    # O(n), iterate with logic
    def maxProfit(self, prices: List[int]) -> int:
        b, r = prices[0], 0
        for p in prices:
            if p > b:
                r += p - b
                b = p
            if p < b:
                b = p
        return r