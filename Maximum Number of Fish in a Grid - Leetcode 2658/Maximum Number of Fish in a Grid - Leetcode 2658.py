class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid) # number of rows
        columns = len(grid[0]) # number of columns
        visited_cells = set() # to keep track of the cells visited
        max_fish = 0 # counter for the max number of fishes caught
        
    
        def dfs(r, c):
            # base cases: out of bounds, cell already visited, or the cell contains water (equals 0)
            if r < 0 or r >= rows or c < 0 or c >= columns or (r, c) in visited_cells or grid[r][c] == 0:
                return 0
            
            # mark the cell as visited
            visited_cells.add((r, c)) 

            # collect the fish at the given cell
            fish = grid[r][c]

            # explore adjacent cells and collect the fishes
            fish += dfs(r + 1, c) # down
            fish += dfs(r - 1, c) # up
            fish += dfs(r, c + 1) # right
            fish += dfs(r, c - 1) # left

            return fish

        # iterate through the cells in the grid
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] > 0 and grid[r][c] not in visited_cells:
                    max_fish = max(max_fish, dfs(r, c)) # run dfs and update max_fish
        
        return max_fish



        

