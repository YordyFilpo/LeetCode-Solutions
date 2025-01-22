class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i,j))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            i, j = queue.popleft()
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:

                    height[nr][nc] = height[i][j] + 1
                    queue.append((nr, nc))
        
        return height