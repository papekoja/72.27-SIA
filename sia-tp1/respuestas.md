
# Answers

## Exercise 1

1. The easiest and most straightforward approach would be to represent each state with a 2-dimensional matrix. Alternatively, you can define the state using a custom class.
2. Two heuristics that can be used to solve the problem are the Misplaced Tiles heuristic and the Manhattan Distance heuristic. The Misplaced Tiles heuristic counts the number of tiles that are not in the correct position. However, the more optimal approach is to use the Manhattan distance. The Manhattan distance is the total sum of each tile's current position to its goal position. This provides a rough estimate of how many moves are needed for the solution.
3. Iterative improvement algorithms fit well with the two mentioned heuristics. While the Hill Climbing algorithm is decent, it has a high risk of getting stuck. Therefore, Simulated Annealing is a better choice for the problem, as it balances exploration and has a good chance of finding a near-optimal solution.