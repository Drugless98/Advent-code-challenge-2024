#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

#: Constant
DAY = 1

def main():
    def part_one():
        return None
    
    def part_two():
        return None


if __name__ == "__main__":
    #: Get task info and input
    input = Input()
    day_one_data = input.get_input(DAY)

    #: Make markdownfile if there isn't one
    markdown_file = os.path.join(os.path.dirname(__file__), "Task_Info.md")
    if not os.path.isfile(markdown_file):
        with open(markdown_file, "w+") as file:
            file.write(day_one_data["task_info"][str(DAY)])
    
    #: Run  
    main()