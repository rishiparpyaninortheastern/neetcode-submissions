class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            # Base case: both nodes are None → same
            if not p and not q:
                return True
            
            # If one is None or values don't match → not same
            if (not p or not q) or (p.val != q.val):
                return False
            
            # Recursively check left and right subtrees
            left_same = dfs(p.left, q.left)
            right_same = dfs(p.right, q.right)
            
            # Both sides must be same
            return left_same and right_same
        
        return dfs(p, q)
