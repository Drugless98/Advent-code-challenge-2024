
from enum import Enum

class Direction(Enum):
    North   = "^"
    East    = ">"
    South   = "v"
    West    = "<"

class Map:
    def __init__(self, task_input: str):
        self.All_Tiles = {}
        self.Obstacle_rows: dict[list] = {} #: Dict of obstacles in each row
        self.Obstacle_cols: dict[list] = {} #: Dict of obstacles in each col
        self.current_pos = None
        self.current_dir = None

        for r_idx, row in enumerate(task_input.splitlines()):
            self.All_Tiles[r_idx] = {}
            self.Obstacle_rows[r_idx] = []

            for c_idx, col in enumerate(row):
                if not c_idx in self.Obstacle_cols:
                    self.Obstacle_cols[c_idx] = []

                if not col in [".", "#"]:
                    self.current_pos = (r_idx, c_idx)
                    self.current_dir = Direction(col)
                elif col == "#":
                    self.Obstacle_rows[r_idx].append(c_idx)
                    self.Obstacle_cols[c_idx].append(r_idx)
                self.All_Tiles[r_idx][c_idx] = col

    def view_All_Tiles(self):
        import json
        print(json.dumps(self.All_Tiles, indent=2))

    def find_obstacle(self, pos: tuple[int, int], dir: Direction):
        row_pos, col_pos = pos
        match dir:
            case Direction.North:
            ##: look through the obstacles in the same column and find the closest one with lower row index (going up)
                for idx, val in enumerate(self.Obstacle_cols[col_pos]):
                    if val < row_pos and self.Obstacle_cols[col_pos][idx+1] > row_pos:
                        return (val, col_pos)

            case Direction.East:
                pass

            case Direction.South:
                pass

            case Direction.West:
                pass

    def iterate(self):
        obstacle = self.find_obstacle(self.current_pos, self.current_dir)