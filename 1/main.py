#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

#: Constant
DAY = 1

def main(task_input):
    def part_one(task_input: str):
        def split_into_lists(header, tail):
            pass

        left_arr, right_arr = split_into_lists(task_input[0], task_input[1:])



        return None
    
    def part_two(task_input):
        return None
    
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