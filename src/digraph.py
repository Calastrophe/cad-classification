from helpers import LOGGER
from parsers import STPFile
import re
import subprocess

class Node:
    def __init__(self, id, type, parameters):
        self.id = id
        self.type = type
        self.parameters = parameters
        self.edges = []
    
    def add_edge(self, index: int):
        self.edges.append(index)


## A linear array which gives the illusion of a graph using indices.
class UndirectedGraph:
    def __init__(self):
        self.nodes: list[Node] = []

    def construct_nodes(self, stp_file: STPFile) -> list[Node]:
        for object in stp_file.data:
            node_id, type_n_params = object.split("=")
            node_type, params = type_n_params.split("(", 1)
            params = params.replace("(", "").replace(")", "").split(",")
            self.nodes.append(Node(node_id.strip()[1:], node_type.strip(), params))
    
    def link_nodes(self):
        for node in reversed(self.nodes):
            for param in node.parameters:
                if "#" in param:
                    index = int(re.sub('\D', '', param)) - 1
                    node.add_edge(index)

    def dot_file(self):
        with open("output.dot", "w") as fd:
            fd.write('graph G {\n\tfontname="Comic Sans MS"\n')
            for node in self.nodes:
                fd.write(f'\t{node.id} [label={node.type}, color=webmaroon]\n')
                for edge in node.edges:
                    ret_edge = self.nodes[edge]
                    fd.write(f'\t{node.id} -- {ret_edge.id}\n')
            fd.write('}')

    def pdf(self, output_name):
        self.dot_file()
        subprocess.run(f'sfdp -Tpdf -Gdpi=300 output.dot -o {output_name}.pdf', shell=True)
                
    
                

if __name__ == "__main__":
    some_stp = STPFile("data/example.stp")
    new_graph = UndirectedGraph()
    new_graph.construct_nodes(some_stp)
    new_graph.link_nodes()
    new_graph.pdf("hi")