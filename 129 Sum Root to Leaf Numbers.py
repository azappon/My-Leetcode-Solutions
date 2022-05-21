class Solution: # at first I approached (and failed) the problem with concatenation,
                # but the trick is to just sum the node values by multiplying by 10 the past value
                # elegant solution by NeetCode
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        def dfs(node, count):
        
            if not node: 
                return 0
                
            # the value obtained is "shifted left" with a 0 (obtained with the x10 muplitplication) 
            # and the current node value is simply added to it
            count = count * 10 + node.val
            
            # when the path ends return the count
            if not node.left and not node.right:
                return count
            
            # summ the counts fron all the paths
            return dfs(node.left, count) + dfs(node.right, count)
        
        return dfs(root, 0)
