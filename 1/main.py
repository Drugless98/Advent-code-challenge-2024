#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

#: Constant
DAY = 1

def main(task_input):
    def part_one(task_input: str):
        ##: make each column into sorted list
        left_arr    = []
        right_arr   = []

        for line in task_input.splitlines():
            left, right = line.split()
            left_arr.append(left)
            right_arr.append(right)
        left_arr.sort()
        right_arr.sort()

        ##: calc differences
        sum = 0
        for left, right in zip(left_arr, right_arr):
            sum += abs(int(left)-int(right))

        ##: Done
        print(f"Day {DAY} result: {sum}")
        return True
    
    def part_two(task_input: str):
        ##: make each column into sorted list
        left_arr    = []
        right_arr   = []

        for line in task_input.splitlines():
            left, right = line.split()
            left_arr.append(left)
            right_arr.append(right)
        
        ##: Calc similarity score
        similarity_score = 0
        for number in left_arr:
            similarity_score += int(number) * right_arr.count(number)

        ##: Done
        print(f"Day {DAY} result: {similarity_score}")
        return True
    
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