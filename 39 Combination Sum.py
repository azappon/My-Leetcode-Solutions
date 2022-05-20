class Solution: # backtracking solution
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, state, remain, res):
            # base case
            if remain == 0:
                res.append(state)
                return
            # recursive case
            for j in range(i, len(candidates)):
                # pruning every state after we encounter the first digit that "overshoots" our state sum
                if remain < candidates[j]: break
                # update the index j if all jth digits sums to target or when breaking
                # add new candidate to state
                # update remain with the new candidate
                dfs(j, state + [candidates[j]], remain - candidates[j], res)
                
        # fundamental to sort the array in order to achieve efficient pruning
        candidates.sort()
        res, state = [], []
        dfs(0, state, target, res)
        return res
