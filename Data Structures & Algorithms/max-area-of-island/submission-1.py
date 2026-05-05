class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        maxcount=0
        count=0

        def isvalid(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c]==0:
                return False
            return True
        def dfs(r,c):
            if not isvalid(r, c):
                return 0
            visited.add((r,c))
            return (1+    dfs(r+1, c) +
            dfs(r-1, c) +
            dfs(r, c+1) +
            dfs(r, c-1))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    count=dfs(r,c)
                    maxcount = max(maxcount, count)

                   
        return maxcount
                    
        