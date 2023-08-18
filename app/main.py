from sokoban_state import SokobanState

# This will be the initial board. W is a wall, . is an empty space, P is the player, 
# B is a box and G is the goal
initial_board = [
    ['W', 'W', 'W', 'W', 'W', 'W'],
    ['W', '.', '.', '.', '.', 'W'],
    ['W', '.', 'P', 'G', '.', 'W'],
    ['W', '.', 'B', 'G', '.', 'W'],
    ['W', '.', '.', '.', '.', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W'],
]

initial_player_pos = (2, 2)
initial_box_positions = [(3, 2)]
initial_goal_positions = [(2, 3), (3, 3)]



if __name__ == "__main__":
    
    initial_state = SokobanState(initial_board, initial_player_pos, initial_box_positions, initial_goal_positions)

    print(initial_state)

