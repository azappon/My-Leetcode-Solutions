class Solution: # credits to NeetCode for this solution
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        # map every digit to their corrisponding string
        d = {'2':'abc',
             '3':'def',
             '4':'ghi',
             '5':'jkl',
             '6':'mno',
             '7':'pqrs',
             '8':'tuv',
             '9':'wxyz'}
        

        def solver(i, state):
            # base case, if the lenght of the state is equal to the number of giver digits
            if len(state) == len(digits):
                res.append(state)
                return
            
            # recursive case, we pass the first letter j into state and than recursively we make j start one index later (i+1), 
            # when the state has the wanted lenght we append and the j stays the same for the next recursive step until the 
            # loop ends and the state returns empty and the j from the first step is updated as the second digit and so on
            for j in d[digits[i]]:
                helper(i+1, state + j)
        
        # if digits is empty we want to avoid appending empty string
        if digits: 
            solver(0, '')
        return res

