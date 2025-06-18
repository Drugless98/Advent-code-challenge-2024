NEXT = {
    "X" : "M",
    "M" : "A",
    "A" : "S",
    "S" : None
}

class Pos:
    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y
    
    def __repr__(self): #: Shown in strings
        return f"pos({self.X}, {self.Y})"
    
    def __iter__(self): #: Ensure that Pos() reutrns tuple[x, y]
        yield self.X
        yield self.Y

class Node: #: Data object for nodes in the graph
    def __init__(self, pos: tuple[int, int], letter: str):
        self.Position = Pos(pos[0], pos[1])
        self.Letter = letter

class Graph: #: Graph of nodes
    #: Make Graph
    def __init__(self, text_input: str):
        self.Graph = {} #: Stor nodes in dict

        lines = text_input.split("\n")
        for row_idx, row_values in enumerate(lines):
            for col_idx, char in enumerate(row_values):
                if row_idx not in self.Graph:
                    self.Graph[row_idx] = {col_idx : Node((row_idx, col_idx), char)}
                else:
                    self.Graph[row_idx][col_idx] = Node((row_idx, col_idx), char)
        ####: Graph example:
        #:   { 
        #:     0 : {
        #:          0 : Node1,
        #           1 : Node2
        #:          }
        #:     1 : {
        #:          0 : Node3,
        #:          1 : Node4
        #:         }
        #:   
        #:   }
        #: Contains a 2 by 2 table of 4 Nodes. 
        #: Graph[0] return dict of nodes in row 0 and Graph[0][1] returns Node2
    
    #: Graph functions
    def get_node(self, pos: Pos) -> Node:
        x, y        = pos
        row: dict   = self.Graph.get(x, None)
        return row.get(y, None) if row else None

    def get_neighbors(self, node: Node):
        x, y = node.Position
        return {
            "nw"    : self.get_node(Pos(x-1 , y-1)),
            "n"     : self.get_node(Pos(x-1 , y  )),
            "ne"    : self.get_node(Pos(x-1 , y+1)),
            "W"     : self.get_node(Pos(x   , y-1)),
            "e"     : self.get_node(Pos(x   , y+1)),
            "sw"    : self.get_node(Pos(x+1 , y-1)),
            "s"     : self.get_node(Pos(x+1 , y  )),
            "se"    : self.get_node(Pos(x+1 , y+1))
        }
    
    def get_neighbors_with_letter(self, node: Node, letter: str):
        neighbors = self.get_neighbors(node)
        return [(neighbors[node_key], node_key) for node_key in neighbors if neighbors[node_key] and neighbors[node_key].Letter == letter]
    
    def get_neighbor_inDir(self, node: Node, dir: str):
        neighbors = self.get_neighbors(node)
        return neighbors[dir]
    
    def get_graph_list(self) -> list[Node]: #make list from left to right
        return [inner_value for outer in self.Graph.values() for inner_value in outer.values()]

    def search_for_xmas(self):
    ###: Helper function
        #: Search through nodes in a direction
        def search(connection_to_search: Node, letter_lookup: str, direction: str):
            if connection_to_search.Letter == "S":
                return 1 #: Hit
            
            #: Get next node and check if letter mach next letter
            next_node = self.get_neighbor_inDir(connection_to_search, direction) 
            if next_node == None:
                return 0
            elif next_node.Letter == NEXT[letter_lookup]:
                return search(next_node, NEXT[letter_lookup], direction)
            else:
                return 0            
    #: Go through the nodes in the Graph and count 'Xmas'
        hits = 0
        for current_node in self.get_graph_list():
            if not current_node.Letter == "X":
                continue #: Skip non X letters

        #: Find sub_nodes with potential xmas
            #: Same charecters can overlap, sum list of potentionally multiple xmas'
            m_nodes  = self.get_neighbors_with_letter(current_node, "M")
            hits    += sum([search(node, "M", dir) for node, dir in m_nodes])
        return hits
    
    def search_for_mas(self):
        hits = 0
        for current_node in self.get_graph_list():
            #: Skip any letter that isn't 'A'
            if not current_node.Letter == "A":
                continue
            
            #: Find relevant nodes
            neightbors = self.get_neighbors(current_node)
            diagonals  = ["nw", "ne", "se", "sw"]
            diagonal_nodes = [neightbors[di_key] for di_key in diagonals]
            if diagonal_nodes.count(None) > 0:
                continue #: invalid
    
            diagonal_letter= [node.Letter for node in diagonal_nodes if node]
            
            #: validate
            m_node_count = diagonal_letter.count("M")
            s_node_count = diagonal_letter.count("S")
            correct_amount = m_node_count == 2 and s_node_count == 2

            if neightbors["nw"].Letter == neightbors["se"].Letter or not correct_amount:
                continue  #: Not valid 
            else:
                hits += 1 #: Valid
        return hits




if __name__ == "__main__": #: Test data
    g = Graph("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""")
    
    a = Pos(0,4)
    node = g.get_node(a)
    for node in g.get_graph_list():
        print(node.Letter)

    
    