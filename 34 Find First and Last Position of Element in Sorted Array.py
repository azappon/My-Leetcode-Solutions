class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
            
        # list comprehension creates a list the indices of target values from the input list (notice: input list already sorted)
        res = [i for i, e in enumerate(nums) if e == target]
        
        # if we have more than two values corresponding to target return the outer boundaries
        if len(res) > 2:
            return [res[0], res[-1]]
        
        # if there is only one value corresponding to target return its index on both ends
        if len(res) < 2:
            return [res[0], res[0]]
        
        return res
