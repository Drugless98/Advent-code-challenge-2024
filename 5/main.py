#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input, time_execution

#: Constant
DAY = 5

def main(task_input):
    @time_execution
    def part_one(task_input: str):
        from graph import ruleSet
        from math  import ceil

        connections, updates = task_input.split("\n\n")
        correct_updates = 0

        #: make nodes and connections:
        rule_set = ruleSet()
        rule_set.build(connections.split("\n"))
        
        #: Check updates
        for update in updates.split("\n")[:-1]:
            update_arr = update.split(",")
            if rule_set.check_update(update_arr):
                middle_idx = int(len(update_arr)/ 2)
                correct_updates += int(update_arr[middle_idx]) #: Find the number in the middle and add it to answer
        
        print(f"Day {DAY} part one, result: {correct_updates}")
        return correct_updates
    
    @time_execution
    def part_two(task_input: str):
        from graph import ruleSet
        connections, updates = task_input.split("\n\n")
        corrected_updates = 0

        #: make nodes and connections:
        rule_set = ruleSet()
        rule_set.build(connections.split("\n"))

        for update in updates.split("\n")[:-1]:
            update_arr = update.split(",")
            if not rule_set.check_update(update_arr):
                corrected_updates += rule_set.get_fixed_median(update_arr)
        
        print(f"Day {DAY} part two, result: {corrected_updates}")
        return corrected_updates
    
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