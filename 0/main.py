#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

import time
def time_execution(func: callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start_time)
        return result
    return wrapper

#: Constant
DAY = _

def main(task_input):
    def part_one(task_input: str):
        return None
    
    def part_two(task_input: str):
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