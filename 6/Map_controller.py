
from enum import Enum

class Direction(Enum):
    North   = "^"
    East    = ">"
    South   = "v"
    West    = "<"

    def next(self):
        directions = list(Direction)
        index = directions.index(self)
        return directions[(index + 1) % len(directions)]

class Map:
    def __init__(self, task_input: str):
        self.All_Tiles = {}
        self.Original_pos = None
        self.current_pos = None
        self.current_dir = None

        self.visited = set()

        for r_idx, row in enumerate(task_input.splitlines()):
            self.All_Tiles[r_idx] = {}

            for c_idx, col in enumerate(row):
                if not col in [".", "#"]:
                    self.current_dir = Direction(col)
                    self.current_pos = (r_idx, c_idx)
                    self.Original_pos = (r_idx, c_idx, self.current_dir)
                self.All_Tiles[r_idx][c_idx] = col

    def view_All_Tiles(self):
        string = ""
        for row in self.All_Tiles:
            for col in self.All_Tiles[row]:
                current = self.All_Tiles[row][col]
                string += current
            string += "\n"
        print(string)
        return string

    def move(self, old_pos, new_pos):
        new_x, new_y = new_pos

    #: Check if currently in a loop otherwise save pos and continue
        if (old_pos[0], old_pos[1], self.current_dir) in self.visited:
            return "Loop"
        else:
            self.visited.add((old_pos[0], old_pos[1], self.current_dir))

    #: move to next tile and place and X where guard have been 
        if new_x in self.All_Tiles and new_y in self.All_Tiles[new_x]:
        #: Normal moves
            if self.All_Tiles[new_x][new_y] in [".", "X"]:
                self.All_Tiles[old_pos[0]][old_pos[1]] = "X"
                self.current_pos = new_pos
        #: When Wall is hit change dir
            elif self.All_Tiles[new_x][new_y] == "#":
                self.current_dir = self.current_dir.next()
            return "Continue"
        else:
            self.All_Tiles[old_pos[0]][old_pos[1]] = "X"
            return "Done"
        

    def iterate(self):
        x, y = self.current_pos
        match self.current_dir:
            case Direction.North:
                status = self.move((x,y), (x-1,y))
            case Direction.East:
                status = self.move((x,y), (x, y+1))
            case Direction.South:
                status = self.move((x,y), (x+1, y))
            case Direction.West:
                status = self.move((x,y), (x, y-1))
        return status
    
    def count_X(self):
        counter = 0
        for row in self.All_Tiles:
            for col in self.All_Tiles[row]:
                current = self.All_Tiles[row][col]
                if current == "X":
                    counter += 1
        return counter
    
    def get_list_of_X(self):
        Xs = []
        for row in self.All_Tiles:
            for col in self.All_Tiles[row]:
                current = self.All_Tiles[row][col]
                if current == "X":
                    Xs.append((row, col))
        return Xs
    

def get_test_input():
    return """....#.....
                .........#
                ..........
                ..#.......
                .......#..
                ..........
                .#..^.....
                ........#.
                #.........
                ......#...""".replace(" ", "")

if __name__ == "__main__":
    input = get_test_input()
    m = Map(input)
    
    while m.iterate() == "Continue":
        pass
    print(m.count_X())
    