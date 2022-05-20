class Solution: # backtracking approach (credits to NeetCode)
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(numOpen, numClose):
            # base case, when both the number of closed/open parenthesis are the same and are equal to the input: return
            if numOpen == numClose == n:
                res.append(''.join(state))
                return
            
            # recursive step
            # we want the ( to appear exactly n times, after the if takes place for the last time
            # the counter will be equal to n (and thus the number of oper parenthesis)
            if numOpen < n:
                state.append('(')
                backtrack(numOpen+1, numClose)
                state.pop()
            
            # this is needed because we could not start with a closed parenthesis, 
            # and we have to create one only if we have already opened one
            if numClose < numOpen:
                state.append(')')
                backtrack(numOpen, numClose+1)
                state.pop()
                
        res, state = [], []
        backtrack(0,0)
        return res
            
