class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= rows or c >= cols or
                heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Pacific Ocean (top row and left column)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

        # Atlantic Ocean (bottom row and right column)
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # Intersection → cells that can reach both oceans
        return [[r, c] for r, c in pac & atl]
