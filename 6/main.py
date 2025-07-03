#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input, time_execution



#: Constant
DAY = 6

def main(task_input):
    @time_execution
    def part_one(task_input: str):
        from Map_controller import Map
        guard_map = Map(task_input)
        while guard_map.iterate() == "Continue":
            pass #: Iterate until guard leaves map or are in a loop

        print(f"Day {DAY} part one, result: {guard_map.count_X()}")
        return True

    @time_execution
    def part_two(task_input: str):
    #: As loop can only happen with obstructions on visited tiles
    #: I try to place one on each visited tile and count any loops

        from Map_controller import Map
        guard_map = Map(task_input)

        #: Run once to get Map with X
        while guard_map.iterate() == "Continue":
            pass #: Iterate undtil guard leaves
        
        #: Place guard back in initial pos
        x, y, dir = guard_map.Original_pos
        guard_map.All_Tiles[x][y] = dir.value
        guard_map.current_dir = dir

        #: get list of Xs
        Xs_list = guard_map.get_list_of_X()

        #: Try a timeline for each obstruction placement
        counter = 0
        import copy 

        original_X_guardmap = copy.deepcopy(guard_map.All_Tiles)
        for timeline in Xs_list:
            #: Reset for next timeline
            guard_map.All_Tiles = copy.deepcopy(original_X_guardmap)
            x, y = timeline
            guard_map.All_Tiles[x][y] = "#"
            guard_map.visited = set()
            x, y, guard_map.current_dir = guard_map.Original_pos
            guard_map.current_pos = (x,y)

            while (result := guard_map.iterate()) == "Continue":
                pass
            if result == "Loop":
                counter += 1
        print(counter)


    return part_one(task_input) and part_two(task_input)


if __name__ == "__main__":
    #: Get task info and input
    input = Input()
    day_data = input.data
    
    #: Run  
    done = main(input.get_input(DAY))

    if done:
        #: Make markdown file 
        markdown_file = os.path.join(os.path.dirname(__file__), "Task_Info.md")
        with open(markdown_file, "w+") as file:
            file.write(day_data["task_info"][str(DAY)])