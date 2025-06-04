import heapq

def minPath(grid, k):
    N = len(grid)
    
    # Initialize min_overall_path with values larger than any possible grid value.
    # N*N is the maximum value in the grid. So N*N + 1 is guaranteed to be larger.
    max_grid_val = N * N
    min_overall_path = [max_grid_val + 1] * k

    # Directions for movement: (dr, dc) for (row_change, col_change)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Iterate through every cell as a potential starting point
    for start_r in range(N):
        for start_c in range(N):
            # Priority queue: stores (current_path_tuple, current_row, current_col)
            # current_path_tuple is a tuple because lists are mutable and cannot be used
            # as elements for direct comparison in heapq if their content changes,
            # and tuples are lexicographically comparable.
            pq = []
            
            # Initial state: path of length 1 starting from (start_r, start_c)
            heapq.heappush(pq, (tuple([grid[start_r][start_c]]), start_r, start_c))

            while pq:
                current_path_tuple, r, c = heapq.heappop(pq)
                current_path_list = list(current_path_tuple) # Convert to list for comparison and extension

                current_len = len(current_path_list)

                # Pruning step: If the current partial path (up to current_len) is already
                # lexicographically greater than the corresponding prefix of the best path found so far (min_overall_path),
                # then any path extending from this current_path will also be worse.
                # This check also correctly handles cases where current_len == k.
                if current_path_list > min_overall_path[:current_len]:
                    continue # Prune this branch

                if current_len == k:
                    # Found a path of length k. Check if it's better than min_overall_path.
                    if current_path_list < min_overall_path:
                        min_overall_path = current_path_list
                    continue # Path is complete, no need to extend further

                # If current_len < k, explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check if neighbor is within grid boundaries
                    if 0 <= nr < N and 0 <= nc < N:
                        new_path_list = current_path_list + [grid[nr][nc]]
                        
                        # Before pushing, perform a pre-check pruning for the new path.
                        # If the new path, even as a partial path, is already worse than the best found,
                        # don't add it to the priority queue.
                        if len(new_path_list) <= k and new_path_list > min_overall_path[:len(new_path_list)]:
                            continue

                        heapq.heappush(pq, (tuple(new_path_list), nr, nc))
    
    return min_overall_path