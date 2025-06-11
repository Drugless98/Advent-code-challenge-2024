#: Std libraries
import sys, os

#: import Lib
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from inputs.Advent_input import Input

#: Constant
DAY = 2

def main(task_input):
    def part_one(task_input: str):
        #: Data Objects
        from data_object import Report
        reports_input = task_input.splitlines()
        report_objects: list[Report]= []

        #: make dataobjects
        for report in reports_input:
            report_objects.append(Report(report.split()))

        sum = 0
        for report in report_objects:
            if report.Safe:
                sum += 1
        print(f"Day {DAY} part one, result: {sum}")
        return True
    
    def part_two(task_input: str):
        from data_object import Report
        sum = -4
        reports_input = task_input.splitlines()
        report_objects: list[Report]= []

        #: make dataobjects
        for report in reports_input:
            report_objects.append(Report(report.split()))

        for report in report_objects:
            if report.Safe or report.SafeDamper:
                sum += 1
    
        print(f"Day {DAY} part two, result: {sum}")
        return True
    return part_one(task_input) and part_two(task_input)

if __name__ == "__main__":
    #: Get task info and input
    input = Input()
    day_data = input.data
    
    #: Run  
    done = main(input.get_input(DAY))

    #: Make markdown file 
    if done:
        markdown_file = os.path.join(os.path.dirname(__file__), "Task_Info.md")
        with open(markdown_file, "w+") as file:
            file.write(day_data["task_info"][str(DAY)])