class Solution:
    # O(n) iteration, with the problem's assumption that ceiling is a constant <= 1000
    def hIndex(self, citations: List[int]) -> int:
        ceiling = min(max(citations), len(citations))
        for h in range(ceiling,-1,-1):
            count = 0
            for num in citations:
                count = count + 1 if num >= h else count
            if count >= h:
                return h
            
    # O(nlog(n)) sort 
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(0, len(citations)):
            if citations[i] < i+1:
                return i
            if citations[i] == i+1:
                return i+1
        return len(citations)