class Solution(object):
    def recursive_solution(self, grid, x_len, y_len, k, counter, d_sum=0, x=0, y=0):
        # print(f"{grid[y][x]} ", end="")
        if x < x_len - 1:
            self.recursive_solution(grid, x_len, y_len, k, counter, d_sum + grid[y][x], x + 1, y)
        if y < y_len - 1:
            self.recursive_solution(grid, x_len, y_len, k, counter, d_sum + grid[y][x], x, y + 1)
        elif x == x_len - 1 and y == y_len - 1:
            d_sum += grid[y][x]
            # print(f"sum: {d_sum}")
            if d_sum % k == 0:
                counter[0] += 1
                print(counter)
        return counter[0]

    def numberOfPaths(self, grid, k):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                grid[y][x] = grid[y][x] % k
        x_len = len(grid[0])
        y_len = len(grid)
        return self.recursive_solution(grid, x_len, y_len, k, [0])


grid = [[5, 2, 4], [3, 0, 5], [0, 7, 2]]
k = 3
print(Solution().numberOfPaths(grid, k))
