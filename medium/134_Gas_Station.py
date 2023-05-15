class Solution:
    # O(n) backwards iteration (can be solved with forward iteration too)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        high = -1
        index = -1
        for i in range(len(gas)-1, -1, -1):
            total += gas[i] - cost[i]
            if total > high:
                high = total
                index = i
        if total < 0:
            return -1
        return index