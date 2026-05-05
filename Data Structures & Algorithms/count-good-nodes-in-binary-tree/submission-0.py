class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            count = 0
            
            # If current node is >= max seen so far → it's a good node
            if node.val >= max_so_far:
                count = 1
            
            # Update max for children
            new_max = max(max_so_far, node.val)
            
            # Count from left and right
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count
        
        return dfs(root, float('-inf'))
