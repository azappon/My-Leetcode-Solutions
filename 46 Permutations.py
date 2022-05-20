class Solution: # backtracking solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, state, res):
            # base case
            if len(nums) == len(state):
                res.append(state.copy())
                return
            # recursive case
            for n in nums:
                # we need to select only the cases in which the digits have unique occurences
                # thus the following if statement
                # careful to include all recursive steps inside 'if' indentation
                if n not in state:
                    state.append(n)
                    dfs(i+1, state, res)
                    state.pop()

        res, state = [], []
        dfs(0, state, res)
        return res
