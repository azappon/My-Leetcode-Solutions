class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            # use a counter variable to save the of the branches
            nonlocal counter 
            
            # important to return the value 0
            if not node: return 0
            
            # recursion is applied to both sides of the tree
            # both left/right return the depth of their specific branch 
            left = height(node.left)
            right = height(node.right)
            
            # the counter is updated with the sum of the two sides
            counter = max(counter, left+right)
            
            # the function returns the deepest branch yet adding +1 for the current node
            return max(left, right) + 1
        
        counter = 0
        height(root)
        return counter
