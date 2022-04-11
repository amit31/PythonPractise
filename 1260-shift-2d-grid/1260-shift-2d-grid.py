class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()
        
        # transform the grid into a 1D queue
        for i in range(rows):
            for j in range(cols):
                queue.append(grid[i][j])
        print(queue)
        # shift the queue of k positions
        for _ in range(k):
            queue.appendleft(queue.pop())

        # transform the queue into a 2D grid
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = queue.popleft()

        return grid