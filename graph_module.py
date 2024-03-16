from trees_module import TreeNode

class Graph:
    def __init__(self, directed = True):
        self.adjacency_list = {}
        self.directed = True
    
    def add_node(self, node, *values):
        self.adjacency_list[node] = [*values]
    
    def find_path(self, from_node, to_node):
        start = [from_node]
        visited = {}
        while len(start > 0):
            current_node = start.pop()
            visited[current_node] = True
            if current_node == to_node:
                return True
            else:
                nodes_to_visit = to_node.children
                start += [node for node in nodes_to_visit if node not in visited]
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print("")
            print(f"{vertex} body type is well suited to wear: ")
            vertex_neighbors = self.adjacency_list[vertex]
            if len(vertex_neighbors)== 0:
                print("no edges!")
            for adjacent_vertex in vertex_neighbors:
                print("=> " + adjacent_vertex.value)
                