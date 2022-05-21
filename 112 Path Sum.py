class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, count):
            if not node:
                return False
            
            # add the node values in order to create the sum of the path root-leaf
            count = count + node.val
            
            # when the leaf is reached if its sum is equal to the target return True
            if not node.left and not node.right:
                if count == targetSum:
                    return True
            
            return dfs(node.left, count) + dfs(node.right, count)
                    
        return dfs(root, 0)
