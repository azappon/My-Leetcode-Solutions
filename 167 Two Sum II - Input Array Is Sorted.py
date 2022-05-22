# iterative solution (memory efficient)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r-=1                
            if (numbers[l] + numbers[r]) < target:
                l+=1
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]

# recursive solution (less memory efficient)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers)-1
        def helper(l, r):
            if (numbers[l] + numbers[r]) == target:
                if l+1 not in res:
                    res.append(l+1)
                if r+1 not in res:
                    res.append(r+1)
                return  
            if (numbers[l] + numbers[r]) > target:
                r-=1
            if (numbers[l] + numbers[r]) < target:
                l+=1         
            helper(l, r)
  
        helper(l, r)
        return res
                
                
