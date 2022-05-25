class Solution: # elegant pythonic solution
    def isAnagram(self, s: str, t: str) -> bool:
        # cases like "aa"/"a" would not work using se(s)!
        if Counter(s) == Counter(t):
            return True
