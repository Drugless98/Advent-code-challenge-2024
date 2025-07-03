


class Calibration:
    def __init__(self, input: str):
        target, numbers = input.split(": ")
        self.Target = int(target)
        self.Numbers = [int(i) for i in numbers.split(" ")]