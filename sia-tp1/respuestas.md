
# Answers

## Exercise 1

1. The easiest and most straightforward approach would be to represent each state with a 2-dimensional matrix. Alternatively, you can define the state using a custom class.
2. Two heuristics that can be used to solve the problem are the Misplaced Tiles heuristic and the Manhattan Distance heuristic. The Misplaced Tiles heuristic counts the number of tiles that are not in the correct position. However, the more optimal approach is to use the Manhattan distance. The Manhattan distance is the total sum of each tile's current position to its goal position. This provides a rough estimate of how many moves are needed for the solution.
3. Several algorithms can be used to solve the puzzle such as BFS, DFS, IDDFS, Hill Climbing and A*. The most optimal algorithm is A* since it can be used with both Misplaced Tiles heuristic and the Manhattan distance heuristic to find the optimal solution. The other algorithms do not use a heuristic and are therefore not optimal. However, BFS and DFS are complete algorithms, meaning that they will always find a solution if it exists. A* is not complete since it can get stuck in a loop if the heuristic is not admissible.