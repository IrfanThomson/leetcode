class Solution:
    """
    front, back = 0, len(s)-1
    while front < back:
        if front != back:
            return false
        front += 1
        back -= 1
    return true
    
    O(n), two pointers
    """
    import re
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[\W_]", "",s)
        front, back = 0, len(s)-1
        while front < back:
            if s[front].lower() != s[back].lower():
                return False
            front += 1
            back -= 1
        return True