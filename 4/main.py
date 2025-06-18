#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

#: Constant
DAY = 4


def main(task_input):
    from graph import Graph, Node, Pos

    def part_one(task_input: str):      
        graph = Graph(task_input)
        xmas_count = graph.search_for_xmas()

        print(f"Day {DAY} part one, result: {xmas_count}")
        return xmas_count
    
    def part_two(task_input: str):
        graph = Graph(task_input)
        mas_count = graph.search_for_mas()

        print(f"Day {DAY} part two, result: {mas_count}")
        return mas_count
    
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