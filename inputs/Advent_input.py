

# PUT SESSION CODE HERE #
SESSION_CODE = "53616c7465645f5f1996df66031206d208437335c32db8303ab4df92eb8661d4e1cb258f69f8c028cd7125d8c23798b13a9ba9fc744afe0b6e4df4c51854af0a"

import time
def time_execution(func: callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took: {time.time() - start_time:6f}')
        return result
    return wrapper

class Input:
    @time_execution
    def __init__(self):
        import os
        from json import load

        #: Input Attributes
        current_folder  = os.path.dirname(__file__)
        self.data_file       = f"{current_folder}\\advent_inputs.json"

        #: load data if needed
        if not os.path.isfile(self.data_file):
            self._make_input_file(SESSION_CODE)

        #: Save data as attribute
        with open(self.data_file, "r", encoding="utf-8") as file:
            self.data = load(file)
            self.data = self.data

    def _make_input_file(self, session_token: str):
        import requests
        import json

        # Send a GET request to advent of code with session cookie
        cookie = {"session" : session_token}
        json_data: dict[str]      = {
            "inputs" : {},
            "task_info" : {}
        }


        for day in range(1,25):
            #: Get day input
            response = requests.get(f'https://adventofcode.com/2024/day/{day}/input', cookies=cookie).content.__str__()
            response_cleaned = response[2:]
            response_cleaned = response_cleaned[:-1]
            json_data["inputs"][day]  = response_cleaned

            #: Get day task info
            import html2text
            response = requests.get(f'https://adventofcode.com/2024/day/{day}', cookies=cookie).content.__str__()

            #: Convert html to markdown
            ##: Find indexes for task start and end
            start_index = response.find("---")
            end_index   = response.find("**</p>\\n<p>At this point, you should <a")

            ##: convert
            markdown = html2text.html2text(response[start_index:end_index])
            markdown = markdown.replace("---", "#")
            markdown = markdown.replace("\\n", "")
            markdown = markdown.replace("\\", "")
            json_data["task_info"][day]  = markdown

        with open(self.data_file, "w+", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)

    def get_input(self, day: int) -> str:
        """day is the day you would like the input for, e.g. get_input(2) return input for day 2"""
        return self.data["inputs"][str(day)].replace("\\n", "\n")

if __name__ == "__main__":
    i = Input()
    i._make_input_file(SESSION_CODE)