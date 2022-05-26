class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        # if list is empty return 0
        if len(nums) == 0:
            return 0
        else:
            # set upper bound in order to avoid "list index out of range"
            nums.append(float('+inf'))
            # a bit to unpack here: I am sorting the nums, in roder to search the consecutive instances more efficiently,
            # then with dict.fromkeys I am creating a dictionary of the nums (in order to avoid duplicates),
            # then I put the unique sorted instances back into a list in order to iterate over them in the loop
            nums = list(dict.fromkeys(sorted(nums)))
            res = []
            # start the count with 1 in case we have only one element in list, or multiple elements but non consecutive
            count = 1
            for i, curr in enumerate(nums):
                # end the loop to avoid out of range
                if curr == float('+inf'):
                    break
                # if the current number values plus 1 is the same values as the next instance update the counter 
                # (it means they are consecutive)
                if curr+1 == nums[i+1]:
                    count+=1
                # if they are not consecutive append and reset the counter value 
                else:
                    res.append(count)
                    count = 1
            
            # return maximum lenght of consecutive numbers found
            return max(res)
    
