class Solution(object):
    def numIslands(self, grid):
        #check for proper grid
        if grid == [[]] or grid[0] == []:
            return 0
        
        height = len(grid)
        width = len(grid[0])
        islands = 0

        queue = []
        
        i = 0
        j = 0       
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    islands += 1
                    queue.append((i,j))
                    #Enter loop to sink islands
                    for row,column in queue:
                        if grid[row][column] == "1":
                            grid[row][column] = "0"
                            #right to queue
                            if column < width - 1:  #don't check to right if at end
                                queue.append((row,column+1))
                            #down to queue
                            if row < height - 1:    #don't check down if bottom row
                                queue.append((row+1,column))
                            #left to queue
                            if column > 0:          #dont check left if first
                                queue.append((row,column-1))
                            #up to queue
                            if row > 0:             #don't check up if top row
                                queue.append((row-1,column))
                        else: #grid[row][number] = zero
                            continue
                    queue = [] #reset queue
                else: #if grid[i][j] == 0
                    continue
        return islands
    
    '''
        def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        """
    '''