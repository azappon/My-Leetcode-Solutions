class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap needed to both store the numbers and their indexes
        hashmap = {}
        
        for i, e in enumerate(nums):
            # create the difference between current num and the target
            diff = target - e
            # whilst we've not yet encountered two "complement nums" we store 
            # the value (and index) of the current num in our hashmap
            if diff not in hashmap:  
                hashmap[e] = i
            else:
                # if the difference is inside the hashmap we have already passed 
                # the "complement num" to the current num and should return both their indexes
                return [hashmap[diff], i]
