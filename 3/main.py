#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

#: Constant
DAY = 3

def main(task_input):
    def part_one(task_input: str):
        #: Find number pairs inside a valid mul expression
        import re
        regex_pattern = "mul\(([0-9]*),([0-9]*)\)"
        expressions = re.findall(regex_pattern, task_input)
        
        #: Sum up the pairs
        summed_expressions = sum([int(exp_1) * int(exp_2) for exp_1, exp_2 in expressions]) 
        print(f"Day {DAY} part one, result: {summed_expressions}")
        return summed_expressions
    
    def part_two(task_input: str):
        #: find pairs, do()s and don'ts 
        import re
        regex_pattern = "mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)"
        expressions = re.findall(regex_pattern, task_input)
        
        #: make expression compiler
        from helper_class import Memory_Compiler 
        compiler = Memory_Compiler(expressions)
        result = compiler.get_result()
        
        print(f"Day {DAY} part two, result: {result}")
        return result
    
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