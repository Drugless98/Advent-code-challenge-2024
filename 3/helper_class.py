#:public libraries 
from dataclasses import dataclass
from re import compile, match, findall

mul_regex_pattern = compile("mul\([0-9]*,[0-9]*\)")


class Flag: #: Flag object of either do() - True and Don't() - False
    def __init__(self, flag: str):
        self.Flag = True if flag == "do()" else False

class Multiply: #: Multiply object, get the numbers and multiply them so they are ready for use
    def __init__(self, input: str):
        self.Value = sum([int(arg_1) * int(arg_2) for arg_1, arg_2 in findall("mul\(([0-9]*),([0-9]*)\)", input)])

class Memory_Compiler: #: Compile corrupted data
    def __init__(self, expressions: list[StopIteration]):
        self.Expressions = [Multiply(expression) if mul_regex_pattern.match(expression) else Flag(expression) for expression in expressions]
    
    def get_result(self):
        #: Flag and sum-accumulator
        enabled = True
        sum     = 0
        
        #: run through expressions
        for expression in self.Expressions:
            if isinstance(expression, Multiply) and enabled:
                sum += expression.Value
            elif isinstance(expression, Flag):
                enabled = expression.Flag
        return sum