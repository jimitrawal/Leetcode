class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands +=1
                    visited.add((i,j))
                    self.traverse(grid,i,j,visited)
        return islands    

    def traverse(self, grid: List[List[str]], i, j, visited):
        if i+1<len(grid) and grid[i+1][j] == "1" and (i+1,j) not in visited:
            grid[i+1][j] = "0"
            visited.add((i+1,j))
            self.traverse(grid,i+1,j,visited)
        if i-1>=0 and grid[i-1][j] == "1" and (i-1,j) not in visited:
            grid[i-1][j] = "0"
            visited.add((i-1,j))
            self.traverse(grid,i-1,j,visited)
        if j+1<len(grid[i]) and grid[i][j+1] == "1" and (i,j+1) not in visited:
            grid[i][j+1] = "0"
            visited.add((i,j+1))
            self.traverse(grid,i,j+1,visited)
        if j-1>=0 and grid[i][j-1] == "1" and (i,j-1) not in visited:
            grid[i][j-1] = "0"
            visited.add((i,j-1))
            self.traverse(grid,i,j-1,visited)