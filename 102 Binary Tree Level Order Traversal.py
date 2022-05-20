class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level):
            if not node: return
            # if all level nodes are appended create new sub-list / if there is no node appended yet start appending 
            if level >= len(res):
                res.append([node.val])
            # append to the sub-list of the level we're in
            elif level < len(res):
                res[level].append(node.val)
            # recursive steps for next levels (update level!)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
             
        res = []
        dfs(root, 0)
        return res
