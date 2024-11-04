class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        letters = []
        for i in s:
            letters.append(i)
        
        for i in t:
            if i in letters:
                letters.remove(i)
            else:
                return False
        
        return True