class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(openN, closeN, s):
            if openN == closeN and openN + closeN == n * 2:
                res.append(s)
                return
            
            if openN < n:
                dfs(openN + 1, closeN, s + "(")
            
            if closeN < openN:
                dfs(openN, closeN + 1, s + ")")
        
        dfs(0, 0, "")

        return res