

# PUT SESSION CODE HERE #
SESSION_CODE = "53616c7465645f5f1996df66031206d208437335c32db8303ab4df92eb8661d4e1cb258f69f8c028cd7125d8c23798b13a9ba9fc744afe0b6e4df4c51854af0a"

class Input:
    def __init__(self):
        import os

        self.data = None
        current_folder  = os.path.dirname(__file__)
        self.data_file       = f"{current_folder}\\advent_inputs.json"

    def _make_input_file(self, session_token: str):
        import requests
        import json


        # Send a GET request to advent of code with session cookie
        cookie = {"session" : session_token}
        json_data: dict[str] = {}

        for day in range(1,25):
            response = requests.get(f'https://adventofcode.com/2024/day/{day}/input', cookies=cookie).content.__str__()
            response_cleaned = response[2:]
            response_cleaned = response_cleaned[:-1]
            json_data[day]  = response_cleaned

        with open(self.data_file, "w+", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)

    def get_input(self, day: int) -> str:
        """day is the day you would like the input for, e.g. get_input(2) return input for day 2"""
        from json import load

        if self.data == None:
            with open(self.data_file, "r", encoding="utf-8") as file:
                self.data = load(file)
                self.data = self.data
        return self.data[str(day)].replace("\\n", "\n")

if __name__ == "__main__":
    i = Input()
    i._make_input_file(SESSION_CODE)