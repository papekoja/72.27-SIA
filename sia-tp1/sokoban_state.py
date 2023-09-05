
class SokobanState:

    def __init__(self, board, player_pos, box_positions, goal_positions):
        self.board = board                      # 2D array representing the game board
        self.player_pos = player_pos            # Current position of the player
        self.box_positions = box_positions      # Positions of boxes on the board
        self.goal_positions = goal_positions    # Positions of the storage goals
