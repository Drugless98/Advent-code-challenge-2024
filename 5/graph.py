

class Node:
    def __init__(self, value):
        self.Value = value
        self.Connections: list = []

    def add_connection(self, rule: tuple[int, int]):
        x, y = rule
        if x not in self.Connections:
            self.Connections[str(x)] = [y]
        else:
            self.Connections[str(x)].append(y)

class ruleSet:
    def __init__(self):
        self.Nodes: dict[Node] = {}

    def add_node(self, node_value: str):
        if node_value in self.Nodes:
            self.Nodes[node_value] = Node(node_value)

    def build(self, connections: list[str]):
        for connection in connections:
            left, right = connection.split("|")

            if left not in self.Nodes:
                self.Nodes[left] = Node(left)
            node: Node = self.Nodes[left]
            node.Connections.append(right)
    
    def check_update(self, update: list[int]) -> bool:
        for update_idx, current_nr in enumerate(update[1:]):
            prev_nr = update[update_idx]
            prev_node: Node = self.Nodes[prev_nr]
            
        #: Check connections
            has_connection = current_nr in prev_node.Connections
            if self.Nodes.get(prev_nr, False) and has_connection:
                continue
            else:
                return False
        return True
    
    def get_fixed_median(self, update: list[int]) -> list[list[int]]: #: Assuming the update list can always be fixed
        from math import floor as math_floor
        median = math_floor(len(update)/2) 

        for number in update:
            current_node: Node = self.Nodes[number]
            common_connections = [number for number in update if number in current_node.Connections]
    
            if len(common_connections) == median:
                return int(current_node.Value)
        return 0
