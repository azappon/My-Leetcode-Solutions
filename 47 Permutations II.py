class Solution: # backtracking solution (works for 46-Permutations too)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # create a map of all digits in nums, 
        # we want unique permutations but there are duplicates!
        hashmap = Counter(nums)
        res, state = [], []
        
        def dfs(state, res):
            # base case
            if len(nums) == len(state):
                res.append(state.copy())
                return
            # recursive case
            for n in hashmap:
                # if we have not used all instances of digit 'n' keep recursin'!
                if hashmap[n] > 0:
                    state.append(n)
                    # update values of hashmap: -1 when values is used
                    hashmap[n]-=1
                    dfs(state, res)
                    # update values of hashmap: +1 when we start new permutation (state)
                    hashmap[n]+=1
                    state.pop()
                
        dfs(state, res)
        return res
